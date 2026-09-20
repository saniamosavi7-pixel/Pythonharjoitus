class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa: {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for _ in range(hissien_lukumäärä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kohdekerros}:")
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

def paakirjoitus():
    talo = Talo(1, 10, 3)
    
    talo.aja_hissiä(1, 5)
    talo.aja_hissiä(2, 8)
    talo.aja_hissiä(1, 1)

if __name__ == "__main__":
    paakirjoitus()