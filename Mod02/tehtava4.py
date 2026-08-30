def main():
    try:
        vuosi = int(input("Anna vuosiluku: "))
    except ValueError:
        print("Virheellinen vuosiluku.")
        return

    if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
        print("Vuosi on karkausvuosi.")
    else:
        print("Vuosi ei ole karkausvuosi.")

if __name__ == "__main__":
    main()