# Importujeme náš modul ui.py, musí být ve stejné složce jako program
import ui

# Použijeme funkci read_int z modulu ui
myint = ui.read_int("Zadej číslo: ")
print(myint+1)

# Použijeme funkci read_float z modulu ui
myfloat = ui.read_float("Zadej float: ")
# Použijeme konstantu PI z modulu ui
print(myfloat/ui.PI)
