def main():
	while True:
		tieto = input("Anna syöte (Lopeta lopettaa):")
		if tieto == "Lopeta":
			break
		else:
			tulostaja(tieto)
	


def tulostaja(saatutieto):
	if len(saatutieto) < 5:
		print("Oletustulostus")
	else:
		print(saatutieto)
	
if __name__ == "__main__":
    main()
