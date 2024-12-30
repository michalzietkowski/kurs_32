from abc import abstractmethod, ABC


class Zwierze(ABC):

    @abstractmethod
    def daj_glos(self):
        pass


class Kot(Zwierze):

    def daj_glos(self):
        print("miauu")

class Pies(Zwierze):

    def daj_glos(self):
        print("hau hau")

def wydaj_dzwiek(zwierze):
    return zwierze.daj_glos()


wydaj_dzwiek(Pies())
wydaj_dzwiek(Kot())
