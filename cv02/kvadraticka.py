# Napište program, který najde v R kořeny kvadratické rovnice
# Koeficienty budou v proměnných `a`, `b` a `c`
# Program vypíše:
# - Rovnice má kořeny <x1>, <x2>
# - Rovnice má dvojnásobný kořen <x>
# - Rovnice nemá v R řešení
from math import sqrt

a = input("Zadej koeficient u x^2: ")
#print(repr(a))
a = float(a)
b = float(input("Zadej koeficient u x: "))
c = float(input("Zadej konstantni clen: "))

D = b**2 - 4*a*c

# Než budeme počítat kořeny, musíme ověřit, že nebudeme dělit nulou nebo odmocňovat záporné číslo
if D < 0:
	print("Rovnice nemá řešení v R")
elif D == 0:
	x = -b/(2*a)
	print("Rovnice má dvojnásobný kořen ",x)
else:
	x1 = -b+sqrt(D)/(2*a)
	x2 = -b-sqrt(D)/(2*a)
	print("Rovnice má 2 kořeny: ",x1, x2)
