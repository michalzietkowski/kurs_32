class Pojazd:
    def __init__(self, marka, model, kolor, silnik, rok_produkcji):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.silnik = silnik
        self.rok_produkcji = rok_produkcji

    def uruchom_silnik(self):
        print(f"uruchomilem silnik {self.silnik}")

    def zmien_kolor(self, nowy_kolor):
        self.kolor = nowy_kolor
        print(f"zmienilem kolor na {nowy_kolor}")

class PojazdUMechanika:
    def polakieruj_drzwi(self):
        print("polakierowalem drzwi")

    def wymien_olej(self):
        print("wymienilem olej w silniku")

    def wymien_opone(self):
        print("wymienilem opone")

    def zaplac_za_naprawe(self):
        print("zaplacilem za naprawe")

    def zmien_kolor(self, nowy_kolor):
        print(f"Mechanik zmienił mi kolor na {nowy_kolor}")

class Samochod(Pojazd):
    def wymien_filtr_do_klimatyzacji(self):
        print("wymienilem filtr do klimatyzacji")

    def uruchom_silnik(self):
        print(f"Uruchomilem silnik w samochodzie!!!")
        super().zmien_kolor("czarny")

    def __init__(self, marka, model, kolor, silnik, rok_produkcji, ilosc_drzwi):
        self.ilosc_drzwi = ilosc_drzwi
        super().__init__(marka, model, kolor, silnik, rok_produkcji)


class Motocykl(Pojazd):
    def stan_deba(self):
        print("jade na jednym kole!")


class SamochodUMechanika(PojazdUMechanika, Samochod):
    pass



samochod = Samochod(marka="audi", model="a4", kolor="czarny", silnik="2.0 TDI", rok_produkcji=2020, ilosc_drzwi=5)
samochod.uruchom_silnik()
samochod.zmien_kolor("czerwony")
print(samochod.kolor)


alfa_romeo = SamochodUMechanika(marka="alfa romeo", model="giula", kolor="czerwony", silnik="1.9 JTD", rok_produkcji=1999, ilosc_drzwi=3)
alfa_romeo.polakieruj_drzwi()
alfa_romeo.zmien_kolor("czarny")