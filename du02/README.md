# Domácí úkol 2 - průměrné sedmidenní a roční průtoky

## Zadání
Napište program, který načte historická data o průměrných denních průtocích a
spočítá roční a sedmidenní průměry. Program bude neinteraktivní. 

### Vstup
Program načte CSV s průměrnými denními průtoky zvolené řeky ze souboru pojmenovaného `vstup.csv`.
Data můžete stahovat ze [stránek
ČHMÚ](https://www.chmi.cz/historicka-data/hydrologie/denni_data/denni-data-dle-z.-123-1998-Sb#). 
Pokud vstup nemá délku násobek sedmi, tak poslední průměr program spočítá z
tolika dat, kolik je k dispozici. Formát souboru je popsán v souboru obsahujícím
řetězem `Metadata` ve staženém archivu, pro všechny toky a místa je stejný.

#### Příklad vstupu
```
139000,QD,1980,11,01,   0.6700
139000,QD,1980,11,02,   0.6700
139000,QD,1980,11,03,   0.6700
139000,QD,1980,11,04,   0.6700
139000,QD,1980,11,05,   0.6700
139000,QD,1980,11,06,   0.6700
139000,QD,1980,11,07,   0.6700
139000,QD,1980,11,08,   0.6700
139000,QD,1980,11,09,   0.6700
139000,QD,1980,11,10,   0.6700
139000,QD,1980,11,11,   0.5800
139000,QD,1980,11,12,   0.5800
139000,QD,1980,11,13,   0.5800
139000,QD,1980,11,14,   0.5800
139000,QD,1980,11,15,   0.5800
139000,QD,1980,11,16,   3.2700
139000,QD,1980,11,17,   3.0000
```

### Výstup
Program vytvoří 2 CSV soubory se stejným formátem, jako má vstupní soubor.

První, pojmenovaný `vystup_7dni.csv` bude obsahovat sedmidenní průměry vstupních
dat, datum bude uvedeno vždy prvního dne z úseku, který se průměruje, průtok
bude průměrem průtoků prvního až sedmého dne úseku, zaokrouhleným na 4 číslice
za desetinnou tečkou. 

Druhý, pojmenovaný `vystup_rok.csv` bude obsahovat roční průměry vstupních dat,
datum bude uvedeno vždy první den z daného roku, kdy byla změřena nějaká data
(tedy pokud první data roku 1995 jsou z 4.5., tak datum u roku 1995 bude
4.5.1995). Průměrný průtok bude opět zaokrouhlen na 4 číslice za desetinnou
tečkou.

Pro základní verzi programu předpokládejte, že data nejsou děravá, tedy že
žádný den nechybí.

#### Příklad výstupu (sedmidenní)
```
139000,QD,1980,11,01,   0.6700
139000,QD,1980,11,08,   0.6185
139000,QD,1980,11,15,   2.2833
```


## Další požadavky
Program by měl ošetřovat všechny obvyklé výjimky a měl by o nastalém problému
informovat uživatele. Program by neměl vyžadovat nic zadávat od uživatele.
Program může vypisovat informace do konzole, ale tyto by měly být stručné a
pochopitelné pro uživatele programu, který nemusí umět programovat.

## Doporučení
Napište si funkce na jednotlivé kroky, případně si rozdělte kroky na podkroky a
opět si na ně napište funkce.

Testujte program nejen na korektní, ale i na nekorektní vstupy. Při předčasném
odevzdání se převážně zaměřuji na ty problémy, které si neumíte snadno odhalit sami.

Vytvořte si kratší vzorek dat, na kterém budete testovat, abyste nebyli zahlceni
ladícími výpisy. Vytvořte si i chybná data, ať víte, že na ně program korektně
zareaguje.

Přečtěte si [doporučení k minulému úkolu](../du01/README.md), zůstávají stále
platná.

Pokud si nejste jistí, jak interpretovat zadání nebo vám nějaká část přijde nejednoznačná, neváhejte se zeptat.

## Odevzdání
Odevzdávat budete zdrojový kód projektu a soubor s dokumentací. Vše
bude zabalené v zip souboru, který bude obsahovat adresář `du02_jmeno_prijmeni`,
ve kterém bude soubor se zdrojovým kódem a soubor s dokumentací, tedy například:
```
du02.zip
|
\du02_tomas_pokorny
  |- README.md
  \- du2.py
```
Zip archiv mi pošlete mailem. 

Deadline bude 11.12.2022 8.03. Úkoly odeslané po deadlinu budou brány jako neodevzdané. Pokud
odevzdáte úkol vícekrát, budu hodnotit poslední odevzdání před deadlinem.
Každému, kdo mi pošle úkol, odpovím, že jsem ho přijal a že se mi podařilo zip
rozbalit. Pokud neodpovím, urgujte.

Detaily pro odevzdání přes GitHub viz sekce *Odevzdání přes GitHub*.

### Předčasné odevzdání
Pokud odevzdáte úkol dopředu, zkusím se na něj podívat a napsat vám případné
nedostatky. Tato možnost není garantovaná, ale budu se snažit odbavovat úkoly co
nejrychleji. Zaručuji vám pouze to, že na úkoly se budu dívat v tom pořadí, v
jakém mi budou doručeny. Rovněž nezaručuji, že najdu v programu všechny chyby
napoprvé, tudíž pokud si nějaké nevšimnu, není to garance, že máte program
správně, závazné je pouze hodnocení po deadlinu. Pokud budete odevzdávat přes
GitHub, chyby vám vystavím jako Issue.

## Bodování
 * 3 b za funkční aplikaci
 * 2 b za dokumentaci a kvalitu kódu

Kvalita kódu zahrnuje i vhodné použití komentářů.

## Bonusové body

### Používání Gitu pro vývoj (1 b)
Pokud budete pro verzování používat Git, vytvořte si účet na GitHubu nebo jiné
podobné stránce a úkol můžete odevzdat přes něj. Kromě samotného odevzdání je
třeba, aby byl repozitář používán i pro vývoj, tedy by měl obsahovat průběžně
commitovanou práci. Repozitář by měl obsahovat jak program, tak případný soubor
s dokumentací, za hodnocenou verzi se počítá poslední commit pushnutý na GitHub
před deadlinem. Repozitář nemusí, ani by neměl, obsahovat velká vstupní data.
Pokud budete potřebovat pomoct, pište mi.

### Výpis maximálního a minimálního průtoku (1 b)
Program na konci do konzole vypíše data a hodnoty, kdy byl v datové sadě průtok
maximální a kdy byl průtok minimální a jaký tento průtok byl.

### Detekce děr a chyb v datech (1 b)
Program při zpracování kontroluje, jestli v datech nechybí nějaký den, nebo se
neobjevil nulový nebo záporný průtok. Program vypíše, které dny v datech chyběly
a ve kterých dnech došlo k nulovému nebo zápornému průtoku.

### (Bez)Chybné vstupy (2 b)
Navrhněte korektní nebo nekorektní vstupní soubor, se kterým by se program měl
vyrovnat, popiště jakým způsobem je správně / špatně a dodejte k němu vzorové
výstupy (pokud to dává smysl). Já vstup projdu a pokud ho uznám za vhodný a
ještě stejný druh nikdo před vámi neposlal, tak ho zveřejním na stránce [Chybné
vstupy](chybne_vstupy.md). Deadline je 4.12. 8.03. Pokud ho váš program úspěšně
zpracuje, tak dostanete 0,25 bodu za program každého spolužáka, který ho úspěšně
úspěšně nezpracuje, max 2 body. Pokud na něm váš program selže, nezískáváte nic.
Dodané vstupy budu průběžně zveřejňovat, nejpozději budou všechny zveřejněny
5.12. 23:59. K danému vstupu dodejte informaci, jestli se jedná o vstup pro
základní nebo rozšířenou verzi s povolenými děrami v datech.
