import math

def laske_yksikkohinta(halkaisija_cm, hinta):
    sade_m = (halkaisija_cm / 100) / 2
    pinta_ala = math.pi * (sade_m ** 2)
    return hinta / pinta_ala

def paakirjoitus():
    halkaisija1 = float(input("Anna 1. pizzan halkaisija senttimetreinä: "))
    hinta1 = float(input("Anna 1. pizzan hinta euroina: "))

    halkaisija2 = float(input("Anna 2. pizzan halkaisija senttimetreinä: "))
    hinta2 = float(input("Anna 2. pizzan hinta euroina: "))

    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    print(f"\n1. pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
    print(f"2. pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Pizzoilla on sama yksikköhinta.")

if __name__ == "__main__":
    paakirjoitus()