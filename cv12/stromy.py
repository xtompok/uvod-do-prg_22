from turtle import right,left,exitonclick,forward,backward, speed

def tree(alen,angle):
	""" Nakreslí (binární) strom.
	
	Dokud je větev dostatečně dlouhá, nakreslí větev a na jejím konci nakreslí 2 stromy s kratšími větvemi mezi krerými je zadaný úhel a pak se vrátí do místa, kde funkce začínala

	alen - délka větve
	angle - velikost úhlu mezi větvemi
	"""

	# Koncová podmínka, ukončíme vykonávání
	if (alen < 10):
		return
	# Nakreslíme větev
	forward(alen)
	# Otočíme se o půlku úhlu doleva
	left(angle/2)
	# Nakreslíme levý podstrom, délka větve se zmenšuje, tudíž rekurze někdy skončí
	tree(alen*0.75,angle)
	# Otočíme se doprava
	right(angle)
	# Nakreslíme pravý podstrom
	tree(alen*0.75,angle)
	# Otočíme se zpět tak, jak jsme do aktuálního místa poprvé přišli
	left(angle/2)
	# Zacouváme zpět do výchozího bodu
	backward(alen)


speed(0)
tree(100,30)
exitonclick()
