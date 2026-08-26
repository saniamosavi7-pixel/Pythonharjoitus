# Tehtävä 1
nimi = input("Anna nimesi: ")
print(f"Terve, {nimi}!")

# Tehtävä 2
import math

sade = float(input("Anna ympyrän säde: "))
pinta_ala = math.pi * sade**2
print(f"Ympyrän pinta-ala on {pinta_ala:.2f}")

#Tehtävät 3 
# Kysytään suorakulmion kanta ja korkeus
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# Lasketaan piiri (kaikkien neljän sivun summa) ja pinta-ala
piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

# Tulostetaan tulokset
print(f"Suorakulmion piiri on {piiri:.2f}")
print(f"Suorakulmion pinta-ala on {pinta_ala:.2f}")

# Tehtävät 4 
# Kysytään kolme kokonaislukua (int)
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

# Lasketaan summa, tulo ja keskiarvo
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

# Tulostetaan tulokset
print(f"Lukujen summa on {summa}")
print(f"Lukujen tulo on {tulo}")
print(f"Lukujen keskiarvo on {keskiarvo:.2f}")

# Tehtävät 5 
# Määritellään muuntokertoimet vakioksi
LUOTI_GRAMMOINA = 13.3
NAULA_LUOTEINA = 32
LEIVISKA_NAULOINA = 20

# Kysytään käyttäjältä leiviskät, naulat ja luodit
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Lasketaan kaikkien mittien yhteismäärä luoteina
yhteensa_luodit = luodit + (naulat * NAULA_LUOTEINA) + (leiviskat * LEIVISKA_NAULOINA * NAULA_LUOTEINA)

# Lasketaan kokonaisgrammat
yhteensa_grammat = yhteensa_luodit * LUOTI_GRAMMOINA

# Erotetaan täydet kilogrammat ja yli jäävät grammat
kilogrammat = int(yhteensa_grammat // 1000)
grammat = yhteensa_grammat % 1000

# Tulostetaan tulos
print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")

# Tehtävät 6
import random

# Arotaan 3-numeroinen koodi (numerot 0..9)
koodi1_numero1 = str(random.randint(0, 9))
koodi1_numero2 = str(random.randint(0, 9))
koodi1_numero3 = str(random.randint(0, 9))
koodi1 = koodi1_numero1 + koodi1_numero2 + koodi1_numero3

# Arpotaan 4-numeroinen koodi (numerot 1..6)
koodi2_numero1 = str(random.randint(1, 6))
koodi2_numero2 = str(random.randint(1, 6))
koodi2_numero3 = str(random.randint(1, 6))
koodi2_numero4 = str(random.randint(1, 6))
koodi2 = koodi2_numero1 + koodi2_numero2 + koodi2_numero3 + koodi2_numero4

# Tulostetaan koodit
print(f"3-numeroinen koodi: {koodi1}")
print(f"4-numeroinen koodi: {koodi2}")