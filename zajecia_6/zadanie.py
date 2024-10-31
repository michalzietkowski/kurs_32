# Napisz program do organizacji przetrzymywania dokumentów w szafkach. Po uruchomieniu, aplikacja pyta, ile chcesz dodać dokumentów,
# a następnie wymaga podania liczby stron dla każdego z nich.
# Na koniec działania program powinien wyświetlić w podsumowaniu:
# 1. Liczbę dokumentów dodanych.
# 2. Łączną liczbę stron.
# 3. Suma niewykorzystanych miejsc w szafkach.
# 4. Która szafka miała najwięcej niewykorzystanych miejsc, jaki to był wynik.
# Restrykcje:
# • Liczba stron dokumentów musi być z przedziału od 1 do 30 stron.
# • Każda szafka może maksymalnie pomieścić 100 stron.
# • W przypadku, jeżeli dodawany dokument przekroczy miejsce w szafce, ma zostać umieszczony w nowej szafce, a obecna zostaje zamknięta.
# • W przypadku podania liczby stron mniejszej od 1 lub większej od 30, dodawanie dokumentów zostaje zakończone i wszystkie szafki są zamknięte. Wyświetlane jest podsumowanie.
# 1. Liczba dokumentow
# 2. Podac ilosc stron kazdego dokumentu
# pojemnosc szafki = 100

liczba_dokumentow = int(input("Podaj ilość dokumentów do dodania: "))

liczba_stron = 0
liczba_szafek = 1
pojemnosc_biezacej_szafki = 0
maksymalna_niewykorzystana_pojemnosc = 0
numer_szafki_z_maksymalna_niewykorzystana_pojemnoscia = 1

for dokument in range(liczba_dokumentow):
    # liczba_stron = 0
    liczba_stron_dokumentu = int(input("Podaj ilość stron dokuemntu: "))
    if liczba_stron_dokumentu > 30 or liczba_stron_dokumentu < 1:
        liczba_dokumentow = dokument
        break

    liczba_stron += liczba_stron_dokumentu

    if liczba_stron_dokumentu + pojemnosc_biezacej_szafki > 100:

        if 100 - pojemnosc_biezacej_szafki > maksymalna_niewykorzystana_pojemnosc:
            maksymalna_niewykorzystana_pojemnosc = 100 - pojemnosc_biezacej_szafki
            numer_szafki_z_maksymalna_niewykorzystana_pojemnoscia = liczba_szafek
        pojemnosc_biezacej_szafki = liczba_stron_dokumentu
        liczba_szafek += 1
    else:
        pojemnosc_biezacej_szafki += liczba_stron_dokumentu

if 100 - pojemnosc_biezacej_szafki > maksymalna_niewykorzystana_pojemnosc:
    maksymalna_niewykorzystana_pojemnosc = 100 - pojemnosc_biezacej_szafki
    numer_szafki_z_maksymalna_niewykorzystana_pojemnoscia = liczba_szafek

print(f"Liczba dokumentów, które dodałeś to {liczba_dokumentow}")
print(f"Łączna liczba stron dokumentów, które dodałeś to {liczba_stron}")
print(f"Suma niewykorzystanego miejsca w szafkach to: {liczba_szafek*100-liczba_stron}")
print(
    f"Najwiecej niewykorzystanego miejsca jest w szafce {numer_szafki_z_maksymalna_niewykorzystana_pojemnoscia}"
    f" i wynosi {maksymalna_niewykorzystana_pojemnosc}"
)
# print(liczba_stron)
# print(pojemnosc_biezacej_szafki)
