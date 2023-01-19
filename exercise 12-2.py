lista = []

while True:
    valinta = int(input("Haluatko\n(1)Lisätä listaan\n(2)Poistaa listalta vai\n(3)Lopettaa?: "))
    if valinta == 1:
        lisays = input("Mitä lisätään?: ")
        lista.append(lisays)
    elif valinta == 2:
        try:
            pituus = len(lista)
            print("Listalla on {0} alkiota.".format(pituus))
            poisto = int(input("Monesko niistä poistetaan?: "))
            lista.pop(poisto)
        except IndexError:
            print("Virheellinen valinta.")
    elif valinta == 3:
        print("Listalla oli tuotteet: ")
        for i in lista:
            print(i)
        break
    else:
        print("Virheellinen valinta.")
