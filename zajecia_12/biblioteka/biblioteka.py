from file_handler import FileHandler


file_handler = FileHandler(data_file="dane_ksiegarni.json", history_file="historia.json")
data = file_handler.load_data_from_data_file()
historia = file_handler.load_data_from_history_file()

saldo_ksiegarni = data.get("saldo")

ksiegozbior = data.get("ksiegozbior")

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
        kwota = float(input("Podaj kwotę, o jaką chcesz zmienić saldo: "))
        if saldo_ksiegarni + kwota < 0:
            print("Niestety nie mamy takich środków na koncie!")
            historia.append("Próba odjęcia zbyt dużej kwoty")
        else:
            saldo_ksiegarni += kwota
            historia.append(f"Zmiana salda o {kwota}")

    elif wybor_uzytkownika == "2":
        autor = input("Podaj autora książki, którą chcesz wypożyczyć: ")
        tytul = input("Podaj tytuł książki, którą chcesz wypożyczyć: ")
        rok_wydania = int(input("Podaj rok wydania książki, którą chcesz wypożyczyć: "))
        znaleziono_ksiazke = False
        for ksiazka in ksiegozbior:
            if (
                ksiazka.get("autor") == autor
                and ksiazka.get("tytul") == tytul
                and ksiazka.get("rok_wydania") == rok_wydania
            ):
                if ksiazka.get("ilosc_dostepnych_ksiazek") >= 1:
                    ksiazka["ilosc_dostepnych_ksiazek"] -= 1
                    saldo_ksiegarni += ksiazka.get("cena_wypozyczenia")
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

    elif wybor_uzytkownika == "3":
        autor = input("Podaj autora książki, którą chcesz zakupić: ")
        tytul = input("Podaj tytuł książki, którą chcesz zakupić: ")
        rok_wydania = int(input("Podaj rok wydania książki, którą chcesz zakupić: "))
        ilosc_ksiazek = int(input("Podaj ilość książek, którą chcesz kupić: "))
        cena_jednostkowa_ksiazki = float(input("Podaj cene zakupu 1 szt: "))
        cena_wypozyczenia = float(input("Podaj cene wypozyczenia 1 szt: "))
        # sprawdz czy taka książka nie istnieje
        if ilosc_ksiazek * cena_jednostkowa_ksiazki > saldo_ksiegarni:
            print("Nie stać nas na te książki")
            # dodajemy do historii
            continue
        ksiegozbior.append(
            {
                "tytul": tytul,
                "autor": autor,
                "rok_wydania": rok_wydania,
                "ilosc_dostepnych_ksiazek": ilosc_ksiazek,
                "ilosc_ksiazek": ilosc_ksiazek,
                "cena_wypozyczenia": cena_wypozyczenia,
            }
        )
        saldo_ksiegarni -= ilosc_ksiazek * cena_jednostkowa_ksiazki
        # dodajemy do historii

    elif wybor_uzytkownika == "4":
        print(saldo_ksiegarni)

    elif wybor_uzytkownika == "5":
        for ksiazka in ksiegozbior:
            print(ksiazka)

    elif wybor_uzytkownika == "7":
        od = 0
        do = 10
        # dlugosc listy = len(histora)
        print(historia[od:do])
    elif wybor_uzytkownika == "8":
        break

    else:
        print("Nie można dodać takiej komendy")

file_handler.save_data_to_data_file(balance=saldo_ksiegarni, book_collection=ksiegozbior)
file_handler.save_data_history_file(history=historia)
