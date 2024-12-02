from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self.edeltava_komento = []
        self.komennot ={
            Komento.SUMMA : Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS : Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS : Nollaus(sovelluslogiikka),
            Komento.KUMOA : Kumous(self.edeltava_komento)
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        try:
            return int(self._syote_kentta.get())
        except ValueError:
            return 0

    def _suorita_komento(self, komento):
        if komento in self.komennot:
            komento_olio = self.komennot[komento]
            komento_olio.suorita()

            if isinstance(komento_olio, Summa) or isinstance(komento_olio, Erotus):
                self.edeltava_komento.append((komento_olio,self._lue_syote()))

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

class Summa():
    def __init__(self, laskin, syote):
        self.laskin = laskin
        self.syote = syote
    
    def suorita(self):
        self.laskin.plus(self.syote())
    
    def kumoa(self, arvo):
        self.laskin.miinus(arvo)

class Erotus():
    def __init__(self, laskin, syote):
        self.laskin = laskin
        self.syote = syote
    
    def suorita(self):
        self.laskin.miinus(self.syote())

    def kumoa(self,arvo):
        self.laskin.plus(arvo)

class Nollaus():
    def __init__(self, laskin):
        self.laskin = laskin
    
    def suorita(self):
        self.laskin.nollaa()

class Kumous():
    def __init__(self, komento):
        self.komento = komento
    
    def suorita(self):
        try:
            edeltava_suoritus, arvo = self.komento.pop()
            edeltava_suoritus.kumoa(arvo)
        except IndexError:
            pass