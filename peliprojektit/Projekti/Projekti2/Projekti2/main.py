def main():
    ika_syote = input("Anna ikäsi: ")
    ika = int(ika_syote)
    
    if ika < 12:
        print("Olet alaikäinen. Ohjelma suljetaan.")
    else:
        print("Tervetuloa peliin!")
        
        while True:
            print()
            print("--- VALIKKO ---")
            print("1. status")
            print("2. tutki")
            print("3. reppu")
            print("lopeta")
            print("---------------")
            
            komento = input("Anna komento: ").lower().strip()
            
            if komento == "lopeta":
                print("Ohjelma päättyy. Hei hei!")
                break
            elif komento == "status":
                print("Hahmosi voimatasot ovat täynnä (HP 100/100).")
            elif komento == "tutki":
                print("Löysit salaisen reitin kartan reunalta!")
            elif komento == "reppu":
                print("Repussasi on: taskulamppu, köysi ja omena.")
            else:
                print("Tuntematon komento, yritä uudelleen.")

main()