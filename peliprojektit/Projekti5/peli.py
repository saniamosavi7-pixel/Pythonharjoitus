import os

INTRO_TIEDOSTO = "intro.txt"
OHJEET_TIEDOSTO = "ohjeet.txt"

def lue_tekstitiedosto(tiedoston_nimi):
    """Lukee ja palauttaa tiedoston sisällön."""
    if os.path.exists(tiedoston_nimi):
        with open(tiedoston_nimi, "r", encoding="utf-8") as f:
            return f.read()
    return f"(Tiedostoa {tiedoston_nimi} ei löytynyt.)"

def lataa_peli(nimi):
    """Yrittää ladata olemassa olevan pelitallennuksen pelaajan nimellä."""
    tallenne_nimi = f"talla_{nimi.lower()}.txt"
    if os.path.exists(tallenne_nimi):
        with open(tallenne_nimi, "r", encoding="utf-8") as f:
            rivit = f.read().splitlines()
            if len(rivit) >= 2:
                pisteet = int(rivit[0])
                sijainti = rivit[1]
                return {"pisteet": pisteet, "sijainti": sijainti}
    return None

def tallenna_peli(nimi, tila):
    """Tallentaa pelaajan tilanteen tiedostoon."""
    tallenne_nimi = f"talla_{nimi.lower()}.txt"
    with open(tallenne_nimi, "w", encoding="utf-8") as f:
        f.write(f"{tila['pisteet']}\n{tila['sijainti']}\n")
    print(f"-> Peli tallennettiin onnistuneesti!")

def kaynnista_peli():
    print("=" * 30)
    print(lue_tekstitiedosto(INTRO_TIEDOSTO))
    print("-" * 30)
    print(lue_tekstitiedosto(OHJEET_TIEDOSTO))
    print("=" * 30 + "\n")

    nimi = input("Anna nimesi: ").strip()
    if not nimi:
        nimi = "Pelaaja"

    tallennettu_tila = lataa_peli(nimi)
    if tallennettu_tila:
        valinta = input(f"Hei {nimi}, löysimme vanhan tallennuksen! Haluatko jatkaa siitä (k/e)? ").strip().lower()
        if valinta == 'k':
            peli_tila = tallennettu_tila
            print(f"Jatketaan peliä paikasta: {peli_tila['sijainti']}, pisteet: {peli_tila['pisteet']}")
        else:
            peli_tila = {"pisteet": 0, "sijainti": "Metsänreuna"}
            print("Aloitetaan uusi peli.")
    else:
        peli_tila = {"pisteet": 0, "sijainti": "Metsänreuna"}
        print(f"Tervetuloa mukaan, {nimi}!")

    print("\nKirjoita komennot pienillä kirjaimilla.")
    while True:
        komento = input(f"\n[{peli_tila['sijainti']}] Komento ('liiku', 'tallenna', 'lopeta'): ").strip().lower()
        
        if komento == "lopeta":
            print("Hei hei, nähdään pian uudestaan!")
            break
        elif komento == "tallenna":
            tallenna_peli(nimi, peli_tila)
        elif komento == "liiku":
            peli_tila['pisteet'] += 10
            peli_tila['sijainti'] = "Vanha mökki"
            print("Liikut uuteen paikkaan! Pisteet kasvoivat.")
        else:
            print("Tuntematon komento. Kokeile 'liiku', 'tallenna' tai 'lopeta'.")

if __name__ == "__main__":
    kaynnista_peli()