import time
import pickle

tiedoston_nimi = "muistio.dat"
lista = []

try:
    tiedosto = open(tiedoston_nimi, "rb")
    lista = pickle.load(tiedosto)
    tiedosto.close()
except IOError:
    print("Virhe tiedostossa, luodaan uusi muistio.dat.")
    tiedosto = open(tiedoston_nimi, "wb")

while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja "
          "lopeta\n")

    valinta = int(input("Mitä haluat tehdä?:"))

    if (valinta == 1):
        for i in lista:
            print(i)
    elif (valinta == 2):
        lisays = input("Kirjoita uusi merkintä:")
        aika = time.strftime("%X %x")
        kokonaisuus = lisays + ":::" + aika
        lista.append(kokonaisuus)
        pickle.dump(lista, tiedosto)
    elif (valinta == 3):
        try:
            pituus = len(lista)
            print("Listalla on {0} merkintää.".format(pituus))
            muutos_valinta = int(input("Mitä niistä muutetaan?:"))
            muutos_valinta = muutos_valinta - 1
            print(lista[muutos_valinta])
        except IndexError:
            print("Virheellinen valinta.")
        else:
            uusi_teksti = input("Anna uusi teksti:")
            aika = time.strftime("%X %x")
            kokonaisuus = uusi_teksti + ":::" + aika
            lista.pop(muutos_valinta)
            lista.insert(muutos_valinta, kokonaisuus)
            tiedosto = open(tiedoston_nimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
    elif (valinta == 4):
        pituus = len(lista)
        print("Listalla on {0} merkintää.".format(pituus))
        poisto_valinta = int(input("Mitä niistä poistetaan?:"))
        try:
            poisto_valinta = poisto_valinta - 1
            print("Poistettiin merkintä {0}".format(lista[poisto_valinta]))
            lista.pop(poisto_valinta)
            tiedosto = open(tiedoston_nimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
        except IndexError:
            print("Virheellinen valinta.")
    elif (valinta == 5):
        tiedosto = open(tiedoston_nimi, "wb")
        pickle.dump(lista, tiedosto)
        print("Lopetetaan.")
        tiedosto.close()
        break
    else:
        print("Tuntematon valinta")
