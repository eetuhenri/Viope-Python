luku_1 = input ("Anna ensimmäinen luku:")
luku_2 = input ("Anna toinen luku:")

print("(1)+\n(2)-\n(3)*\n(4)/")

valinta = input("Tee valinta (1-4):")

if valinta == "1":
	print("Tulos on:", int(luku_1) + int(luku_2))
elif valinta == "2":
	print("Tulos on:", int(luku_1) - int(luku_2))
elif valinta == "3":
	print("Tulos on:", int(luku_1) * int(luku_2))
elif valinta == "4":
	print("Tulos on:", int(luku_1) / int(luku_2))
else:
	print("Valintaa ei tunnistettu.")
	
