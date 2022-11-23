with open("soubor.txt") as f:
	obsah = f.read()
	print(repr(obsah))
	# Teď jsme na konci souboru, takže další read už nic nenačte
	obsah = f.read()
	print(repr(obsah))

with open("soubor.txt") as f:
	obsah = f.readlines()
	print(obsah)

with open("soubor.txt",encoding="utf-8") as f:
	for line in f:
		print(line.rstrip())

with open("soubor_out.txt","w",encoding="utf-8") as f:
	f.write("Ahoj, toto je můj první zápis do souboru\n")
	f.write("Ahoj, toto je můj druhý zápis do souboru")


