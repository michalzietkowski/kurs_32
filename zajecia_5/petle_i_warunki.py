# print("witaj swiecie")
#
# imie = "Michał"
# print(imie)
# print(imie)
#
# produkt = input("Podaj mi swój produkt do kupienia: ").lower()
# if produkt == "piwo" or produkt == "wodka" or produkt == "papierosy":
#     wiek = int(input("Podaj mi swój wiek: "))
#     if wiek >= 18:
#         print(f"Brawo kupiłeś/aś {produkt}")
#     else:
#         print("Nie możesz kupić tego produktu!")
# else:
#     print(f"Brawo kupiłeś/aś {produkt}")
# if warunek do spełnienia:
#   instrukcje dla uzytkownika gdy warunek jest spelniony
# else:
#   instrukcje gdy warunek nie jest spelniony
# print("Papierosy" == "papierosy")

# zawod = input("Podaj mi swój zawód: ")
# pensja = float(input("Podaj mi swoją pensję: "))
#
# if zawod == "programista":
#     emerytura = pensja * 0.10
# elif zawod == "analityk":
#     emerytura = pensja * 0.60
# elif zawod == "pielegniarka":
#     emerytura = pensja * 0.30
# elif zawod == "zolnierz":
#     emerytura = pensja * 0.80
# else:
#     print("Niestety nie mamy twojego zawodu w naszej bazie")
#     emerytura = None
#
# print(f"Twoja emerytura wynosi: {emerytura}")

# ilosc_towaru = int(input("Podaj ilosc przedmiotow, które chcesz kupić: "))
# wartosc_zamowienia = 0
# przedmiot_1 = float(input("Podaj mi wartość netto 1 przedmiotu: "))
# cena_przedmiotu_1 = przedmiot_1 * 1.23
# wartosc_zamowienia += cena_przedmiotu_1
# # wartosc_zamowienia = wartosc_zamowienia + cena_przedmiotu_1
# przedmiot_2 = float(input("Podaj mi wartość netto 2 przedmiotu: "))
# cena_przedmiotu_2 = przedmiot_2 * 1.23
# wartosc_zamowienia += cena_przedmiotu_2
# for towar in range(ilosc_towaru):
#     print(towar)
# przedmiot = float(input("Podaj mi wartość netto przedmiotu: "))
# wartosc_zamowienia += przedmiot * 1.23

# for zmienna_tymczasowa in struktura iterowalna - range, listy, krotki, słowniki:
# kod, który będzie się powtarzać

# print(round(wartosc_zamowienia ,2))

# wiek = int(input("Podaj mi swój wiek:"))

# if wiek < 18:
#     print(f"Nie masz jescze 18 lat. Twój wiek to: {wiek}")
#     wiek += 1
# else:
#     print("Jesteś już dorosły")
# while wiek < 18:
#     print(f"Nie masz jeszcze 18 lat. Twój wiek to: {wiek}")
#     wiek += 1
# print("Jesteś już dorosły")

# while True:
#     print("Zabijam Ci kompa")

# while warunek, który musi być spełniony:
#   kod, który jest wykonywany w momencie gdy warunek jest spełnione
# for item in range(6):
#     pass

# wiek = int(input("Podaj mi swój wiek: "))
# # while True:
# #     print(f"Nie masz jeszcze 18 lat. Twój wiek to: {wiek}")
# #     if wiek >= 18:
# #         break
# #     wiek += 1
# print("Jesteś już dorosły")
# while True:
#     wiek += 1
#     print(f"Nie masz jeszcze 21 lat. Twój wiek to {wiek}")
#     if wiek >= 21:
#         break
#     if wiek >= 16:
#         print("Możesz prowadzić samochód")
#         continue
#     print("Nie możesz jeszcze prowadzić samochodu")
import sys

print(sys.argv)
print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])
ilosc_paczek = int(sys.argv[1])
for paczka in range(ilosc_paczek):
    print(paczka)
