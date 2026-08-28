import random

koodi1_numero1 = str(random.randint(0, 9))
koodi1_numero2 = str(random.randint(0, 9))
koodi1_numero3 = str(random.randint(0, 9))
koodi1 = koodi1_numero1 + koodi1_numero2 + koodi1_numero3

koodi2_numero1 = str(random.randint(1, 6))
koodi2_numero2 = str(random.randint(1, 6))
koodi2_numero3 = str(random.randint(1, 6))
koodi2_numero4 = str(random.randint(1, 6))
koodi2 = koodi2_numero1 + koodi2_numero2 + koodi2_numero3 + koodi2_numero4

print(f"3-numeroinen koodi: {koodi1}")
print(f"4-numeroinen koodi: {koodi2}")