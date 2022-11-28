# Jak bychom mohli zpracovávat CSV, kdybychom neměli modul `csv`
with open("parkoviste.csv") as f:
	# Textový soubor lze procházet `for` cyklem po řádcích
	for line in f:
		# Vypíšeme si řádek, ať víme, s čím pracujeme
		print(line)
		# Pomocí `rstrip()` ořízneme bílé znaky na konci řádku, v tomto případě `\n` -- konec řádku
		# Pomocí `split(";")` rozdělíme řádek na seznam řetězců tak, že v každém výskytu `;` rozlomíme řetězec na dva
		cols = line.rstrip().split(";") 
		# Vypíšeme si třetí sloupec
		print(cols[2])
