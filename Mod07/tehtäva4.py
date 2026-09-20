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

def paakirjoitus():
    autot = []
    
    # Luodaan 10 autoa
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))

    kilpailu_kaynnissa = True
    tunnit = 0

    # Kilpailusilmukka
    while kilpailu_kaynnissa:
        tunnit += 1
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)
            
            if auto.kuljettu_matka >= 10000:
                kilpailu_kaynnissa = False

    # Tulostetaan tulokset taulukkona
    print(f"\nKilpailu päättyi! Kesto: {tunnit} tuntia.\n")
    print(f"{'Rekisteritunnus':<15} | {'Huippunopeus (km/h)':<20} | {'Nopeus nyt (km/h)':<18} | {'Kuljettu matka (km)':<20}")
    print("-" * 81)
    
    for auto in autot:
        print(f"{auto.rekisteritunnus:<15} | {auto.huippunopeus:<20} | {auto.tamanhetkinen_nopeus:<18} | {auto.kuljettu_matka:<20}")

if __name__ == "__main__":
    paakirjoitus()