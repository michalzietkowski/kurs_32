def nazwa_funkcji(parametr_1, parametr_2):
    print(parametr_1)
    return "moje imie"

imie = nazwa_funkcji("123", 23)
nowe_imie = nazwa_funkcji(parametr_2="55555", parametr_1="12345")
print(imie)

class Samochod:
    def __init__(self, marka, kolor):
        self.marka_samochodu = marka
        self.kolor_samochodu = kolor

    def zmien_kolor_auta(self, nowy_kolor):
        self.kolor_samochodu = nowy_kolor


audi = Samochod(marka="audi", kolor="czarny")
print(audi.kolor_samochodu)
print(audi.marka_samochodu)
audi.zmien_kolor_auta(nowy_kolor="czerwony")
print(audi.kolor_samochodu)