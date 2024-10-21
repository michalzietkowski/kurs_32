imie = "Michal"
print(id(imie))
print(hash(imie))
imie += " Ziętkowski"
# print(id(imie))
wiek = 20
# print(id(wiek))
print(hash(wiek))
wiek = 24
# print(id(wiek))

# slownik = {
#     "imie": "Michal",
#     "imie": "Andrzej"
# }
# print(slownik.get("imie"))
#
# lista_imion = ["Michal", "Jacek"]
# print(id(lista_imion))
# lista_imion.append("Mariusz")
# print(id(lista_imion))
############## lista nie moze byc kluczem w Pythonie!!!
# slownik_2 = {
#     ["Michal", "Jacek"]: "1234",
#     ["Jolanta", "Barbara"]: True
# }
#
# slownik_3 = {
#     ["Michal", "Jacek"]: "1234",
#     ["Michal", "Jacek"]: True
# }

# print(hash(["Michal"]))

print(hash(("mezczyzna",)))

slownik_30 = {
    ("mezczyzna",): "123"
}
print(slownik_30)

lista = ["123", True, 23434]

slownik = {
    "klucz1": [],
    "klucz2": {},
    "klucz3": {
        "123": []
    },
}