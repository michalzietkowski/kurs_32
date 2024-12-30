from abc import ABC, abstractmethod
#
#
# class Zwierze(ABC):
#
#     @abstractmethod
#     def odezwij_sie(self):
#         pass
#
#     @abstractmethod
#     def zyj(self):
#         pass
#
#
# class Lew(Zwierze):
#     def odezwij_sie(self):
#         print("rawrrr")
#
#
# class Ryba(Zwierze):
#     def odezwij_sie(self):
#         print("gul gul gul")
#
#     def plywaj(self):
#         print("plywam")
#
# class Pies(Zwierze):
#     pass
#
#
# lew = Lew()
# lew.odezwij_sie()
# ryba = Ryba()
# ryba.odezwij_sie()
# pies = Pies()


class Produkt(ABC):

    def przywitaj_sie(self):
        print("czesc z produktu")

    @abstractmethod
    def podaj_mi_swoja_cene(self):
        pass

    @abstractmethod
    def podaj_mi_swoja_date_waznosci(self):
        pass


class ProduktSwiateczny(Produkt):

    def podaj_mi_swoja_cene(self):
        pass

    def podaj_mi_swoja_date_waznosci(self):
        pass


class ProduktPrzeceniony(Produkt):

    def podaj_mi_swoja_cene(self):
        pass

    def podaj_mi_swoja_date_waznosci(self):
        pass



class NowyProdukt:
    def przywitaj_sie(self):
        print("czesc z produktu")

    def podaj_mi_swoja_cene(self):
        pass

    def podaj_mi_swoja_date_waznosci(self):
        pass
