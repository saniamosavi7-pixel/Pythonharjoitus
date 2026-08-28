LUOTI_GRAMMOINA = 13.3
NAULA_LUOTEINA = 32
LEIVISKA_NAULOINA = 20

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

yhteensa_luodit = luodit + (naulat * NAULA_LUOTEINA) + (leiviskat * LEIVISKA_NAULOINA * NAULA_LUOTEINA)

yhteensa_grammat = yhteensa_luodit * LUOTI_GRAMMOINA
kilogrammat = int(yhteensa_grammat // 1000)
grammat = yhteensa_grammat % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")