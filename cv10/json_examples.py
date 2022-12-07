import json

# Slovník jako datová struktura
parkoviste = {
	"jmeno": "P+R Zličín",
	"kapacita": {
		"obycejne": 340,
		"ztp": 6,
		"elektromobily": 10
	},
	"pr": True,
	"zaplnenost": 320,
	"seznam": [1,2,3],
}

astr = json.dumps(parkoviste, ensure_ascii=False, indent=2)
print(astr)

with open("parkoviste.json","w", encoding="utf-8") as f:
	json.dump(parkoviste,f, ensure_ascii=False, indent=2)

with open("parkoviste.json", encoding="utf-8") as f:
	parkoviste2 = json.load(f)


print(type(parkoviste2))
print(parkoviste2)
