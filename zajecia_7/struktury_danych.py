#### listy

a = "Michal"
b = "Adam"
c = "Jacek"
d = "Tomek"

#CRUD

uczniowie = ["Michał", "Adam", "Jacek", "Tomek"]
randomowa_lista = ["michal", True, 1.0, 123, []]
# uczniowie_3 = ["Michał", "Adam", "Jacek", "Tomek", "Ada", "Jagoda", "Maria", "Jowita"]
# uczniowie_2 = list()
# # print(uczniowie)
# print(uczniowie_2)
# print(type(uczniowie))
# print(type(uczniowie_2))
# print(uczniowie[0])
# print(uczniowie[1])
# print(uczniowie[3])
# print(uczniowie[-1])
# print(uczniowie[-1])
# print(uczniowie[0:2])
# print(uczniowie_3[0:8:3])
# for index, uczen in enumerate(uczniowie):
#     if index == 2:
#         uczniowie[index] = "Zdzisław"
#     print(index)
#     print(uczen)
# print(uczniowie)
# print(len(uczniowie))
# numer = 3
# if numer <= len(uczniowie) -1:
#     uczniowie[numer] = "Wojtek"
# print(uczniowie)
# uczniowie[0] = "Tomek" # operacja zmiany wartości
# uczniowie[4] = "Paweł" # to jest zła operacja dodania do listy
uczniowie.append("Paweł")
uczniowie.insert(0, "Ania")
uczniowie.insert(100, "Ania")
print(uczniowie)

del(uczniowie[0]) # działamy na indexach
uczniowie.remove("Michał") # działamy na wartościach
print(uczniowie)

# in_1 in_2 output
# 0   0       0
# 1   0       0
# 0   1       0
# 1   1       1
#
# in_1 in_2 output
# 0   0       0
# 1   0       1
# 0   1       1
# 1   1       1


########### KROTKI (Tuple)

# krotka_plci = ("mezczyzna", "kobieta")
#
# pusta_krotka = tuple()
#
# krotka_3_sposob = "mezczyzna", "kobieta"
#
# imie = "Michal"
#
# print(krotka_plci[0])
# for wartosc in krotka_plci:
#     print(wartosc)
# # krotka_plci[0] = "transgender"
# dane = input("Podaj mi swoje wartosci")
# krotka = tuple(dane.split())
# print(krotka)
# print(type(imie))

###### ZBIORY (SET)
#
# kolory = {"niebieski", "czerwony", "zielony"}
#
# kolory.add("biały")
# print(kolory)
# kolory.add("niebieski")
# print(kolory)
# for kolor in kolory:
#     print(kolor)
#
# kolory.remove("niebieski")
# print(kolory)


############ SŁOWNIKI

uczen = {"imie": "Michał",
         "nazwisko": "Ziętkowski",
         "klasa": "6A",
         "wiek": 13,
         "wzrost": "90"
         }

print(uczen)
print(uczen["imie"])
print(uczen["nazwisko"])
# print(uczen["waga"])
print(uczen.get("waga"))

uczen["imie"] = "Wojciech"
uczen["waga"] = 100
print(uczen)

# for dane in uczen: zly przyklad
#     print(dane)

for klucz in uczen.keys():
    print(klucz)

for wartosc in uczen.values():
    print(wartosc)

for a, b in uczen.items():
    print(f"{a}: {b}")
