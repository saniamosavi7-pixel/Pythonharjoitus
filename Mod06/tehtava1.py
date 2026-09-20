def maarita_vuodenaika():
    vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
    kk_numero = int(input("Anna kuukauden numero (1-12): "))
    
    if 1 <= kk_numero <= 12:
        vuodenaika = vuodenajat[kk_numero - 1]
        print(f"Kuukausi {kk_numero} kuuluu vuodenaikaan: {vuodenaika}")
    else:
        print("Virheellinen kuukauden numero. Anna luku väliltä 1-12.")

if __name__ == "__main__":
    maarita_vuodenaika()