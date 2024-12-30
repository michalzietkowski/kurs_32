

class Uczen:
    def __init__(self, imie, nazwisko, wiek, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.oceny = oceny


    def custom_method(self):
        print("To jest nasza customowa metoda")

    def __int__(self):
        return self.wiek

    def __str__(self):
        return self.imie

    def __bool__(self):
        return False if self.imie[-1].lower() != "a" else True

    def __getitem__(self, item):
        return self.oceny.get(item)

    def __setitem__(self, key, value):
        self.oceny[key] = value


uczen_1 = Uczen(imie="Michal", nazwisko="Zietkowski", wiek=12, oceny={
    "niemiecki": [1, 2, 3],
    "angielski": [4, 2, 5]
})
uczen_1.custom_method()
print(type(uczen_1))
print(int(uczen_1))
print(str(uczen_1))

print(bool(uczen_1))

print(uczen_1["niemiecki"])
uczen_1["matematyka"] = [4, 5, 5, 2]
print(uczen_1["matematyka"])

