cislo =6

if cislo == 0:
	print("Nic")
elif cislo < 5:		# elif je nepovinný a může tam být vícekrát
	print("Malo")
else:			# else je nepovinné a může tam být nejvýše jednou (protože je to pro všechny ostatní varianty, které nepobraly ify a elify výše)
	print("Moc")
