# 1)
# Napište program, který převede formát DMS na stupně
# Program se uživatele zeptá na D, M, S a vypíše desetinné stupně

# Rovnou převedeme `str`, co vrátí `input()` na `float`
d = float(input("Zadej stupně: "))
m = float(input("Zadej minuty: "))
s = float(input("Zadej vteřiny: "))

d = d + m/60 + s/3600

print("Výsledek je", d, "stupňů")

