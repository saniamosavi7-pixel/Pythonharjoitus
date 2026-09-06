pelaaja_nimi = ""
pelaaja_ika = 0
inventaario = []
pelaaja_hp = 100




def tutki_maailmaa():
    """Toiminto 1: Kysyy käyttäjältä esineen ja lisää sen inventaariolistaan."""
    global pelaaja_hp
    print("\n--- TUTKIMUSRETKI ---")
    print("Löysit vanhan aarrearkun!")

    esine = input("Mitä löysit arkusta? (esim. Miekka, Terveysjuoma, Avain): ").strip()

    if esine:
        inventaario.append(esine)
        print(f"-> Lisäsit esineen '{esine}' inventaarioosi!")
    else:
        print("-> Et ottanut mitään mukaasi.")

    pelaaja_hp -= 10
    print(f"Tutkimusretki väsytti sinua. HP: {pelaaja_hp}/100\n")


def nayta_inventaario():
    """Toiminto 2: Tulostaa inventaariolistan sisällön sekä pelaajan tilanteen."""
    print(f"\n--- PELAAJAN TILA: {pelaaja_nimi.upper()} ({pelaaja_ika} v) ---")
    print(f"Elämäpisteet (HP): {pelaaja_hp}/100")
    print("Mukanasi olevat esineet:")

    if not inventaario:
        print(" (Inventaario on tyhjä)")
    else:
        for indeksi, esine in enumerate(inventaario, start=1):
            print(f" {indeksi}. {esine}")
    print("-----------------------------------\n")


def lepaa_nuotiolla():
    """Toiminto 3: Lisätoiminto, joka palauttaa pelaajan HP-pisteitä."""
    global pelaaja_hp
    print("\n--- NUOTIO ---")
    if pelaaja_hp >= 100:
        print("Olet jo täysissä voimissa, et tarvitse lepoa.")
    else:
        parannus = 25
        pelaaja_hp = min(100, pelaaja_hp + parannus)
        print(f"Lepäsit nuotiolla ja voimasi palautuivat! HP: {pelaaja_hp}/100")
    print("--------------\n")




def paaohjelma():
    global pelaaja_nimi, pelaaja_ika

    print("====================================")
    print("   TERVETULOA SEIKKAILUPELIIN!      ")
    print("====================================\n")

    pelaaja_nimi = input("Syötä pelaajan nimi: ").strip()
    pelaaja_ika = input("Syötä pelaajan ikä: ").strip()

    print(
        f"\nTervetuloa peliin, {pelaaja_nimi}! Ikäsi on taltioitu ({pelaaja_ika} vuotta)."
    )
    print("Peli alkaa...\n")

    while True:
        print("=== PÄÄVALIKKO ===")
        print("1. Lähde tutkimusretkelle (Etsi esineitä)")
        print("2. Tarkista inventaario ja tila")
        print("3. Lepää nuotiolla (Palauta HP)")
        print("4. Lopeta peli")

        valinta = input("Mitä haluat tehdä? (1-4): ").strip()

        if valinta == "1":
            tutki_maailmaa()
        elif valinta == "2":
            nayta_inventaario()
        elif valinta == "3":
            lepaa_nuotiolla()
        elif valinta == "4":
            print(
                f"\nKiitos pelaamisesta, {pelaaja_nimi}! Peli päättyi. Näkemiin!"
            )
            break
        else:
            print("-> Virheellinen valinta, syötä numero 1–4.\n")


if __name__ == "__main__":
    paaohjelma()