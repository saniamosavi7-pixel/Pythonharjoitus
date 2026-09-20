class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, Päätoimittaja: {self.päätoimittaja}")

if __name__ == "__main__":
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_no_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    aku_ankka.tulosta_tiedot()
    hytti_no_6.tulosta_tiedot()