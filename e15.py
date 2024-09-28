def egeszbeolvas():
    szam = float(input("Kérem adjon megegy valos számot!"))
    return szam

# eljárás


def teglalap():

    oldal1 = egeszbeolvas()
    oldal2 = egeszbeolvas()

    if (oldal1 > 0) and (oldal2 > 0):
        kerulet = round(2*(oldal1+oldal2), 2)
        terulet = round(oldal1 * oldal2, 2)
        print("A téglalap kerulete: "+str(kerulet)+", területe: "+str(terulet)+".")
    else:
        print("Hiba: a téglalap oldalai nem pozitivak!")
