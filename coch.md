# ČOCH aneb Často opakované chyby

Zde se nachází seznam často opakovaných chyb v domácích úkolech. Slouží k tomu,
aby se na něj dalo rychle odkazovat při opravování a zároveň byl problém jasně
popsaný a zdůvodněný

## 1. Funkce používá proměnné mimo svůj scope
Ve funkcích je vhodné používat pouze takové proměnné, které jsme buď dostali
jako argument funkce, nebo jsme si je uvnitř funkce vytvořili. Je tomu tak
proto, abychom pak funkci mohli použít odjinud a nemuseli jsme se bát, že nám přepíše
nějaké proměnné používané mimo funkci a naopak že nebude vyžadovat existenci nějak
specificky pojmenovaných proměnných. Výjimky jsou možné v dobře odůvodněných případech,
pak je ale vhodné do dokumentačního komentáře k funkci napsat, jaké proměnné a jaké
hodnoty v nich funkce očekává.
