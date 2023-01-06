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

## 2. Chybí uživatelská dokumentace
Viz [README.md](README.md). Pro 2. úkol by měla obsahovat:
 - co program dělá (tedy efektivně opsané zadání)
 - jméno vstupního souboru
 - požadovaný formát vstupního souboru (sloupce, oddělovače)
 - jména a strukturu výstupních souborů

## 3. Vývojářská dokumentace zbytečně konkrétní
Ve vývojářské dokumentaci není potřeba popisovat druh cyklu, jména proměnných,
čísla řádků apod. Vývojářská dokumentace má ve zkratce popisovat, jak program
funguje, číst jí by mělo být výrazně rychlejší, než si přečíst zdroják.
Například místo věty *Program na řádku 42 vyrobí reader a pak pomocí for cyklu
na řádcích 43--48 přiřazuje třetí sloupec do seznamu `bflm` a pomocí funkce
`try` je implementována ochrana proti chybě ValueError.* je vhodnější napsat
*Pomocí objektu `csv.reader` procházíme v cyklu soubor a průtok si ukládáme do
seznamu. Pokud průtok není číslo, program vypíše chybovou hlášku a skončí.*
Případnému navazujícímu vývojáři podá toto mnohem jasnější představu o tom, co
program skutečně dělá a když uvidí zdroják, tak ho bude snáze chápat.

## 4. Program spadne na prázdném vstupu / vstupním souboru
Pokud program bere nějaký vstup, je třeba předpokládat, že se uživatel splete a
vstupní soubor bude prázdný. V takovémto případě by měl program vypsat chybovou
hlášku a skončit, protože stejně nemá, jak by to řešil.

## 5. Program spadne na neexistujícím souboru / souboru ke kterému nemá přístup
Pokud program čte nebo vytváří nějaké soubory, tak by se měl umět vypořádat s
tím, že očekávaný vstupní soubor neexistuje, nebo že vstupní či výstupní soubor
nejde vytvořit / otevřít z důvodů přístupových práv.


## 6. Není vhodné pojmenovávat proměnné `min` a `max`
`min` a `max` jsou funkce počítající minimum a maximum ze seznamu, takhle to
bude fungovat, ale čtenáře by to mohlo splést. Navíc je pak nepůjde v programu
(snadno) použít.

## 7. Lépe mít `try` blok pro každý soubor zvlášť
Pro uživatele je lepší, když se dozví, který vstupní soubor je vadný než když
se jen dozví, že nějaký. Pokud se načítání jednoho souboru navíc udělá jako
funkce, tak pak kód ani zbytečně nebobtná.

## 8. V Gitu jsou velké soubory
Je v pořádku mít v repozitáři testovací data, ale měla by mít jednotky až
desítky položek a ne několik MB. Zbytečně to zabírá místo a pro otestování
funkčnosti to není potřeba.

## 9. Transformační objekt vytvářet jen jednou
Transoformační objekt mezi souřadnicovými systémy je výpočetně náročné
vytvořit, proto je lepší ho v programu vytvořit pouze jednou a pak ho jen
předávat tam, kde je potřeba. V opačném případě je pak program zbytečně pomalý.

## 10. Dokumentace neobsahuje dostatečný popis vstupních souborů
Dokumentace by měla obsahovat pro každý vstupní soubor:
 - formát souboru
 - souřadnicový systém (pokud se jedná o geodata)
 - požadované sloupce / atributy a jejich význam
