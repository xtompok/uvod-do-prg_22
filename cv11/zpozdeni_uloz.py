# Modul requests slouží pro stahování z webu, potřeba doinstalovat
import requests
import json

# Stáhneme polohy vozidel
response = requests.get("https://mapa.pid.cz/getData.php")
# Je to JSON, takže rovnou requests umí výsledek rovnou naparsovat a vrátit nám Pythoní strukturu
data = response.json()

# Výsledek uložíme jako JSON do souboru zpozdeni.json
with open("zpozdeni.json", "w", encoding="utf-8") as f:
	# ensure_ascii a indent slouží k tomu, aby byl výstupní soubor pro člověka přehlednější
	json.dump(data,f, ensure_ascii=False, indent=2)
