class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        self.matkamittari += self.nopeus * tuntimäärä

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

if __name__ == "__main__":
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdytä(120)
    polttomoottoriauto.kiihdytä(100)

    sahkoauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print(f"Sähköauton ({sahkoauto.rekisteritunnus}) matkamittarilukema: {sahkoauto.matkamittari} km")
    print(f"Polttomoottoriauton ({polttomoottoriauto.rekisteritunnus}) matkamittarilukema: {polttomoottoriauto.matkamittari} km")