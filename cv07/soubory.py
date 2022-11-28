# Pomocí `with` můžeme otevřít soubor, aniž bychom museli řešit, kdy ho zavřít
# Uvnitř bloku vystupuje otevřený soubor pod jménem, co jsme uvedli za `as`
with open("soubor.txt") as f:
	# Celý obsah souboru přečteme pomocí `read()` bez parametrů
	obsah = f.read()
	# Vypíšeme načtený obsah
	print(repr(obsah))
	# Teď jsme na konci souboru, takže další read už nic nenačte
	obsah = f.read()
	print(repr(obsah))

# Pokud chceme soubor přečíst znovu, musíme ho otevřít znovu (nebo se v něm posunout, ale to není předmětem tohoto cvičení)
with open("soubor.txt") as f:
	obsah = f.readlines()
	print(obsah)

# U textových souborů je vhodné určit, v jakém kódování soubor je (obvykle utf-8 nebo windows-1250)
with open("soubor.txt",encoding="utf-8") as f:
	for line in f:
		print(line.rstrip())

# Pro zápis do souboru musíme přidat parametr `w` a také je velmi vhodné uvést `encoding`
# Otevření souboru smaže veškerý obsah, který byl v souboru předtím
with open("soubor_out.txt","w",encoding="utf-8") as f:
	# Do souboru můžeme zapisovat pomocí `.write()`, konce řádků ale musíme zadávat explicitně pomocí `\n`.
	f.write("Ahoj, toto je můj první zápis do souboru\n")
	f.write("Ahoj, toto je můj druhý zápis do souboru")


