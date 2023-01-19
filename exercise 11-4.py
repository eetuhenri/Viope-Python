import time

tiedoston_nimi = "muistio.txt"

try:
    tiedosto = open(tiedoston_nimi, "r")
    tiedosto.close()
except IOError:
    print("Oletusmuistioa ei löydy, luodaan tiedosto.")

while True:
    print("käytetään muistiota: {0}".format(tiedoston_nimi))
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")

    valinta = int(input("Mitä haluat tehdä?: "))

    if (valinta == 1):
        tiedosto = open(tiedoston_nimi, "r")
        sisalto = tiedosto.read()
        print(sisalto)
        tiedosto.close()
    elif (valinta == 2):
        tiedosto = open(tiedoston_nimi, "a")
        lisays = input("Kirjoita uusi merkintä: ")
        aika = time.strftime("%X %x")
        tiedosto.write(lisays + ":::" + aika)
        tiedosto.close()
    elif (valinta == 3):
        tiedosto = open(tiedoston_nimi, "w")
        print("Muistio tyhjennetty.")
        tiedosto.close()
    elif (valinta == 4):
        tiedoston_nimi = input("Anna tiedoston nimi: ")
        try:
            tiedosto = open(tiedoston_nimi, "r")
            tiedosto.close()
        except IOError:
            print("Tiedostoa ei löydy, luodaan tiedosto.")
    elif (valinta == 5):
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta")
