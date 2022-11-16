def kvadrat(a):
	vysledek = a*a
	return vysledek

def soucet(a,b):
	return a+b

def soucet2(a:int,b:int)->int: # Type hint
	"""Secte 2 cisla"""
	return a+b

def inkrementuj(a):
	# a = 5
	a = a + 1
	# a = 6
	return a
	# return 6

a = 5
a = inkrementuj(a) # a = inkrementuj(5) # a = 6
print(a)

print(soucet2(3,4))
#print(soucet2(3.5,4.5))

# Napište funkce pro obsah čtverce, obdélníku, kruhu

def umocni(cislo, exponent=2):
	return cislo**exponent

print(umocni(4,3))
print(umocni(4))

# Napište funkci potvrd()
# Funkce se pta uzivatele tak dlouho, dokud nezada ano/ne, to vrati jako bool

def potvrd() -> bool:
	while True:
		vstup = input("Zadej ano nebo ne: ")
		vstup = vstup.lower()
		if vstup == "ano":
			return True
		elif vstup == "ne":
			return False
	
print(potvrd())
