import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa_alkio_listaan(1)
    joukko.lisaa_alkio_listaan(2)
    joukko.lisaa_alkio_listaan(3)
    joukko.lisaa_alkio_listaan(6)
    joukko.lisaa_alkio_listaan(7)
    joukko.lisaa_alkio_listaan(8)
    joukko.lisaa_alkio_listaan(9)
    joukko.lisaa_alkio_listaan(10)
    joukko.lisaa_alkio_listaan(11)
    joukko.lisaa_alkio_listaan(12)
    joukko.lisaa_alkio_listaan(13)
    joukko.lisaa_alkio_listaan(4)
    joukko.lisaa_alkio_listaan(5)

    print(joukko.to_int_list())
    joukko.poista_alkio_listasta(4)
 


    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
