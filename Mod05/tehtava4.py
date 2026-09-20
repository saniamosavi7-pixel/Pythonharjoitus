def laske_summa(luvut):
    return sum(luvut)

def paakirjoitus():
    testilista = [2, 4, 6, 8, 10, 12]
    tulos = laske_summa(testilista)
    print(f"Listan lukujen summa on: {tulos}")

if __name__ == "__main__":
    paakirjoitus()