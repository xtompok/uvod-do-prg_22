import csv

# Otevřeme soubor parkoviste.csv, parametr newline doporučuje dokumentace modulu csv
with open("parkoviste.csv", encoding="utf-8", newline='') as f:
	# Vytvoříme reader - objekt na čtení CSV, oddělovač sloupců jsou středníky
	reader = csv.reader(f, delimiter=";")
	# Načteme jeden (první) řádek z CSV, uložíme ho do proměnné `column_names`
	column_names = next(reader)
	# Zbylé řádky načítáme v cyklu, postupně jsou přiřazeny do proměnné `row`
	for row in reader:
		# Vypíšeme načtený řádek
		print(row)
	# Vypíšeme řádek s názvy sloupečků (viz výše)
	print(f"Column names: {column_names}")

# 1. Pro každé parkoviště vypište jméno a kapacitu
with open("parkoviste.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=";")
	# Zahodíme první řádek s názvy sloupců
	next(reader)
	for row in reader:
		# Řádek je seznam sloupců, tedy můžeme indexovat jednotlivé buňky
		print(f"{row[0]}: {row[-1]}")

# 2. Spočtěte celkovou kapacitu parkovišť
with open("parkoviste.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=";")
	next(reader)
	# Vytvoříme si proměnnou pro celkovou kapacitu
	capacity = 0
	for row in reader:
		# Soubor může obsahovat na konci prázdné řádky, když se nám nepodaří převést kapacitu na int, tak řádek přeskočíme
		try:
			#capacity = capacity + int(row[-1]) # Ekvivalentní s řádkem níže
			# Připočítáme aktuální kapacitu k celkové
			capacity += int(row[-1]) 
		except ValueError:
			# Pokud kapacita není číslo, nic neděláme (a tedy daný řádek přeskočíme
			pass
print(f"Celkem míst: {capacity}")


# 3. Spočtěte celkovou kapacitu P+R parkovišť
# Řešení viz 2 a 4

# 4. Uložte P+R parkoviště do souboru pr.csv tak, že budou obsahovat
#    sloupce `name` a `totalNumOfPlaces`.

# Otevřeme si soubor `parkoviste.csv` pro čtení a `pr.csv` pro zápis (parametr `"w"`)
# \ na konci prvního řádku je proto, aby šel druhý open napsat na nový řádek
with open("parkoviste.csv", encoding="utf-8", newline='') as f, \
	open("pr.csv","w",encoding="utf-8", newline='') as fout:
	reader = csv.reader(f, delimiter=";")
	next(reader)
	# Vytvoříme si zapisovací objekt pro CSV nad výstpním souborem
	writer = csv.writer(fout)
	for row in reader:
		# Pokud sloupec pr neobsahuje `true` libovolně velkými písmeny, řádek přeskočíme
		if row[3].lower() != 'true':
			continue
		#writer.writerow([row[0],row[-1]]) # Ekvivalentní s řádky níže
		# Z načteného řádku vyextrahujeme jméno a kapacitu
		name = row[0]
		capa = row[-1]
		# Vytvoříme si výstupní řádek jako seznam sloupců
		outrow = [name, capa]
		# Zapíšeme řádek do výstupního souboru
		writer.writerow(outrow)

