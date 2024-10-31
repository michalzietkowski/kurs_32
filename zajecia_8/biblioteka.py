"""
Stwórz system zarządzania księgozbiorem bibliotecznym, który pozwoli na monitorowanie przepływu książek oraz śledzenie budżetu biblioteki.
Po uruchomieniu systemu użytkownik otrzymuje listę komend do wyboru:
- doładowanie
- wypożycz
- zakup
- bieżący_stan
- zestawienie
- szczegóły_książki
- dziennik
- zakończ
Funkcje po wywołaniu danych komend są następujące:
1. doładowanie - Umożliwia dodanie środków do budżetu biblioteki lub ich odjęcie.
2. wypożycz - Rejestruje wypożyczenie książki przez czytelnika. System żąda podania imienia, nazwiska oraz daty ksiązki. Koszt wypożyczenia jest dodawany do budżetu.
3. zakup - Rejestruje zakup nowych książek dla biblioteki. System pyta o tytuł książki, koszt zakupu i liczbę egzemplarzy. Zakupione książki są dodawane do zbioru, a środki są odprowadzane z budżetu, który nie może być negatywny po transakcji.
4. bieżący_stan - Wyświetla aktualny stan środków finansowych.
5. zestawienie - Podsumowuje cały księgozbiór biblioteki wraz z cenami zakupu i ich ilością.
6. szczegóły_książki - Wyświetla dostępność i dane dotyczące pojedynczej książki po wpisaniu numeru ISBN.
7. dziennik - Przegląd historii transakcji. Podając wartości "od" i "do", system wyświetla zapisane działania w podanym zakresie. W przypadku pustych pól lub wartości spoza zakresu, użytkownik jest informowany o błędzie i wyświetlana jest liczba wszystkich zarejestrowanych transakcji.
8. zakończ - Kończy działanie programu.
**Inne wymagania:**
- System działa do momentu wybrania komendy zakończ.
- Operacje doładowanie, wypożycz oraz zakup są zapisywane dla późniejszej referencji przy użyciu komendy dziennik.
- Po każdej komendzie system wyświetla ponownie listę dostępnych opcji i prosi o wybór kolejnej.
- Ochrona przed błędami użytkownika, takimi jak wpisywanie błędnych danych czy żądanie zakupu na wartości ujemne. Powinno być również sprawdzanie poprawności typów danych wprowadzanych przez użytkownika.
"""

saldo_ksiegarni = 10000.0
historia = [
    "dodano 1000 zł do konta",
    "odjęto 1000 zł od konta",
    "wypożyczono książkę Wiedźmin",
]
ksiegozbior = [
    {
        "tytul": "Wiedzmin",
        "autor": "Andrzej Sapkowski",
        "rok_wydania": 1999,
        "ilosc_dostepnych_ksiazek": 5,
        "ilosc_ksiazek": 5,
        "cena_wypozyczenia": 10.0,
    },
    {
        "tytul": "Clean code",
        "autor": "Uncle Bob",
        "rok_wydania": 1990,
        "ilosc_dostepnych_ksiazek": 5,
        "ilosc_ksiazek": 5,
        "cena_wypozyczenia": 15.0,
    },
    {
        "tytul": "Clean Architecture",
        "autor": "Uncle Bob",
        "rok_wydania": 1990,
        "ilosc_dostepnych_ksiazek": 5,
        "ilosc_ksiazek": 5,
        "cena_wypozyczenia": 15.0,
    },
]

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
