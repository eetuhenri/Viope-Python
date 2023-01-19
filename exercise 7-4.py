

luku_1 = input ("Anna ensimmäinen luku:") #Valitaan ensimmäinen luku
luku_2 = input ("Anna toinen luku:") #Valitaan toinen luku

while True:
	print("(1)+\n(2)-\n(3)*\n(4)/\n(5)Vaihda luvut\n(6)Lopeta\nValitut luvut:", luku_1, luku_2) #Listaus valittavista vaihtoehdoista
	valinta = input("Tee valinta (1-6):") #Tee valinta
	
	if valinta == "1":
		print("Tulos on:", int(luku_1) + int(luku_2))
	elif valinta == "2":
		print("Tulos on:", int(luku_1) - int(luku_2))
	elif valinta == "3":
		print("Tulos on:", int(luku_1) * int(luku_2))
	elif valinta == "4":
		print("Tulos on:", int(luku_1) / int(luku_2))
	elif valinta == "5": #Uudet luvut
		luku_1 = input ("Anna uusi ensimmäinen luku:")
		luku_2 = input ("Anna uusi toinen luku:")
	elif valinta == "6": #Ohjelma loppuu
		break
	else:
		print("Valinta ei ole oikein")
