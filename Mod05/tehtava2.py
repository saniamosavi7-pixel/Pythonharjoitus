import random 

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

def paakirjoitus():
    tahkot= int(input("Anna nopan tahkojen yhteismäärä:"))
    silmaluku = 0
    while silmaluku != tahkot:
        silmaluku = heita_noppaa(tahkot)
        print(f"heitto: {silmaluku}")

if __name__ == "__main__":
    paakirjoitus()