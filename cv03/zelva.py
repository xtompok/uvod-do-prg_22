from turtle import forward, exitonclick, right, left, speed

speed(10)	# 0 - nejrychleji, pak 1--10 od nejpomalejšího po rychlý
for j in range(10):
	for i in range(4):
		forward(100)
		left(90)
	left(36)
exitonclick()

# Nakreslete čtvercovou síť o a sloupcích a b řádcích
# Nakreslete "kytičku"
# Nakreslete šestiúhelníkovou síť