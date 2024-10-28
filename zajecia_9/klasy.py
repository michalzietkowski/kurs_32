from cffi.cffi_opcode import PRIM_SCHAR

ciasta_cukierni_u_Michala = [
    {
        "nazwa": "makowiec",
        "cena_za_kg": 14.99,
        "skladniki": "maka, jajka, mak",
        "dostepnosc": True,
        "dostepna_ilosc": 10,
    },
    {
        "nazwa": "sernik",
        "cena_za_kg": 17.99,
        "skladniki": "maka, jajka, ser, rodzynki",
        "dostepnosc": True,
        "dostepna_ilosc": 12,
    },
]


class Ciasto:
    def __init__(
        self, nazwa_parametr, cena_za_kg, skladniki, dostepnosc, dostepna_ilosc
    ):
        self.nazwa = nazwa_parametr
        self.cena_za_kg = cena_za_kg
        self.skladniki = skladniki
        self.dostepnosc = dostepnosc
        self.dostepna_ilosc = dostepna_ilosc

    def zrob_ciasto(self):
        print(f"Robie ciasto {self.nazwa} ze składników {self.skladniki}")
        self.dostepna_ilosc += 1


makowiec = Ciasto(
    nazwa_parametr="makowiec",
    cena_za_kg=17.99,
    skladniki=["maka", "mak", "jajka", "mleko"],
    dostepnosc=True,
    dostepna_ilosc=10,
)
sernik = Ciasto(
    nazwa_parametr="sernik",
    cena_za_kg=14.99,
    skladniki=["maka", "ser", "jajka", "mleko"],
    dostepnosc=True,
    dostepna_ilosc=14,
)
print(sernik.nazwa)
print(sernik.skladniki)
print(sernik.dostepna_ilosc)
print(makowiec.dostepna_ilosc)
sernik.zrob_ciasto()
print(sernik.dostepna_ilosc)
print(makowiec.dostepna_ilosc)
