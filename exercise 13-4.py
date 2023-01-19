class Emo:
	arvo = 0
	tila = "Toiminnassa"
	
	def tulostus(self):
		print("Minä olen emoluokka.")
		
class Lapsi(Emo):
	
	def tulostus1(self):
		print("Minä olen lapsiluokka.")
		
def main():
	emo = Emo()
	lapsi = Lapsi()
	print(emo.tila)
	emo.tulostus()
	print(lapsi.tila)
	lapsi.tulostus1()
	
	
if __name__ == "__main__":
    main()
