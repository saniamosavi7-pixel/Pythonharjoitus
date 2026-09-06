class Koira:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

koirat= []
svuosi = 2016
nimi = "a"
for i in range(10):
    koirat .append(Koira(nimi, svuosi))
    svuosi += 1
    nimi_int = int(nimi)
    nimi_int = nimi_int + 1
    nimi = str(nimi_int)
    
    
    