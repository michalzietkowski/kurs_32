import json

# with open("nic_dwa_razy.txt") as plik:
#     print(plik.read())
#     plik.write("dodatkowa linijka")
#
# # mode w - nadpisuje cały plik, bez możliwości odczytu
# with open("nic_dwa_razy_2.txt", mode="w") as plik:
#     # print(plik.read())
#     plik.write("dodatkowa linijka")

# # mode a - dodaje nowe rzeczy do pliku zachowując poprzednie, bez możliwości odczytu
# with open("nic_dwa_razy_2.txt", mode="a") as plik:
#     # print(plik.read())
#     plik.writelines(["\nnowa linijka\n", "1234324"])
#
#

# with open("nic_dwa_razy_2.txt") as plik:
#     # print(plik.read())
#     # plik.writelines(["\nnowa linijka\n", "1234324"])
#     tresc_pliku =  plik.read()
#     print(tresc_pliku)

# # mode r+ odczytuje oraz dopisuje dane do naszego pliku
# with open("nic_dwa_razy.txt", mode="r+") as plik:
#     tresc = plik.read()
#     print(tresc)
#     plik.write("\n dodatkowa linia")
#
# # # mode a+ odczytuje oraz dopisuje dane do naszego pliku
# with open("nic_dwa_razy.txt", mode="a+") as plik:
#     tresc = plik.read()
#     print(tresc)
#     plik.write("\n dodatkowa linia")

# mode w+ odczytuje oraz nadpisuje dane naszego pliku
# with open("nic_dwa_razy_2.abc", mode="a+") as plik:
#     tresc = plik.read()
#     print(tresc)
#     plik.write("dodatkowa linia")
#
# with open("example.json") as plik:
#     tresc_pliku = json.loads(plik.read())
#     # tresc_pliku = plik.read()
#     print(tresc_pliku)
#
# with open("test.json", mode="a+") as plik:
#     plik.write(json.dumps(tresc_pliku))





