import random

pisteet_yhteensa = int(input("Syötä arvottavien pisteiden määrä: "))

ympyran_sisalla = 0

for _ in range(pisteet_yhteensa):
    # Arvotaan x- ja y-koordinaatit väliltä [-1, 1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Tarkistetaan, onko piste yksikköympyrän sisällä (x^2 + y^2 < 1)
    if x**2 + y**2 < 1:
        ympyran_sisalla += 1

# Lasketaan piin likiarvo kaavalla: pi ≈ 4 * n / N
piin_likiarvo = 4 * ympyran_sisalla / pisteet_yhteensa

print(f"Piin likiarvo: {piin_likiarvo}")