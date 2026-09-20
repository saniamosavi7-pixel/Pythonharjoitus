from autot.malli import Sähköauto, Polttomoottoriauto

if __name__ == "__main__":
    sahkoauto = Sähköauto("ABC-15", 180, 52.5)
    polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sahkoauto.kiihdytä(120)
    polttomoottoriauto.kiihdytä(100)

    sahkoauto.kulje(3)
    polttomoottoriauto.kulje(3)

    print(f"Sähköauton ({sahkoauto.rekisteritunnus}) matkamittarilukema: {sahkoauto.matkamittari} km")
    print(f"Polttomoottoriauton ({polttomoottoriauto.rekisteritunnus}) matkamittarilukema: {polttomoottoriauto.matkamittari} km")