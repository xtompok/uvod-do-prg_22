# Z řetězců i seznamů vybíráme pomocí [index], index se počítá od nuly
print('ahoj'[0])
a = 'ahoj'
# Řetězce jsou neměnné, funkce modifikující řetězec vrací jeho modifikovanou kopii
b = a.upper()
# `a` a `b` jsou různé řetězce
print(a)
print(b)

# Seznam definujeme pomocí prvků oddělených čárkou v hranantých závorkách.
a = [1,2,3,4,5]
# Seznamy jsou modifikovatelné, do prvků lze přiřadit novou hodnotu
a[0] = -1
# Výpis seznamu
print(a)
# Výpis typu proměnné `a` (tedy `list`)
print(type(a))

# Ntici definujeme pomocí prvků oddělených čárkou v kulatých (nebo žádných) závorkách
b = (1,2,3,4,5)
# Prvky ntice nejde modifikovat, jsou stejně jako řetězce neměnné
# Výpis ntice
print(b)
# Výpis typu proměnné `b` (tedy `tuple` == ntice)
print(type(b))

# Prázdný seznam můžeme vytvořit pomocí `[]` nebo zavoláním funkce `list()`
prazdny_seznam = []
prazdny_seznam = list()
# Napište hru hádej číslo 2
# Program na začátku vytvoří seznam `n=5` náhodných čísel (0--10)
# Následně postupně vždy číslo odebere a nechá uživatele hádat
# Když dojdou čísla, program skončí
