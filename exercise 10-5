import time
while True:
	print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta")
	valinta = int(input("Mitä haluat tehdä?:"))
	
	if (valinta == 1):
		muistikirja = open("muistio.txt", "r")
		teksti = muistikirja.read()
		print(teksti)
	elif (valinta == 2):
		muistikirja = open("muistio.txt", "a")
		lisays = input("Kirjoita uusi merkintä:")
		curr_time = time.strftime("%X %x")
		muistikirja.write(lisays +":::"+ curr_time + "\n")
		muistikirja.close()
	elif (valinta == 3):
		muistikirja = open("muistio.txt", "w")
		muistikirja.close()
		print("Muistio tyhjennetty.")
	elif (valinta == 4):
		print("Lopetetaan.")
		break
	else:
		print("Tuntematon valinta.")
