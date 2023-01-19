class kilpailija:
	"""Kilpailija: sisältää pisteet ja värin"""
	pisteet = 0
	vari = ""
	
	def __init__(self):
		self.vari = input("Anna minulle väri:")
	
	def tilanne(self):
		print("Olen", self.vari, "ja minulla on", self.pisteet, "pistettä!")
	
def main():
	eka = kilpailija()
	toinen = kilpailija()
	eka.tilanne()
	toinen.tilanne()
	print(eka.__doc__)

