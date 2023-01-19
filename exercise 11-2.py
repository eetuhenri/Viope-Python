tiedoston_nimi = input("Anna tiedoston nimi: ")

try:
    tiedosto = open(tiedoston_nimi, "r")
    sisalto = tiedosto.read()
    sisalto = int(sisalto) + 313
    tiedosto.close()

except IOError:
    print("Virheellinen tiedostonnimi")

except ValueError:
    print("Tiedoston sisältö virheellinen!")

else:
    print("Saatiin tulos {0}".format(sisalto))
		
