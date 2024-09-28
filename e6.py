def szog():
    vszam = float(input("kérem adjon meg egy valós számot"))
    if (vszam >= 0) and (vszam <= 360):
        if vszam == 0:
            print(str(vszam)+" -> nullszög")
        elif (vszam > 0) and (vszam < 90):
            print(str(vszam)+" -> hegyesszög")
        elif vszam == 90:
            print(str(vszam)+" -> derékszög")
        elif (vszam > 90) and (vszam < 180):
            print(str(vszam)+" -> tompaszög")
        elif vszam == 180:
            print(str(vszam)+" -> egyenesszög")
        elif (vszam > 180) and (vszam < 360):
            print(str(vszam)+" -> homotuszög")
        elif vszam > 360:
            print(str(vszam)+" -> teljesszög")
    else:
        print("HIBA: Nem megfelelő szögérték!")
