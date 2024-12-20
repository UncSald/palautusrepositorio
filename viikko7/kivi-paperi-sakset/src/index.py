from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class PeliUI:
    def __init__(self):
        self.pelimuodot = {
            'a':KPSPelaajaVsPelaaja(),
            'b':KPSTekoaly(),
            'c':KPSParempiTekoaly()
        }

    def suorita(self):
        while True:
            print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                )
            vastaus = input()
            if vastaus not in self.pelimuodot.keys():
                break

            peliolio = self.pelimuodot[vastaus]
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            peliolio.pelaa()

def main():
    peli_liittymä = PeliUI()
    peli_liittymä.suorita()


if __name__ == "__main__":
    main()
