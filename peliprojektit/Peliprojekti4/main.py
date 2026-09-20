from peli.esine import Esine
from peli.huone import Huone
from peli.pelaaja import Pelaaja

def main():
    print("--- TERVETULOA SEIKKAILUPELIIN! ---")

    avain = Esine("Kultainen avain", 0.5)
    kirja = Esine("Vanha kirja", 1.2)

    eteinen = Huone("Eteinen", avain)
    keittio = Huone("Keittiö", kirja)
    oleskelutila = Huone("Oleskelutila", None)

    eteinen.naapurit = {"keittiö": keittio, "oleskelutila": oleskelutila}
    keittio.naapurit = {"eteinen": eteinen}
    oleskelutila.naapurit = {"eteinen": eteinen}

    nimi = input("Anna pelaajan nimi: ")
    pelaaja = Pelaaja(nimi, eteinen)

    while True:
        print("\n" + "="*30)
        print(pelaaja)
        print(pelaaja.sijainti)
        
        print("\nMitä haluat tehdä?")
        print("1 = Kerää esine")
        print("2 = Liiku toiseen huoneeseen")
        print("0 = Lopeta peli")
        
        valinta = input("Valintasi: ")

        if valinta == "1":
            pelaaja.keraa_esine()
        elif valinta == "2":
            print("Voit mennä huoneisiin:")
            for suunta in pelaaja.sijainti.naapurit:
                print(f"- {suunta}")
            suunta = input("Mihin huoneeseen haluat mennä? ").strip().lower()
            
            if suunta in pelaaja.sijainti.naapurit:
                uusi_huone = pelaaja.sijainti.naapurit[suunta]
                pelaaja.liiku(uusi_huone)
            else:
                print("Sinne ei voi mennä tästä huoneesta!")
        elif valinta == "0":
            print("Kiitos pelaamisesta! Hei hei.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    main()