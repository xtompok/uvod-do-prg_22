import json

# Načteme data z JSONu do pythonních struktur
with open("zpozdeni.json",encoding="utf-8") as f:
	data = json.load(f)

# Najdeme si seznam vozidel
trips = data['trips']
vehicles = list(trips.values())

# Procházíme vozidla, každé vozidlo je slovník samo o sobě
#for v in vehicles:
#	print(v)

# 1. Vypište všechny linky

# První přístup se seznamem
linky = []
for v in vehicles:
	# získáme jméno linky
	name = v['route']
	# pokud linka není v seznamu, tak ji tam přidáme
	if name not in linky:
		linky.append(name)

# seznam setřídíme a vypíšeme
linky.sort()
print(linky)

# Druhý přístup se slovníkem
linky = {}
for v in vehicles:
	# Vyrobíme ve slovníku klíč jako jméno linky a hodnotu True
	linky[v['route']] = True
# Vypíšeme všechny klíče
print(linky.keys())

# 2. Vypište průměrné zpoždění dohromady
total_delay = 0
for v in vehicles:
	# K celkovému zpoždění připočteme zpoždění aktuálního vozidla
	total_delay += v['delay']
# Celkové zpoždění vydělíme počtem vozidel
print(f"Průměrné zpoždění je {total_delay/len(vehicles)}")

# 3. Vypište průměrné zpoždění každé linky

# Slovník pro celkové zpoždění dané linky
line_delay = {}
# Slovník pro počet vozidel dané linky
line_count = {}
for v in vehicles:
	# získáme jméno linky
	name = v['route']
	# pokud linku ve slovnících už máme, připočteme zpoždění a vozidlo
	if name in line_delay:
		line_delay[name] += v['delay']
		line_count[name] += 1
	# pokud linku ve slovnících ještě nemáme, vytvoříme jí zpoždění rovné
	# aktuálnímu a přidáme první vozidlo
	else:
		line_delay[name] = v['delay']
		line_count[name] = 1

# Vypíšeme průměrné zpoždění po linkách
for (name, delay) in line_delay.items():
	count = line_count[name]
	print(f"Linka: {name} zpoždění: {delay/count}")
