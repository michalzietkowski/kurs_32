def funkcja_kwadratowa(numer):
    return numer ** 2

def dodaj(a, b):
    return a + b

print(funkcja_kwadratowa(5))
print(funkcja_kwadratowa(10))
print(funkcja_kwadratowa(15))

funkcja_kwadratowa_lambda = lambda numer: numer **2
# nazwa funkcji = lamba <argumenty funkcji>: <wartosc zwracana z funkcji>

funkcja_dodaj_lambda = lambda a, b: a + b
print(funkcja_kwadratowa_lambda(5))
print(funkcja_kwadratowa_lambda(10))
print(funkcja_kwadratowa_lambda(15))
print(funkcja_dodaj_lambda(1, 2))
print(funkcja_dodaj_lambda(5, 2))

def przetworz_zbior_danych():
    #operacje przetwarzajace
    dane = []
