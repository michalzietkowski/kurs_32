"""
Jesteś szefem firmy technologicznej tworzącej system zarządzania dla międzynarodowego lotniska. System ten ma obsługiwać dane związane z lotami, liniami lotniczymi, pasażerami oraz stewardessami. Każdy lot może mieć przypisanych wielu pasażerów i jedną stewardessę, natomiast linie lotnicze mogą obsługiwać nieograniczoną liczbę lotów. Celem jest stworzenie programu, który pozwoli na efektywne zarządzanie i dostarczanie właściwych informacji na potrzeby logistyki i obsługi klienta lotniska.

**Program do zarządzania danymi lotów na międzynarodowym lotnisku**
Program powinien umożliwić:
1. Dodanie nowych danych do systemu:
   - Pasażera z przypisanym numerem lotu.
   - Stewardessy z przypisanym numerem lotu.
   - Linii lotniczej, która może obsługiwać wiele różnych lotów.
2. Przeglądanie i zarządzanie istniejącymi informacjami:
   - Pobranie listy pasażerów danego lotu.
   - Znalezienie przypisanej linii lotniczej dla wybranego pasażera.
   - Wyświetlenie listy lotów danej linii lotniczej.
   - Otrzymanie listy wszystkich pasażerów dla lotu, którego stewardessą jest wybrana osoba.
**Polecenia programu**
Po uruchomieniu, program powinien wyświetlić menu z następującymi komendami:
- dodaj - przechodzi do menu dodawania nowych danych.
- przeglądaj - przechodzi do menu przeglądania i zarządzania danymi.
- zakończ - kończy działanie programu.
**Menu dodawania danych (dodaj):**
Użytkownik może wybrać:
- pasażer - dodanie pasażera wymaga wprowadzenia imienia i nazwiska, numeru lotu.
- stewardessa - dodanie stewardessy wymaga wprowadzenia imienia i nazwiska, numeru lotu, do którego jest przypisana.
- linia_lotnicza - dodanie linii lotniczej wymaga wprowadzenia jej nazwy.
- zakończ_dodawanie - powrót do głównego menu.
**Menu przeglądania i zarządzania danymi (przeglądaj):**
Użytkownik może wybrać:
- lot - wprowadzenie numeru lotu wyświetla listę pasażerów tego lotu.
- pasażer - wprowadzenie imienia i nazwiska pasażera wyświetla nazwę linii lotniczej.
- linia_lotnicza - wprowadzenie nazwy linii lotniczej wyświetla listę lotów obsługiwanych przez linię.
- stewardessa - wprowadzenie imienia i nazwiska stewardessy wyświetla listę pasażerów jej lotu.
- zakończ_przeglądanie - powrót do głównego menu.
**Zakończenie pracy programu**
Polecenie zakończ powoduje zamknięcie aplikacji.
"""


class Pasazer:
    def __init__(self, imie_pasazera, nazwisko_pasazera, numer_lotu_pasazera):
        self.imie = imie_pasazera
        self.nazwisko = nazwisko_pasazera
        self.numer_lotu = numer_lotu_pasazera

    def __repr__(self):
        return f"Pasażer {self.imie} {self.nazwisko} z lotu {self.numer_lotu}"

class Stewardessa:
    def __init__(self, imie_stewardessy, nazwisko_stewardessy, numer_lotu):
        self.imie = imie_stewardessy
        self.nazwisko = nazwisko_stewardessy
        self.numer_lotu = numer_lotu

    def __repr__(self):
        return f"Stewardessa {self.imie} {self.nazwisko} z lotu {self.numer_lotu}"

class LiniaLotnicza:
    def __init__(self, nazwa, lista_lotow):
        self.nazwa = nazwa
        self.lista_lotow = lista_lotow

    def __repr__(self):
        return f"Linia lotnicza {self.nazwa} z listą lotów {self.lista_lotow}"



lotnisko = {
    "pasazerowie": [Pasazer("Piotr", "Kubiak", "LOT123"), Pasazer("Michał", "Ziętkowski", "LOT123"), Pasazer("Anna", "Nowak", "RY123")],
    "stewardessy": [Stewardessa(imie_stewardessy="Monika", nazwisko_stewardessy="Adamiec", numer_lotu="LOT123"),
                    Stewardessa(imie_stewardessy="Jacek", nazwisko_stewardessy="Dębski", numer_lotu="RY123"),
                    ],
    "linie_lotnicze": [LiniaLotnicza(nazwa="LOT", lista_lotow=["LOT123", "LOT333"]),
                       LiniaLotnicza("Ryanair", ["RY123"])]
}

def wyszukaj_pasazerow_lotu_po_jego_numerze(numer_lotu):
    lista_pasazerow_lotu = []
    for pasazer in lotnisko.get("pasazerowie"):
        if pasazer.numer_lotu == numer_lotu:
            lista_pasazerow_lotu.append(pasazer)
    return lista_pasazerow_lotu

def wyszukaj_numer_lotu_pasazera(imie, nazwisko):
    for pasazer in lotnisko.get("pasazerowie"):
        if pasazer.imie == imie and pasazer.nazwisko == nazwisko:
            return pasazer.numer_lotu

def wyszukaj_nazwe_linii_po_numerze_lotu(numer_lotu):
    for linia_lotnicza in lotnisko.get("linie_lotnicze"):
        if numer_lotu in linia_lotnicza.lista_lotow:
            return linia_lotnicza.nazwa

def wyszukaj_liste_lotow_linii_lotniczej(nazwa_linii):
    for linia in lotnisko.get("linie_lotnicze"):
        if linia.nazwa == nazwa_linii:
            return linia.lista_lotow

def wyszukaj_lot_stewardessy_po_jej_danych(imie, nazwisko):
    for stewardessa in lotnisko.get("stewardessy"):
        if stewardessa.imie == imie and stewardessa.nazwisko == nazwisko:
            return stewardessa.numer_lotu


while True:
    wybor_uzytkownika = input("Podaj co chcesz zrobić:\n"
                              "1. Utwórz\n"
                              "2. Zarządzaj\n"
                              "3. Zakończ\n")
    if wybor_uzytkownika in ("1", "Utwórz"):
        opcja_do_dodania = input("Podaj co chcesz dodać?\n"
                                 "1. Pasażer\n"
                                 "2. Stewardessa\n"
                                 "3. Linia lotnicza\n")
        if opcja_do_dodania == "1":
            imie = input("Podaj imię pasażera: ")
            nazwisko = input("Podaj nazwisko pasażera: ")
            numer_lotu = input("Podaj numer lotu pasażera: ")
            lotnisko["pasazerowie"].append(Pasazer(imie, nazwisko, numer_lotu))
    elif wybor_uzytkownika in ("2", "Zarządzaj"):
        opcja_do_zarzadzania = input("Podaj co chcesz zrobić?\n"
                                     "1. Sprawdź listę pasażerów lotu\n"
                                     "2. Sprawdź jaką linią lotniczą leci pasażer\n"
                                     "3. Sprawdź loty linii lotniczej\n"
                                     "4. Sprawdź pasażerów stewardessy")
        if opcja_do_zarzadzania == "1":
            numer_lotu = input("Podaj numer lotu: ")
            pasazerowie = wyszukaj_pasazerow_lotu_po_jego_numerze(numer_lotu)
            print(pasazerowie)
        elif opcja_do_zarzadzania == "2":
            imie_pasazera = input("Podaj imie pasazera: ")
            nazwisko_pasazera = input("Podaj nazwisko pasazera: ")
            numer_lotu = wyszukaj_numer_lotu_pasazera(imie_pasazera, nazwisko_pasazera)
            if numer_lotu:
                nazwa_linii = wyszukaj_nazwe_linii_po_numerze_lotu(numer_lotu)
                print(nazwa_linii)
            else:
                print("Nie ma takiego pasażera")
        elif opcja_do_zarzadzania == "3":
            nazwa_linii = input("Podaj nazwę linii lotniczej: ")
            lista_lotow = wyszukaj_liste_lotow_linii_lotniczej(nazwa_linii)
            print(lista_lotow)
        elif opcja_do_zarzadzania == "4":
            imie_stewardessy = input("Podaj imię stewardessy: ")
            nazwisko_stewardessy = input("Podaj nazwisko stewardessy: ")
            numer_lotu = wyszukaj_lot_stewardessy_po_jej_danych(imie_stewardessy, nazwisko_stewardessy)
            pasazerowie = wyszukaj_pasazerow_lotu_po_jego_numerze(numer_lotu)
            print(pasazerowie)
    elif wybor_uzytkownika in ("3", "Zakończ"):
        break
    else:
        print("Niepoprawna komenda!")
