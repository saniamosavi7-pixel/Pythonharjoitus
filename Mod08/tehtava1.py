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

def paakirjoitus():
    hissi = Hissi(1, 5)
    
    print("Siirretään hissi 5. kerrokseen:")
    hissi.siirry_kerrokseen(5)
    
    print("\nSiirretään hissi takaisin alimpaan kerrokseen:")
    hissi.siirry_kerrokseen(1)

if __name__ == "__main__":
    paakirjoitus()