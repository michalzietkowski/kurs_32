class KontoBankowe:
    def __init__(self, haslo, saldo):
        self._haslo = haslo
        self.__saldo = saldo

    def wyplata(self, kwota_do_wyplaty):
        print("weryfikacja kto chce zmienic saldo")
        if self.__saldo >= kwota_do_wyplaty:
            self.__saldo -= kwota_do_wyplaty
        else:
            print("nie mozemy zmienic salda")




moje_konto = KontoBankowe("123", 1000)
moje_konto.wyplata(900)
moje_konto.__saldo = 200
print(moje_konto.__saldo)
