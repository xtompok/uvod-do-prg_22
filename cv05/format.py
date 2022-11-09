pi = 3.1415927
a = "Ahoj"
b = True
print("pi ma hodnotu", pi, "a promenna a ma hodnotu",a)
print(f"pi^2 ma hodnotu {pi**2:.2f} a promenna a ma hodnotu {a:>20}")
print(f"pi^2 ma hodnotu {pi**2:.2f} a promenna a ma hodnotu {a:^20}")
print(f"16 je v hexa {16:x}")
print(f"Promenna a jeji hodnota: {pi=}")
print(f"Promenna ve {{slozenych zavorkach}} {b=}")

#https://docs.python.org/3/library/string.html#format-specification-mini-language

# Přepište DMS konverzi na používání f-stringů, vteřiny zaokrouhlete na 2 desetinná místa, stupně na 5
# Každý řádek by měl být vypsán jedním f-stringem