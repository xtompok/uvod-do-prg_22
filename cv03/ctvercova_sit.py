from turtle import forward, exitonclick, left, right

a = 5
b = 3
strana = 50

# Nakreslí tabulku
for y in range(b):
	# Nakreslí řádek
	for x in range(a):
		# Nakreslí čtverec
		for i in range(4):
			forward(strana)
			left(90)
		forward(strana)
	right(180)
	forward(a*strana)
	right(90)
	forward(strana)
	right(90)