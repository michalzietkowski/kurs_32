# import narzedzia
# from narzedzia import Kosiarka, Mlotek, Pilarka, Srubokret
# import narzedzia as moj_wymysl
from narzedzia_paczka import Mlotek, Srubokret

print("Witaj w naszym warsztacie narzędziowym. Oto lista twoich narzędzi: młotek, kosiarka, pilarka, śrubokręt")
# Tutaj powinien byc kod wykonywalny

# srubokret = narzedzia.Srubokret("krzyzak", "czerwony")
# pilarka = narzedzia.Pilarka("mocne", "automatyczna")
# kosiarka = narzedzia.Kosiarka("zylka", "600W", "spalinowa")
# mlotek = narzedzia.Mlotek("niebieski", "20cm")
# srubokret.skrec_cos()
# print(narzedzia.zmienna_1)
# #
# srubokret = Srubokret("krzyzak", "czerwony")
# pilarka = Pilarka("mocne", "automatyczna")
# kosiarka = Kosiarka("zylka", "600W", "spalinowa")
# mlotek = Mlotek("niebieski", "20cm")
# srubokret.skrec_cos()
# print(zmienna_1)
#
# srubokret = moj_wymysl.Srubokret("krzyzak", "czerwony")
# pilarka = moj_wymysl.Pilarka("mocne", "automatyczna")
# kosiarka = moj_wymysl.Kosiarka("zylka", "600W", "spalinowa")
# mlotek = moj_wymysl.Mlotek("niebieski", "20cm")
# srubokret.skrec_cos()
# print(moj_wymysl.zmienna_1)

srubokret = Srubokret("krzyzak", "czerwony")
mlotek = Mlotek("niebieski", "20cm")
srubokret.skrec_cos()
mlotek.wypozycz()