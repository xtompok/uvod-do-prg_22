def podel(a,b):
#	try:
		return a/b
#	except ZeroDivisionError:
#		print("Dělíme nulou!")
#		return 2000

def vydel_nulou(a):
	#try:
	vysledek = podel(a,1)
	#except ZeroDivisionError:
	#	print("Jejda, dělili jsme nulou")
	#	return 1000
	return vysledek

def uzivatelske_deleni():
	try:
		cislo = int(input("Zadej číslo"))
		vysledek = vydel_nulou(cislo)
		raise NameError("Výsledek je špatně")
		return vysledek
	except ValueError:
		print("Nebylo to číslo")
		return None
	except ZeroDivisionError:
		print("Bylo děleno nulou")
		return None
	else:
		pass
	finally:
		print("provádím finally")
		# Provede se úplně vždycky
	return vysledek

print(uzivatelske_deleni())
