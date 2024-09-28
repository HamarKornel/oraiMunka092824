def kocka():
    el = int(input("Kérem adjon meg egy él értéket!"))
    if el <= 0:
        print("Hiba: a kocka élének értéke nem pozítív")
    else:
        felszin = 6 * el**2
        terfogat = pow(el, 3)

        print("Kocka felszine: "+str(felszin)+", térfogata: "+str(terfogat)+".")
