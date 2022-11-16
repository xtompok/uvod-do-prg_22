#int(input("Zadej číslo:"))

#42/0

#while True:
#	pass

while True:
	x = input("Zadej číslo")
	try:
		out = int(x)
		break
	except ValueError:
		print("Nastal ValueError")
		print(f"Hodnota {x} není číslo")

print(out)

# Napište funkci zadej_stupne()
# Pokud stupně nejsou float nebo jsou mimo rozsah <0,360>, 
# nechť zadává znovu

def zadej_stupne():
	while True:
		in_str = input("Zadej stupně")
		try:
			in_float = float(in_str)
		except ValueError:
			print("Nebyly zadany stupně")
			continue
		if in_float < 0 or in_float > 360:
			print("Vstup je mimo rozsah")
			continue
		return in_float
deg = zadej_stupne()
print(deg)

