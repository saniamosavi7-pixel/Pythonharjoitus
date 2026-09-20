import random

def heita_noppaa():
    return random.randint(1, 6)

def paakirjoitus():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print(f"heitto: {silmaluku}")

if __name__ == "__main__":
    paakirjoitus()