# V modulu můžeme definovat funkce
def read_int(prompt: str) -> int:
	""" Read integer from user."""
	return int(input(prompt))

def read_float(prompt: str) -> float:
	""" Read float from user """
	return float(input(prompt))

# V modulu můžeme definovat i konstanty
PI=3.1415927


# Není vhodné v modulu cokoli počítat / vypisovat, protože se to provede vždy
# jen při prvním importu a může to mít vedlejší účinky, se kterými program,
# který z modulu importuje, nepočítá
# print("Ahoj Hugo")
