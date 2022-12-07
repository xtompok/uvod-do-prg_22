import random
# Napište program, který ze seznamu měst vybere jedno a pak nechá uživatele
# zadávat písmena tak dlouho, dokud nezadá všechna, která jsou ve jménu daného
# města 

# (Hádáte Kokory)
# _ _ _ _ _ _
# Zadej písmeno: R
# _ _ _ _ r _
# Zadej písmeno: K
# K _ k _ r _
# Zadej písmeno: e
# K _ k _ r _
# Zadej písmeno: o
# K o k o r _
# Zadej písmeno: y
# K o k o r y
# Vyhrál jsi

# v1 - hádané slovo je v proměnné
# v2 - hádané slovo se vybírá ze seznamu
# v3 - hádaný seznam se načítá ze souboru

for index, item in enumerate(["Ahoj","čau"]):
	print(f"{index}: {item}")

# ukazat random choice

mesta = ["Brno", "Praha", "Litomyšl", "Město Albrechtice"]

hadane_mesto = random.choice(mesta)

# Varianta "mám seznam, co vypisuji"
uhadnuto = ["_" for znak in hadane_mesto]
while "_" in uhadnuto:
	print(" ".join(uhadnuto))
	pismeno = input("Zadej znak:")
	for (idx, mznak) in enumerate(hadane_mesto):
		if pismeno.lower() == mznak.lower():
			uhadnuto[idx] = mznak
print("".join(uhadnuto))
print("Gratulujeme.")

# Varianta "pamatuji si, co už uživatel zadal"
hadano = []
while True:
	hotovo = True
	for mznak in hadane_mesto:
		if mznak in hadano:
			print(mznak,end=" ")
		else:
			print("_",end=" ")
			hotovo = False
	if hotovo:
		print("Gratulujeme")
		break
	pismeno = input("Zadej pismeno")
	if not pismeno in hadano:
		hadano.append(pismeno)
