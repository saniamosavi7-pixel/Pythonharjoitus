lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")
    
    valinta = input("Valintasi (1, 2 tai 3): ")
    
    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) tallennettu.")
        
    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema ICAO-koodilla {icao} on {lentoasemat[icao]}.")
        else:
            print("Kyseistä ICAO-koodia ei löytynyt.")
            
    elif valinta == "3":
        print("Lopetetaan ohjelman suoritus.")
        break
    else:
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")