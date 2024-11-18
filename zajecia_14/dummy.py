# macierz = [[0, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]]
#
# print(macierz[0][0])
#
# macierz[0][1] = 10
#
# print(macierz)



lista_imion = ["Michal", "Adam", "Zosia", "Gosia"]

# for imie in lista_imion:
#     print(imie)

for pozycja, imie in enumerate(lista_imion):
    if pozycja == 1:
        lista_imion[pozycja] = "Tomek"
    print(imie)

print(lista_imion)

