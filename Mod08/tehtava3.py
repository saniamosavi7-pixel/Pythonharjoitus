class Hissi:
    def __init__(self, alin, ylin):
        self.alin, self.ylin, self.nykyinen = alin, ylin, alin

    def siirry(self, kohde):
        while self.nykyinen != kohde:
            self.nykyinen += 1 if self.nykyinen < kohde else -1
            print(f"Hissi on nyt kerroksessa {self.nykyinen}")

class Talo:
    def __init__(self, alin, ylin, lkm):
        self.alin = alin
        self.hissit = [Hissi(alin, ylin) for _ in range(lkm)]

    def aja(self, nro, kohde):
        self.hissit[nro - 1].siirry(kohde)

    def palohälytys(self):
        for h in self.hissit:
            h.siirry(self.alin)

talo = Talo(1, 10, 2)
talo.aja(1, 5)
talo.aja(1, 1)
talo.palohälytys()