from collections.abc import Iterable

# numbers = [1, 2, 3, 4]
#
# for number in numbers:
#     print(number)
#
#
#
# print(isinstance(numbers, Iterable))
#
# class Uczen:
#     def __init__(self, imie, nazwisko, wiek, oceny):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wiek = wiek
#         self.oceny = oceny
#
#     def __iter__(self):
#         return iter(self.oceny)
#
#
# uczen_1 = Uczen(imie="Michal", nazwisko="Zietkowski", wiek=12, oceny=[1, 4, 5, 4, 3, 2, 4])
#
# for wartosc in uczen_1:
#     print(wartosc)

def show_users(users):
    for user in users:
        return user


# def zaladuj_dane_z_pliku():
#     with open("first_example.txt") as plik:
#         temp_list = []
#         for line in plik.read():
#             temp_list.append(line)
#         return temp_list


users = ["user1", "user2", "user3", "user4", "user5", "user6"]
# for user in show_users(users):
#     print(user)
#
#
# for line in zaladuj_dane_z_pliku():
#     print(line)
#
# print(show_users(users))
# print(show_users(users))
# print(show_users(users))
# print(show_users(users))
# print(show_users(users))


def show_users_generator(users):
    for user in users:
        yield user

generator = show_users_generator(users)
# print(type(generator))
# print(generator)
# wartosc = show_users(users)
# print(wartosc)
# print(type(wartosc))
for user in generator:
    print(user)
print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


class Uczen:
    def __init__(self, imie, nazwisko, wiek, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.oceny = oceny

    def __iter__(self):
        return iter(self.oceny)


uczen_1 = Uczen(imie="Michal", nazwisko="Zietkowski", wiek=12, oceny=[1, 4, 5, 4, 3, 2, 4])

for wartosc in uczen_1:
    print(wartosc)
# print(next(uczen_1))