tiedosto = open("merkkijonoja.txt", "r")
teksti = tiedosto.readlines()
tiedosto.close()

for line in teksti:
	if(line.replace("\n", "").isalnum()):
		print(line, "kelpaa salasanaksi.")
	else:
		print(line, "sisältää virheellisiä merkkejä.")
						  
