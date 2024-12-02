KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:

    def __init__(self, maksimi_kapasiteetti:int=KAPASITEETTI, kasvatuskoko:int=OLETUSKASVATUS):

        if not isinstance(maksimi_kapasiteetti, int) or maksimi_kapasiteetti < 0:
            raise Exception("Väärä maksimi_kapasiteetti")

        self.maksimi_kapasiteetti = maksimi_kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = self._luo_lista(self.maksimi_kapasiteetti)
        self.alkioiden_lukumaara = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluuko_alkio_listaan(self, a):
        if a in self.lukujono:
            return True

        return False

    def lisaa_alkio_listaan(self, a):

        if not self.kuuluuko_alkio_listaan(a):
            self.lukujono[self.alkioiden_lukumaara] = a
            self.alkioiden_lukumaara += 1

            if self.alkioiden_lukumaara == self.maksimi_kapasiteetti:
                taulukko_old = []
                self.kopioi_lista(self.lukujono, taulukko_old)
                self.lukujono = self._luo_lista(self.maksimi_kapasiteetti + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.lukujono)

    def poista_alkio_listasta(self, n):
        self.lukujono.remove(n)
        self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1

    def kopioi_lista(self, a, b):
        for item in a:
            b.append(item)

    def listan_alkioiden_lukumaara(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lukumaara)

        for i in range(len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_arvo in a_taulu:
            x.lisaa_alkio_listaan(a_arvo)

        for b_arvo in b_taulu:
            x.lisaa_alkio_listaan(b_arvo)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_arvo in a_taulu:
            if a_arvo in b_taulu:
                y.lisaa_alkio_listaan(a_arvo)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_arvo in a_taulu:
            if a_arvo not in b_taulu:
                z.lisaa_alkio_listaan(a_arvo)

        return z

    def __str__(self):
        tuotos = "{"

        if self.alkioiden_lukumaara>1:
            for i in range(self.alkioiden_lukumaara - 1):
                tuotos += str(self.lukujono[i]) + ", "
            tuotos += str(self.lukujono[self.alkioiden_lukumaara - 1])

        elif self.alkioiden_lukumaara == 1:
            tuotos += str(self.lukujono[0])

        tuotos = tuotos + "}"

        return tuotos
