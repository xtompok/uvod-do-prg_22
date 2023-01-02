from turtle import exitonclick, right,left,forward, speed, backward

# Funkce volající sama sebe, tato vede k nekonečné rekurzi
def volej_sama_sebe(i):
	print(i)
	volej_sama_sebe(i+1)

# Při spuštění vypadne chyba o překročení maximální hloubky rekurze
#volej_sama_sebe(0)

# Výpočet faktoriálu pomocí rekurze
# Pouze demonstrační příklad, v praxi nepraktické, lépe počítat obyčejným for cyklem
def factorial(n):
	print(f"Pocitam faktorial {n}")
	# koncová podmínka, nutná, aby rekurze někdy skončila
	if n == 1:
		return 1
	# volání sebe sama. n se snižuje, tedy jednou dojde na koncovou podmínku a rekurze skončí 
	return n * factorial(n-1)

print(factorial(5))
print(factorial(10))

# Kreslení Kochovy vločky (viz https://cs.wikipedia.org/wiki/Kochova_k%C5%99ivka)
def koch(alen, order):
	""" Funkce kreslící Kochovu vločku (jednu stranu)

	alen - celková délka strany
	order - řád vločky. 0 odpovídá rovné čáře, čím vyšší, tím členitější
	"""
	# Pokud klesl řád na nulu, nakreslíme rovnou čáru a skončíme
	if order == 0:
		forward(alen)
		return
	# Jinak nakreslíme čtyři Kochovy vločky třetinové velikosti o jedna
	# menšího řádu do tvaru Kochovy vločky
	koch(alen/3,order-1)
	left(60)
	koch(alen/3,order-1)
	right(120)
	koch(alen/3, order-1)
	left(60)
	koch(alen/3, order-1)

# Postupné opakované kreslení jednotlivých iterací Kochovy vločky přes sebe
speed(4)
backward(500)
koch(500,1)
backward(500)
koch(500,2)
backward(500)
koch(500,3)
backward(500)
koch(500,4)
backward(500)
koch(500,5)
exitonclick()
