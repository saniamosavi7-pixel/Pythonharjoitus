class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 2000  # Asetettu esimerkkitilannetta varten (tai alussa 0)

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos
        
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntimaara

def paakirjoitus():
    uusi_auto = Auto("ABC-123", 142)
    uusi_auto.tamanhetkinen_nopeus = 60  # Esimerkin mukainen nopeus
    uusi_auto.kuljettu_matka = 2000     # Esimerkin mukainen lähtömatka
    
    print(f"Matka ennen ajoa: {uusi_auto.kuljettu_matka} km")
    
    uusi_auto.kulje(1.5)
    
    print(f"Matka ajon jälkeen (1.5 h @ 60 km/h): {uusi_auto.kuljettu_matka} km")

if __name__ == "__main__":
    paakirjoitus()