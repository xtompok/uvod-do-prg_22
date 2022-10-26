# Domácí úkol 1 - piškvorky

## Zadání
Napište hru piškvorky na 3x3 polích. Program nemusí umět vyhodnocovat, že nějaký
hráč vyhrál, ani kolizi v políčkách. Hráči zadávají souřadnice do konzole,
průběh hry je vykreslen želví grafikou.

### Vstup
Program bude interaktivní. Program se střídavě ptá jednoho a druhého
hráče na souřadnice tahu. Pokud hráč zadá platné souřadnice, program do daného
políčka zakreslí značku daného hráče, pokud zadá souřadnice mimo herní plán,
program hráče vyzve k novému zadání souřadnic, a to opakovaně, dokud hráč nezadá
platné. 

### Výstup
Po spuštění vykreslí čtvercovou síť 3x3 políčka. Délka strany políčka budiž
definována konstantou v programu. Po každém úspěšném zadání vykreslí program na
odpovídajících souřadnicích buď křížek (pro prvního hráče) nebo kolečko (pro
druhého hráče). 


# Další požadavky
Program může spadnout, pokud nelze převést souřadnice zadané uživatelem na
číslo. Program skončí po tolika tazích, kolik má herní plán políček. Program
nemusí umět vyhodnotit, že nějaký hráč vyhrál, ani že bylo zahráno do již
obsazeného pole.

### Doporučení
Pro načítání znaků použijte funkci `input`, pro převedení na čísla pak `float` a `int` 

Projděte si poznámky z cvičení, naleznete tam odpověď na mnoho ze svých otázek.

Projděte si [dokumentaci k modulu
`turtle`](https://docs.python.org/3/library/turtle.html), může se vám hodit
například funkce [`setpos`](https://docs.python.org/3/library/turtle.html).

Testujte aplikaci nejen na korektní, ale i nekorektní vstupy.

Odevzdejte úkol pár dní i týden dopředu, ať mám čas vám ho zkontrolovat a případně
vrátit k dodělání / přepracování. 

Pište aplikaci jednoduše, nevytvářejte zbytečné vzdušné zámky. 

Dodržujte princip "Nejprve načítám vstup a ověřuji, že je korektní, následně provádím výpočty"

Použijte Git či jiný verzovací systém, nebo si aspoň před tím, než smažete kus
kódu proto, že si myslíte, že je špatně, udělejte zálohu bokem.
 
Nebojte se zeptat. Pokud se na něčem zaseknete a nevíte, jak dál, klidně mi
napište, rád vám poradím.

### Odevzdání
Odevzdávat budete zdrojový kód projektu a soubor s dokumentací. Vše
bude zabalené v zip souboru, který bude obsahovat adresář `du1_jmeno_prijmeni`,
ve kterém bude soubor se zdrojovým kódem a soubor s dokumentací, tedy například:
```
du1.zip
|
\du1_tomas_pokorny
  |- dokumentace.md
  \- du1.py
```
Zip archiv mi pošlete mailem. 

Deadline bude 6.11. 8.03. Úkoly odeslané po deadlinu budou brány jako neodevzdané. Pokud
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

### Bodování
- 2 b za funkční program pro korektní vstupy
- 1 b za funkční program pro nekorektní vstupy
- 1 b za kvalitu kódu
- 1 b za komentáře v kódu
 
Kvalitou kódu se rozumí použití vhodných prostředků k dosažení cíle,
minimalizace opakujícího se kódu, vhodné odsazení a oddělení funkčních celků.
 
Komentáře v kódu jsou důležité, aby člověk, co si váš kód čte, získal přehled o
tom, co kód dělá. Nekomentujte každý řádek, ale jednotlivé funkční celky. 
Komentářů by mělo být výrazně méně než kódu.
 
Postup, jak domácí úkol napsat, spolu klidně konzultujte, ale kód pište každý
sám. Pokud objevím identické či nápadně podobné řešení, oboduji je jednou a body
rovnoměrně rozdělím mezi autory. 

## Bonusové body

Za různé nadstavby k zadání můžete získat bonusové body. Bonusové body se
počítají pouze tehdy, pokud bude program fungovat korektně včetně ošetření
všech nesprávných vstupů, i těch z bonusové části. Pokud je chyba pouze v
bonusové části (bude hodnoceno individuálně), pak se aplikace považuje za
funkční a propadají pouze body z bonusové části.

### Odevzdání před GitHub (1 b)

Pokud budete pro verzování používat Git, vytvořte si účet na
[GitHubu](https://github.com) nebo jiné podobné platformě a úkol můžete odevzdat
přes něj. Repozitář by měl obsahovat jak program, tak případný soubor s
dokumentací, za hodnocenou verzi se počítá poslední commit pushnutý na GitHub
před deadlinem. Pokud budete potřebovat pomoct, pište mi.

### Volitelná velikost hrací plochy (1 b)

Před vykreslením čtvercové sítě se program zeptá uživatele, kolik by měla mít
sloupců a kolik řádků a podle toho ji nakreslí. Hra pak probíhá na celé této
síti.

### Piškvorky na šestiúhelníkové síti (1 b)
Místo na čtvercové síti se hraje na šestiúhelníkové síti.
