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

def paakirjoitus():
    uusi_auto = Auto("ABC-123", 142)
    
    uusi_auto.kiihdyta(30)
    uusi_auto.kiihdyta(70)
    uusi_auto.kiihdyta(50)
    
    print(f"Auton nopeus kiihdytysten jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")
    
    uusi_auto.kiihdyta(-200)
    print(f"Auton nopeus hätäjarrutuksen jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")

if __name__ == "__main__":
    paakirjoitus()