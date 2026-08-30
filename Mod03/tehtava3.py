syote = input("Syötä luku: ")

if syote != "":
    pienin = float(syote)
    suurin = float(syote)

    while True:
        syote = input("Syötä luku: ")
        if syote == "":
            break
        
        luku = float(syote)
        
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku

    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")