class Pelaaja:
    def __init__(self, nimi, aloitus_huone):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = aloitus_huone

    def liiku(self, uusi_huone):
        self.sijainti = uusi_huone
        print(f"{self.nimi} siirtyi huoneeseen: {uusi_huone.nimi}")

    def keraa_esine(self):
        if self.sijainti.esine:
            loytynyt_esine = self.sijainti.esine
            self.esineet.append(loytynyt_esine)
            print(f"Poimit esineen: {loytynyt_esine.nimi}")
            self.sijainti.esine = None
        else:
            print("Täällä ei ole mitään kerättävää.")

    def __str__(self):
        esineiden_nimet = ", ".join([e.nimi for e in self.esineet]) if self.esineet else "Ei esineitä"
        return f"Pelaaja: {self.nimi} | Sijainti: {self.sijainti.nimi} | Reppu: {esineiden_nimet}"