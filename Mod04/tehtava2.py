luvut = []

while True:
    syote = input("Syötä luku (tyhjä lopettaa): ")
    
    if syote == "":
        break
        
    luvut.append(float(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)