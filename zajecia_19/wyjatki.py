# try:
#     print("Otwieram polaczenie z baza danych")
#     wiek = int(input("Podaj mi swoj wiek: "))
#     print(wiek)
# except ValueError:
#     print("Nie jestes wartoscia numeryczna")
# finally:
#     print("Zamykam polaczenie z baza danych")

lista_gosci = ["Adam", "Ewa", "Marta"]


try:
    numer_goscia = int(input("Podaj numer goscia na liscie: "))
    print(f"Twoj gosc to {lista_gosci[numer_goscia]}")
    wiek_goscia = int(input("Podaj wiek goscia: "))
# except ValueError:
#     print("Niestety to nie jest wartosc numeryczna")
# except IndexError:
#     print("Niestety nie mamy takiego goscia na liscie")
except (ValueError, IndexError):
    print("Cos poszlo nie tak!")