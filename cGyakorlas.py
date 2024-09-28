def harom():
    for i in range(21):
        print(i)
    """
    for i in range(0, 21):
        print(i)

    for i in range(0, 21, 1):
        print(i)

    i = 0
    while i < 21:
        print(i)
        i+=1
    """


def negy():
    pass
    for i in range(20, 57, 2):
        print(i)


def ot():
    for i in range(77, -77, -4):
        print(i)


def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot!"))
    return szam


def hat():
    szam1 = beolvas()
    szam2 = beolvas()

    if szam2 < szam1:
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet

    for i in range(szam1, szam2+1, 1):
        print(i, end=" ")


def het():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2
    if szorzat < 0:
        for i in range(0, szorzat-1, -1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat+1, 1):
            print(i, end=" ")


def nyolc():
    pass


def kilenc():
    pass