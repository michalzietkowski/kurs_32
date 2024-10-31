from helpers import wymien_zarowke

class Mlotek:
    def __init__(self, kolor, rozmiar):
        self.kolor = kolor
        self.rozmiar = rozmiar

    def wypozycz(self):
        print("Wypozyczyles mlotek swojemu koledze")

class Kosiarka:
    def __init__(self, rodzaj_ostrza, moc, typ):
        self.rodzaj_ostrza = rodzaj_ostrza
        self.moc = moc
        self.typ = typ

    def skos_trawnik(self):
        print("Skosilismy trawnik")

class Pilarka:
    def __init__(self, rodzaj_ostrza, typ):
        self.rodzaj_ostrza = rodzaj_ostrza
        self.typ = typ

    def spiluj_cos(self, przedmiot):
        print(f"Spilowalem {przedmiot}")

class Srubokret:
    def __init__(self, typ_nitu, kolor):
        self.typ_nita = typ_nitu
        self.kolor = kolor

    def skrec_cos(self):
        print("skreciles przedmiot")


zmienna_1 = "hahaha"