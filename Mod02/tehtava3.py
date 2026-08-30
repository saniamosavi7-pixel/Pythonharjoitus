def main():
    sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").strip().lower()

    if sukupuoli != "nainen" and sukupuoli != "mies":
        print("Virheellinen sukupuoli.")
        return

    try:
        hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))
    except ValueError:
        print("Virheellinen hemoglobiiniarvo.")
        return

    if sukupuoli == "nainen":
        alaraja = 117
        yläraja = 175
    else:
        alaraja = 134
        yläraja = 195

    if hemoglobiini < alaraja:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini > yläraja:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

if __name__ == "__main__":
    main()