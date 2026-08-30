pituus = float(input("Syötä kuhan pituus senttimetreinä: "))

ALIMMITTA = 37

if pituus < ALIMMITTA:
    puuttuvat_sentit = ALIMMITTA - pituus
    print(f"Kuha on alamittainen! Laske se takaisin järveen.")
    print(f"Sallitusta pyyntimitasta puuttuu {puuttuvat_sentit:.1f} cm.")
else:
    print("Kuha on sallitun pyyntimitan mukainen, voit pitää sen!")