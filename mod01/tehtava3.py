import math


def main():
    # Kysytään säde käyttäjältä
    sade = float(input("Anna ympyrän säde: "))

    # Lasketaan ympyrän pinta-ala (A = π * r²)
    pinta_ala = math.pi * sade**2

    # Tulostetaan tulos
    print(f"Ympyrän pinta-ala on {pinta_ala:.2f}")


if __name__ == "__main__":
    main()