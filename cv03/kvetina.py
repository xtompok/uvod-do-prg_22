from turtle import forward,left, exitonclick, speed, right

speed(0)
for _ in range(6):
	for _ in range(6):
		forward(30)
		left(60)
	forward(30)
	right(60)

exitonclick()