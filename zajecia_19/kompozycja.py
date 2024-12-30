class Silnik:
    def __init__(self, moc, pojemnosc):
        self.moc = moc
        self.pojemnosc = pojemnosc

    def uruchom(self):
        print(f"Uruchomilem silnik o mocy {self.moc} i pojemnosci {self.pojemnosc}")


class Samochod:
    def __init__(self, marka, model, kolor, silnik):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.silnik = silnik

    def uruchom_silnik(self):
        if isinstance(self.silnik, Silnik):
            self.silnik.uruchom()
        else:
            print("Niestety twoj silnik nie jest silnikiem")

silnik_1_9_tdi = Silnik(moc=90, pojemnosc="1.9")

auto = Samochod(marka="Audi", model="A4", kolor="czarny", silnik=silnik_1_9_tdi)
auto_1 = Samochod(marka="Audi", model="A4", kolor="czarny", silnik="1.9 TDI")

auto.uruchom_silnik()

auto_1.uruchom_silnik()