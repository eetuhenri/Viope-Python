import math


def syote():
    while True:
        try:
            luku = int(input("Anna luku: "))
            break
        except ValueError:
            print("Virheellinen syöte!")
            continue

    return luku


luku_1 = syote()
luku_2 = syote()

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(luku1/luku2)\n(6) cos(luku1/luku2)\n(7) Vaihda luvut\n(8) Lopeta")

    print("Valitut luvut: {0} {1}".format(luku_1, luku_2))
    valinta = int(input("Tee valinta (1-8): "))

    if valinta == 1:
        print("Tulos on:", luku_1 + luku_2)
    elif valinta == 2:
        print("Tulos on:", luku_1 - luku_2)
    elif valinta == 3:
        print("Tulos on:", luku_1 * luku_2)
    elif valinta == 4:
        print("Tulos on:", luku_1 / luku_2)
    elif valinta == 5:
        print("Tulos on:", math.sin(luku_1 / luku_2))
    elif valinta == 6:
        print("Tulos on:", math.cos(luku_1 / luku_2))
    elif valinta == 7:
        luku_1 = syote()
        luku_2 = syote()
    elif valinta == 8:
        break
    else:
        print("Valintaa ei tunnistettu.")
