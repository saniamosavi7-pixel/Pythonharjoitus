def karsi_parittomat(luvut):
    return [luku for luku in luvut if luku % 2 == 0]

def paakirjoitus():
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = karsi_parittomat(alkuperainen_lista)
    print(f"Alkuperäinen lista: {alkuperainen_lista}")
    print(f"Karsittu lista (vain parilliset): {karsittu_lista}")

if __name__ == "__main__":
    paakirjoitus()