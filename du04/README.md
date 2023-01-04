# Domácí úkol 4 - dělení adresních bodů

## Motivace

V některých situacích nechceme zpracovávat data pro každou jednu jednotku, ale
chceme z jednotek vytvořit skupiny a zpracovávat data dohromady pro celou
skupinu, například pro vyloučení extrémních případů. Jednotky chceme seskupovat
do skupin tak, aby vzniklé skupiny byly kompaktní a nebyly složeny z jednotek
roztroušených po celé mapě a měly nějakou maximální velikost.

## Zadání

Napište neinteraktivní program, který bude metodou [quadtree][1] dělit data do skupin
tak, aby žádná skupina neměla více než 50 jednotek (definujte konstantou na
začátku programu). Program načte vstupní data
ze souboru `input.geojson`, jednotky ze vstupního souboru rozdělí do
skupin pomocí algoritmu quadtree, ke každé jednotce přidá informaci, do které
skupiny patří a jednotky s informacemi o skupinách vypíše do výstupního souboru
`output.geojson`.
Při programování počítejte s tím, že vstupních bodů můžou být desetitisíce.

Budeme uvažovat následující variantu quadtree. Výchozí obdélník je bounding box
množiny vstupních bodů. Pokud nějaká oblast obsahuje více než 50 bodů, rozdělí
se geometricky na čtvrtiny a opět je testována na toto kritérium. Pokud oblast obsahuje méně
než 50 bodů, dále se nedělí.  

### Vstup

Vstup je uložen ve formátu [GeoJSON][2] jako [FeatureColection][3] bodů. Každý bod má
nějaké properties, jejich hodnoty nás nezajímají, ale chceme je zachovat do
výstupního souboru.

Testovací vstupy si můžete vygenerovat například pomocí [Overpass Turbo][4],
uložíte pomocí `Export` -> `download as GeoJSON`, mapou můžete posouvat a měnit
zoom, nové body vygenerujete pomocí `Run`.

### Výstup

Výstup bude uložen také ve formátu GeoJSON, ke každému bodu přibude property
`cluster_id`, která bude určovat, do které skupiny bod patří. Můžete
předpokládat, že tuto property žádný bod ve vstupním souboru nemá. `cluster_id`
musí být jedinečné pro každou skupinu.

Výstupní data můžete snadno vizualizovat například v QGISu, který GeoJSON
nativně podporuje (`Vrstva` -> `Přidat vrstvu` -> `Přidat vektorovou vrstvu`), nastavte si
kategorizovaný symbol podle cluster_id.

### Další požadavky

Funkce počítající quadtree by měly být samostatném modulu `quadtree.py`, hlavní
program by se měl jmenovat `split.py` a funkce si z modulu `quadtree` importovat. 

## Doporučení
Předtím, než začnete programovat, rozmyslete se, jak by měl program fungovat a
pro ucelené části používejte funkce. Napište si kostru programu a pak
implementujte jednotlivé funkce, průběžně ověřujte, zda se chovají dle
očekávání.

## Odevzdání
Odevzdávat budete zdrojový kód projektu a soubor s dokumentací. Vše
bude zabalené v zip souboru, který bude obsahovat adresář `du4_jmeno_prijmeni`,
ve kterém bude soubor se zdrojovým kódem a soubor s dokumentací, tedy například:
```
du4.zip
|
\du4_tomas_pokorny
  |- README.md
  \- du4.py
```
Zip archiv mi pošlete mailem. 

Deadline budiž týden před datem, kdy byste chtěli zápočet. 
Každému, kdo mi pošle úkol, odpovím, že jsem ho přijal a že se mi podařilo zip
rozbalit. Pokud neodpovím, urgujte.

Detaily pro odevzdání přes GitHub viz sekce *Odevzdání přes GitHub*.


## Bodování
  * 5 b za funkční aplikaci
  * 3 b za kvalitu kódu
  * 2 b za dokumentaci

## Bonusové body

### Používání Gitu pro vývoj s vhodnými popisy commitů (1 b)
Pokud budete pro verzování používat Git, vytvořte si účet na GitHubu nebo jiné
podobné stránce a úkol můžete odevzdat přes něj. Kromě samotného odevzdání je
třeba, aby byl repozitář používán i pro vývoj, tedy by měl obsahovat průběžně
commitovanou práci a jednotlivé commity by měly obsahovat stručný a jasný popis
toho, co se v daném commitu změnilo. Repozitář by měl obsahovat jak program, tak
případný soubor s dokumentací, za hodnocenou verzi se počítá poslední commit
pushnutý na GitHub před deadlinem. Repozitář nemusí, ani by neměl, obsahovat
velká vstupní data.  Pokud budete potřebovat pomoct, pište mi.

### Vstupní a výstupní soubory jako argumenty příkazové řádky
Program může dostat argument `-i <vstupni_soubor>` a / nebo `-o
<vystupni_soubor>` a v takovém případě načte vstup a/nebo uloží výstup do
souboru, jehož jméno dostal jako příslušný argument. Pokud daný argument chybí,
berou se soubory dle zadání. Argumenty mohou být oba, v libovolném pořadí.

### Vykreslování průběhu algoritmu (2 b)
Program na začátku vykreslí všechny vstupní body a následně vykresluje, kde
právě probíhá dělení. Body jsou vykresleny tak, aby vhodně vyplňovaly okno. Může
se vám hodit funkce `turtle.screensize()`.

### Další algoritmy na dělení dat (1 -- 5 b dle složitosti)
Na začátku programu bude konstantou `ALGORITHM` zvolen algoritmus, kterým se
bude provádět dělení bodů. Můžete použít libovolný vhodný algoritmus, podle jeho
obtížnosti za něj získáte 1 -- 5 bodů (pokud mi dopředu napíšete, který
algoritmus budete implementovat, odpovím vám, kolik bodů za něj bude).
Implementace quadtree je samozřejmě povinná bez bonusových bodů. Každý
algoritmus by měl být implementován v samostaném modulu.

[1]: https://en.wikipedia.org/wiki/Quadtree
[2]: https://tools.ietf.org/html/rfc7946
[3]: https://tools.ietf.org/html/rfc7946#section-3.3
[4]: https://overpass-turbo.eu/s/E9v
