# Napište program pro výpočet obsahu a obvodu čtverce o straně 324
# Výstup: Obvod čtverce o straně 324 je xxx a jeho obsah je yyyyy
# Pokud je strana čtverce záporná, program si postěžuje a skončí
strana = 457

if strana < 0:
	print("Zadána záporná strana, končím")
	exit()
print("Obvod čtverce o straně " + str(strana) + 
	" je " + str(strana*4) + " a jeho obsah je " + str(strana*strana))
