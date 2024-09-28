import math


def negyzegyok():
    szam = float(input("Adjon meg egy számot"))
    if szam >= 0:
        gyok = math.sqrt(szam)
        print(gyok)
    else:
        print("HIBA: negativ szám gyökét akarja számolni!")
