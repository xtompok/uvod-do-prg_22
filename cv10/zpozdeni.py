# Modul requests slouží pro stahování z webu
import requests

# Stáhneme polohy vozidel
response = requests.get("https://mapa.pid.cz/getData.php")
# Je to JSON, takže rovnou requests umí výsledek rovnou naparsovat a vrátit nám Pythoní strukturu
data = response.json()

print("Loaded")
# Najdeme si seznam vozidel
trips = data['trips']
vehicles = list(trips.values())
# Procházíme vozidla, každé vozidlo je slovník samo o sobě
for v in vehicles:
	print(v)

# 1. Vypište všechny linky
# 2. Vypište průměrné zpoždění dohromady
# 3. Vypište průměrné zpoždění každé linky
