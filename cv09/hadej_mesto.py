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


# Města, ze kterých budeme hádat
mesta = ["Brno", "Praha", "Litomyšl", "Město Albrechtice"]

# Pomocí random.choice vybereme náhodný prvek ze seznamu (výběr s opakováním)
hadane_mesto = random.choice(mesta)

# Varianta "mám seznam, co vypisuji" - držím si informaci o uhádnutých písmenech
# ve formě seznamu písmen hádaného slova, který obsahuje na pozicích, které
# ještě nebyly uhádnuty, podtržítka a když uživatel zadá písmeno, tak nahradím
# na místech výskytu tipnutého písmena ve slově podtržítko za toto písmeno. Na
# konci tedy žádné podtržítko v seznamu není

# Vytvořím si seznam podtržítek stejně dlouhý, jako je hádané město
uhadnuto = ["_" for znak in hadane_mesto]

# Dokud seznam obsahuje nějaké podtržítko
while "_" in uhadnuto:
	# Vypíši, co už mám uhádnuto (spojím prvky seznamu mezerami a vypíši)
	print(" ".join(uhadnuto))
	pismeno = input("Zadej znak:")
	# Procházím písmena hádaného města
	for (idx, mznak) in enumerate(hadane_mesto):
		# Pokud zadané písmeno odpovídá písmenu města na aktuální pozici
		if pismeno.lower() == mznak.lower():
			# přepíši podtržítko za písmeno (to vezmu z hádaného
			# města, abych zachoval velká / malá písmena
			uhadnuto[idx] = mznak

# Nakonec vypíšu celé město (bez prokládání mezerami)
print("".join(uhadnuto))
print("Gratulujeme.")

# Varianta "pamatuji si, co už uživatel zadal" - držím si seznam již hádaných
# písmen, jestli vypíši podtržítko nebo písmeno, se rozhoduji až těsně před
# výpisem

# Seznam hádaných písmen
hadano = []
# Ukončení je řešeno pomocí break
while True:
	# Předpokládáme, že už je město uhádnuto
	hotovo = True
	# Procházíme znaky hádaného města
	for mznak in hadane_mesto:
		# Pokud je aktuální znak v hádaných písmenech, vypíšeme ho
		if mznak.lower() in hadano:
			print(mznak,end=" ")
		# jinak vypíšeme podtržítko a zapamatujeme si, že jsme ještě
		# neuhádli
		else:
			print("_",end=" ")
			hotovo = False
	# Pokud jsme uhádli slovo, skončíme
	if hotovo:
		print("Gratulujeme")
		break
	# Jinak si vyžádáme další písmeno
	pismeno = input("Zadej pismeno").lower()
	# Pokud není v seznamu již hádaných, tak ho do seznamu přidáme
	if not pismeno in hadano:
		hadano.append(pismeno)
