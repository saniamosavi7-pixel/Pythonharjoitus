from .esine import Esine

class Huone:
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine  # Esine tai None, jos huone on tyhjä
        self.naapurit = {}  # Sanakirja naapurihuoneille

    def __str__(self):
        if self.esine:
            return f"Huone: {self.nimi}. Täällä näkyy esine: {self.esine}"
        return f"Huone: {self.nimi}. Täällä ei ole esineitä."