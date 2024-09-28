import math
# from math import pow, pi


def kor():
    r = float(input("Kérem adjon meg egy kör sugár értékét!"))
    if r > 0:
        terulet = r ** 2 * math.pi
        # terulet2 = r * r * math.pi
        # terulet3 = math.pow(r, 2) * math.pi
        # terulet4 = pow(r, 2) * math.pi
        kerulet = 2 * r * math.pi

        print("A kör területe: "+str(terulet)+", a kör kerülete: "+str(kerulet)+".")
    else:
        print("HIBA: a kör sugara nem pozitiv.")
