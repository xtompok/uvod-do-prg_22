# Funkce a konstanty také můžeme přímo importovat do našeho programu a pak se
# chovají, jako bychom je vytvořili lokálně
from ui import read_float, read_int, PI


myint = read_int("Zadej číslo: ")
print(myint+1)

myfloat = read_float("Zadej float: ")
print(myfloat/PI)
