import random

# age = int(input("Podaj swoj wiek: "))
# if age >= 18:
#     is_adult = True
# else:
#     is_adult = False
#
# print(is_adult)
#
# is_adult = True if age >= 18 else False
#
# print(is_adult)
from zajecia_11.funkcje_args_kwargs import lista

# nazwa_zmiennej = pierwsza_wartosc if <instrukcja warunkowa, ktora jest zgodna z pierwsza wartoscia> else druga_wartosc


uczniowie = ["Michal", "ADAM", "WoJtEk", "zoSia", "gosiA"]

# poprawieni_uczniowie = []
# for uczen in uczniowie:
#     poprawieni_uczniowie.append(uczen.capitalize())
#
# print(poprawieni_uczniowie)
#
# poprawieni_uczniowie_list_comprehension = [uczen.capitalize() for uczen in uczniowie]
#
#
#
# #skladnia
# # nowa_lista = [<wartosc, ktora ma byc w liscie> for tymczasowa_zmienna_do_iteracji in <obiekt iterowalny> ]
#
# print(poprawieni_uczniowie_list_comprehension)


lista_uczennic = []
for uczen in uczniowie:
    if uczen.lower()[-1] == "a":
        lista_uczennic.append(uczen.capitalize())

print(lista_uczennic)

lista_uczennic_druga_opcja = [uczen.capitalize() for uczen in uczniowie if uczen.lower()[-1] == "a"]
lista_uczniow_meskich = [uczen.capitalize() for uczen in uczniowie if uczen.lower()[-1] != "a"]


#skladnia

# nowa_lista = [wartosc_do_listy for tymczasowa_zmienna in obiekt_iterowalny if warunek]

print(lista_uczennic_druga_opcja)
print(lista_uczniow_meskich)

kolory = {"zielony", "niebieski", "czerwony"}

kolory_capitalize = {kolor.capitalize() for kolor in kolory}

print(kolory_capitalize)

przedmioty_zosi = ["niemiecki", "angielski", "historia", "polski", "matematyka", "fizyka", "chemia", "biologia"]

oceny_zosi = {}
lista_ocen_zosi = []
for przedmiot in przedmioty_zosi:
    oceny_zosi[przedmiot] = random.randint(1, 6)
    lista_ocen_zosi.append(random.randint(1, 6))

print(oceny_zosi)

# pozytywne_oceny_zosi = {przedmiot: ocena for przedmiot, ocena in oceny_zosi.items() if ocena > 1}
# pozytywne_oceny_zosi = [ocena for przedmiot, ocena in oceny_zosi.items() if ocena > 1]
#
# print(pozytywne_oceny_zosi)