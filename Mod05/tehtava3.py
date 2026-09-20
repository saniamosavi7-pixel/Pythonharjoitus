def gallonat_litroiksi(gallonat):
    return gallonat * 3.78541

def paakirjoitus():
    while True:
        syote= float(input("Anna bensiinin määrä gallononia (negatiivien luku lopettaa )"))
        if syote < 0 :
            break 
        muutetut_litrat = gallonat_litroiksi(syote)
        print(f"{syote} gallonaa on {muutetut_litrat:.3f} litraa.")

        if __name__ == "__main__":
            paakirjoitus()