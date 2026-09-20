class Esine:
    def __init__(self, nimi: str, paino: float):
        self.nimi = nimi
        self.paino = paino

    def __str__(self):
        return f"{self.nimi} ({self.paino} kg)"

class Huone:
    def __init__(self, nimi: str, esine: Esine = None):
        self.nimi = nimi
        self.esine = esine  

    def __str__(self):
        esine_str = f", jossa on esine: {self.esine}" if self.esine else ", tyhjä huone"
        return f"Huone: {self.nimi}{esine_str}"

class Pelaaja:
    def __init__(self, nimi: str, sijainti: Huone):
        self.nimi = nimi
        self.esineet = []  
        self.sijainti = sijainti

    def liiku(self, kohde: Huone):
        self.sijainti = kohde
        print(f"{self.nimi} siirtyi huoneeseen: {kohde.nimi}")

    def keraa_esine(self):
        if self.sijainti.esine:
            otettava = self.sijainti.esine
            self.esineet.append(otettava)
            print(f"Keräsit esineen: {otettava.nimi}")
            self.sijainti.esine = None
        else:
            print("Tässä huoneessa ei ole esinettä kerättäväksi.")


def paajohto():
   
    miekka = Esine("Miekka", 3.5)
    avain = Esine("Avain", 0.2)

    eteinen = Huone("Eteinen", avain)
    olohuone = Huone("Olohuone", miekka)
    keittio = Huone("Keittiö", None)

    pelaaja = Pelaaja("Seikkailija", eteinen)

    huoneet = {"1": eteinen, "2": olohuone, "3": keittio}

    while True:
        print("\n--- PELIVALIKKO ---")
        print(f"Pelaaja: {pelaaja.nimi}")
        print(f"Nykyinen sijainti: {pelaaja.sijainti}")
        print("Reppu:")
        if pelaaja.esineet:
            for e in pelaaja.esineet:
                print(f" - {e}")
        else:
            print(" (tyhjä)")

        print("\nValitse toiminto:")
        print("1: Liiku toiseen huoneeseen")
        print("2: Kerää huoneessa oleva esine")
        print("0: Lopeta peli")

        valinta = input("Valintasi: ")

        if valinta == "1":
            print("\nValitse huone:")
            print("1: Eteinen")
            print("2: Olohuone")
            print("3: Keittiö")
            huone_valinta = input("Mihin huoneeseen haluat liikkua? ")
            if huone_valinta in huoneet:
                pelaaja.liiku(huoneet[huone_valinta])
            else:
                print("Virheellinen huonevalinta.")

        elif valinta == "2":
            pelaaja.keraa_esine()

        elif valinta == "0":
            print("Lopetetaan peli. Hei hei!")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    paajohto()