def testaa(syöte):
	if len(syöte) < 5:
		return False
	else:
		if not syöte.isdigit() and syöte.isalnum(): 
			for char in syöte:
				if char.isdigit():
					return True
		else:
			return False
	
