import os


file = os.chmod("nic_dwa_razy.txt", mode="")

plik = open(file="nic_dwa_razy.txt")
print(type(plik))
# print(plik.read())
# print(plik.readline())
for line in plik:
    print(line)
plik.close()

with open("nic_dwa_razy.txt") as plik:
    print(plik.read())

with open("nic_dwa_razy.txt") as plik:
    plik.write("To napisala Wislawa Szymborska")