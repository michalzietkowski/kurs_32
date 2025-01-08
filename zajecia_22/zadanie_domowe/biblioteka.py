from manager import manager



@manager.assign("zmiana_salda")
def zmiana_salda(manager):
    kwota = float(input("Podaj kwotę, o jaką chcesz zmienić saldo: "))
    if manager.saldo_ksiegarni + kwota < 0:
        print("Niestety nie mamy takich środków na koncie!")
        manager.historia.append("Próba odjęcia zbyt dużej kwoty")
    else:
        manager.saldo_ksiegarni += kwota
        manager.historia.append(f"Zmiana salda o {kwota}")


@manager.assign("wypozyczenie_ksiazki")
def wypozyczenie_ksiazki(manager):
    autor = input("Podaj autora książki, którą chcesz wypożyczyć: ")
    tytul = input("Podaj tytuł książki, którą chcesz wypożyczyć: ")
    rok_wydania = int(input("Podaj rok wydania książki, którą chcesz wypożyczyć: "))
    znaleziono_ksiazke = False
    for ksiazka in manager.ksiegozbior:
        if (
                ksiazka.get("autor") == autor
                and ksiazka.get("tytul") == tytul
                and ksiazka.get("rok_wydania") == rok_wydania
        ):
            if ksiazka.get("ilosc_dostepnych_ksiazek") >= 1:
                ksiazka["ilosc_dostepnych_ksiazek"] -= 1
                manager.saldo_ksiegarni += ksiazka.get("cena_wypozyczenia")
                print(f"wypozyczyles ksiazke {tytul}")
            else:
                print(
                    "Niestety, w tym momencie ta książka jest całkowicie wypożyczona! Wróć w innym terminie."
                )
                # dodanie do historii
            znaleziono_ksiazke = True
            break
    if not znaleziono_ksiazke:
        print("Nie znaleziono książki\n")
        # dodanie info do historii


@manager.assign("kup_ksiazke")
def kup_ksiazke(manager):
    autor = input("Podaj autora książki, którą chcesz zakupić: ")
    tytul = input("Podaj tytuł książki, którą chcesz zakupić: ")
    rok_wydania = int(input("Podaj rok wydania książki, którą chcesz zakupić: "))
    ilosc_ksiazek = int(input("Podaj ilość książek, którą chcesz kupić: "))
    cena_jednostkowa_ksiazki = float(input("Podaj cene zakupu 1 szt: "))
    cena_wypozyczenia = float(input("Podaj cene wypozyczenia 1 szt: "))
    # sprawdz czy taka książka nie istnieje
    if ilosc_ksiazek * cena_jednostkowa_ksiazki > manager.saldo_ksiegarni:
        print("Nie stać nas na te książki")
        # dodajemy do historii
    manager.ksiegozbior.append(
        {
            "tytul": tytul,
            "autor": autor,
            "rok_wydania": rok_wydania,
            "ilosc_dostepnych_ksiazek": ilosc_ksiazek,
            "ilosc_ksiazek": ilosc_ksiazek,
            "cena_wypozyczenia": cena_wypozyczenia,
        }
    )
    manager.saldo_ksiegarni -= ilosc_ksiazek * cena_jednostkowa_ksiazki
    # dodajemy do historii



while True:
    print("Witaj w naszym programie do zarządzania księgarnią.")
    wybor_uzytkownika = input(
        "Podaj co chcesz zrobić:\n"
        "1. Zmiana salda\n"
        "2. Wypożyczenie książki\n"
        "3. Zakup książki\n"
        "4. Sprawdzenie salda\n"
        "5. Zestawienie księgarni\n"
        "6. Szczegóły książki\n"
        "7. Historia działań\n"
        "8. Zakończenie programu\n"
    )

    if wybor_uzytkownika in ("1", "Zmiana salda"):
        manager.execute("zmiana_salda")

    elif wybor_uzytkownika == "2":
        manager.execute("wypozyczenie_ksiazki")
    elif wybor_uzytkownika == "3":
       manager.execute("kup_ksiazke")

    elif wybor_uzytkownika == "4":
        print(manager.saldo_ksiegarni)

    elif wybor_uzytkownika == "5":
        for ksiazka in manager.ksiegozbior:
            print(ksiazka)

    elif wybor_uzytkownika == "7":
        od = 0
        do = 10
        # dlugosc listy = len(histora)
        print(manager.historia[od:do])
    elif wybor_uzytkownika == "8":
        break
    else:
        print("Nie można dodać takiej komendy")

manager.file_handler.save_data_to_data_file(balance=manager.saldo_ksiegarni, book_collection=manager.ksiegozbior)
manager.file_handler.save_data_history_file(history=manager.historia)
