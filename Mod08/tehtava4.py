import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntimaara

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{'Rekisteritunnus':<15} | {'Huippunopeus (km/h)':<20} | {'Nopeus nyt (km/h)':<18} | {'Kuljettu matka (km)':<20}")
        print("-" * 81)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15} | {auto.huippunopeus:<20} | {auto.tamanhetkinen_nopeus:<18} | {auto.kuljettu_matka:<20}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

def paakirjoitus():
    autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
    romuralli = Kilpailu("Suuri romuralli", 8000, autot)
    
    tunnit = 0
    while not romuralli.kilpailu_ohi():
        romuralli.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            print(f"\n--- Tilanne {tunnit} tunnin jälkeen ---")
            romuralli.tulosta_tilanne()
            
    print(f"\n=== KILPAILU PÄÄTTYI ({tunnit} tuntia) ===")
    romuralli.tulosta_tilanne()

if __name__ == "__main__":
    paakirjoitus()