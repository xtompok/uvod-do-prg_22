import requests

response = requests.get("https://mapa.pid.cz/getData.php")
data = response.json()

print("Loaded")
trips = data['trips']
vehicles = list(trips.values())
for v in vehicles:
	print(v)

# 1. Vypište všechny linky
# 2. Vypište průměrné zpoždění dohromady
# 3. Vypište průměrné zpoždění každé linky