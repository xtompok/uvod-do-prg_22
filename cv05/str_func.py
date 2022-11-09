my_string = " Ahoj Hugo, jak se dari?  "
lower_string = my_string.lower()
print(lower_string)
upper_string = my_string.upper()
print(upper_string)
if "Hugo" in my_string:
	print("Hugo přítomen")
if "hugo" in my_string.lower():
	print("hugo přítomen")
print(f">{my_string}<")
print(f">{my_string.strip()}<")