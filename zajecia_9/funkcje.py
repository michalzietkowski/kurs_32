print("Witaj w programie do obliczania pola prostokąta!")
#
# wymiar_1 = int(input("Podaj proszę pierwszy bok prostokąta: "))
# wymiar_2 = int(input("Podaj proszę drugi bok prostokąta: "))
# print(f"Wymiar twojego prostokąta wynosi: {wymiar_2 * wymiar_1}")
#
# while True:
#     wymiar_1 = int(input("Podaj proszę pierwszy bok prostokąta: "))
#     wymiar_2 = int(input("Podaj proszę drugi bok prostokąta: "))
#     print(f"Wymiar twojego prostokąta wynosi: {wymiar_2 * wymiar_1}")
#
# def obliczanie_pola_prostokata():
#     wymiar_1 = int(input("Podaj proszę pierwszy bok prostokąta: "))
#     wymiar_2 = int(input("Podaj proszę drugi bok prostokąta: "))
#     print(f"Wymiar twojego prostokąta wynosi: {wymiar_2 * wymiar_1}")
#

pole = 0


def obliczanie_pola_prostokata_v2(wymiar_1, wymiar_2):
    # print(f"Wymiar twojego prostokąta wynosi: {wymiar_2 * wymiar_1}")
    pole = wymiar_2 * wymiar_1
    pass


def obliczanie_pola_prostokata_v3(wymiar_1, wymiar_2):
    return wymiar_1 * wymiar_2


for numer in range(10):
    print(numer)

# obliczanie_pola_prostokata()
# obliczanie_pola_prostokata_v2(10, 10)
# obliczanie_pola_prostokata_v2(12, 10)
# a = int(input("Podaj proszę pierwszy bok prostokąta: "))
# b = int(input("Podaj proszę drugi bok prostokąta: "))
# obliczanie_pola_prostokata_v2(a, b)
# wynik_obliczenia = obliczanie_pola_prostokata_v3(10, 10)
# wynik_obliczenia_2 = obliczanie_pola_prostokata_v2(10, 10)
# print(wynik_obliczenia)
# print(wynik_obliczenia_2)
# print(pole)


lista_uczniow = [
    {"imie": "Michał", "nazwisko": "Zietkowski", "klasa": "6a"},
    {"imie": "Adam", "nazwisko": "Małysz", "klasa": "4c"},
]

# def znajdz_ucznia_w_liscie(imie_ucznia, nazwisko_ucznia, klasa_ucznia="0"):
#     print(klasa_ucznia)
#     znaleziono_ucznia = False
#     for uczen in lista_uczniow:
#         if uczen.get("imie") == imie_ucznia and uczen.get("nazwisko") == nazwisko_ucznia and uczen.get("klasa") == klasa_ucznia:
#             print("Znaleźliśmy ucznia!!")
#             znaleziono_ucznia = True
#     if not znaleziono_ucznia:
#         print("Nie znaleźliśmy ucznia!")


def znajdz_ucznia_w_liscie(imie_ucznia, nazwisko_ucznia, klasa_ucznia="0"):
    print(klasa_ucznia)
    for uczen in lista_uczniow:
        if (
            uczen.get("imie") == imie_ucznia
            and uczen.get("nazwisko") == nazwisko_ucznia
            and uczen.get("klasa") == klasa_ucznia
        ):
            print("Znaleźliśmy ucznia!!")
            return uczen
    print("Nie znaleźliśmy ucznia!")


#
znajdz_ucznia_w_liscie("Michał", "Zietkowski")
# znajdz_ucznia_w_liscie("Zietkowski", "Michał")
uczen = znajdz_ucznia_w_liscie(
    nazwisko_ucznia="Zietkowski", imie_ucznia="Michał", klasa_ucznia="6a"
)
print(uczen)
