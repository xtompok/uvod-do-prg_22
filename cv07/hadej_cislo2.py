from random import randint

# Vytvoříme prázdný seznam
cisla = []
# Postupně do něj přidáme 5 čísel
for i in range(5):
	# `.append(<prvek>)` přidá <prvek> na konec seznamu
	# `randint` vrátí náhodné číslo ze zadaného rozsahu
	cisla.append(randint(0,10))

# Vypíšeme vytvořený seznam
print(cisla)

# Seznam můžeme projít for cyklem...
#for hadane in cisla:
# ... nebo procházíme, dokud je neprázdný a vždy z něj hledané číslo odebereme pomocí `.pop()`
while cisla:
	# `.pop()` odebírá poslední prvek
	hadane = cisla.pop()
	# Hádáme číslo, dokud není uhodnuté
	while True:
		x = int(input("Hádej:"))
		if x < hadane:
			print("Málo!")
			continue
		elif x > hadane:
			print("Moc!") 
			continue
		print("Gratuluji, správně!")
		break

print("Čísla došla, vyhrál jsi!")
