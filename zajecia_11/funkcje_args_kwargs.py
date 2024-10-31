def podaj_swoje_imie(imie):
    print(f"{imie}")

podaj_swoje_imie(imie="Michał")

def wyprintuj_wartosci(*args, **kwargs):
    print(args)
    print(type(args))
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(type(kwargs))
lista = [1, 2, 3, 4]
lista_1 = ""
# wyprintuj_wartosci(1, 434, "aaaa", "5454", False, ["123", True], {})
# wyprintuj_wartosci(1, 434, "aaaa", "5454", False, ["123", True], slownik={})
wyprintuj_wartosci(pusty_string = lista_1)
# wyprintuj_wartosci(lista)