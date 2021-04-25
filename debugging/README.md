# Tipy: Jak efektivně odladit program

Programátorům<sup>1</sup> se občas stane, že dostanou za úkol vytvořit program, který má dávat nějaké výstupy na základě zadaných vstupů, a navíc na to dostanou málo času. Tedy, občas... chtěl jsem říct *vždycky*.

Takový program většinou není složitý z pohledu algoritmizace. Když se v programu nějaký zajímavý algoritmus vyskytne, tak na něj navíc často už existuje specializovaná knihovna.

Program ale je potřeba správně navrhnout, naimplementovat a otestovat – což pořád rozhodně není nic, co by uměl každý programátor-začátečník. Je na to potřeba kreativní myšlení, schopnost abstrakce, znalost konkrétního programovacího jazyka, zručnost v práci s programovacím prostředím a odolnost vůči stresu. Dobrou zprávou ale je, že všechno se dá naučit a potrénovat.

Zápočtový test je takovým simulátorem běžné práce programátora. Ačkoliv to tak na první pohled nevypadá, úkolem zápočtového testu není studenty vystresovat, ale naučit je psát a ladit programy efektivně a tím jim ušetřit stres v budoucnu.

Tento návod obsahuje pár tipů, jak na to. Není potřeba se ho držet doslovně, ale je to odrazový můstek pro ty, co chtějí programovat trochu méně živelně. Návod obsahuje pár konkrétních tipů k programování v Pythonu s Visual Studio Code a odevzdávání úloh do ReCodExu, většina rad ale platí při programování obecně. 

<sup>1</sup>*a programátorkám, kterým se tímto omlouvám, že budu pro přehlednost používat jen mužský rod*

## Postup psaní kódu

### Fáze 1 – Čtení zadání
*= pochopit, co se ode mě chce*

Radu "čti pořádně zadání" už jste určitě slyšeli. Už jen kvůli tomu, že na konci může být napsáno *"kdo jste dočetli až sem, napište do chatu 'jsem ryba' a nemusíte nic programovat"*, se to vyplatí. Mnohem spíš je to ale dobré kvůli tomu, že v každém zadání se skrývá pár konkrétních vět, které je dobré mít na paměti.

Důkladné čtení zadání vám navíc pomůže udělat si představu o podobě programu. Zadání není potřeba umět odříkat zpaměti, ale udělat si v paměti "záložky", ke kterým je pak možné se vracet.

### Fáze 2 – Návrh programu
*= promyslet, jak úkol splním*

Po prvním čtení zadání je dobré se vrátit v zadání k zásadním bodům a začít přemýšlet nad strukturou programu. Může stačit vnitřní monolog ve stylu: *"Ok, tady mi přijde seznam položek, tak ho načtu do listu... Aha, ještě k nim budu muset přiřadit hodnoty, tak to radši rovnou uložím do slovníku."* U složitějších programů je ale dobré se naučit načrtávat diagramy. (Ačkoliv se vám softwaroví inženýři budou snažit namluvit něco jiného, na naprostou většinu diagramů stačí text, obdélníčky a šipky).

Existují soutěže, ve kterých se programátoři snaží napsat kód co [nejkratší](https://js1k.com), případně co [nejnepřehlednější](https://www.ioccc.org). Kód, který programátoři píšou v podobném stylu i v reálném životě, ale skončí mnohem spíš na [této stránce](https://shitcode.net), nebo ukrytý hluboko v uzavřených kódech korporátních programů (navíc jejich kód narozdíl od těchto soutěží nemá žádnou přidanou uměleckou hodnotu).

Zásadní pro úspěch<sup>2</sup> programu v reálném světě je rozdělení programu do souborů, objektů a/nebo funkcí. V případě programů malého rozsahu toho dělení nebude moc, záleží taky na vybraném paradigmatu a programovacím jazyce. Je ale dobré pamatovat na to, že nějaká struktura by v programu být měla – ne proto, že vám to říká nějaký návod, ale proto, že se vám nad programem bude v praxi o dost lépe přemýšlet.

Většinou se stačí držet pravidla, že byste se kód měli snažit rozdělit na co **nejmenší** funkční celky. Pokud část kódu dělá jednu přesně definovatelnou věc, je to dostatečný důvod kód oddělit do funkce. Pokud by se kód měl opakovat (i kdyby jen jednou), je to taky důvod kód oddělit do funkce. Pokud z bloku kódu na první pohled nepochopíte, co má dělat, je to důvod ho rozdělit do víc funkcí.

Možná si říkáte: *"Jasně, až budu psát opravdovej kód, tak si budu hrát na funkce a objekty. Přece to ale nebudu dělat, když potřebuju ušetřit čas a nikdo to po mně číst nebude."* Jenže kód, který funguje hned napoprvé, je velká vzácnost. A není nic horšiho, než v debuggeru zírat na seznam dvakrát zanořených n-tic a přemýšlet, na jakém indexu je co schované.

<sup>2</sup> *úspěšný program (adj.,n.) = 1) program projde v ReCodExu; 2) program pochopí autor i po roce; 3) kolega, který dostal za úkol program po autorovi rozšířit, nemá chuť autora nakopnout.*

### Fáze 3 – Prototyp
*= napsat kód, který má šanci fungovat*

Teprv v této fázi by měl programátor poprvé začít psát kód. Na samotné psaní kódu určitě existuje víc názorů, ale osobně doporučuju program psát po minimálních funkčních celcích. Neboli řečeno laicky – "blbuvzdorně". Tento postup poskytuje záruku asymptoticky lineárního množství chyb – když každý celek odladíte, co nejdřív to jde, chyby vám nezačnou interagovat navzájem.

Takový první minimální funkční celek je **načtený vstup**. Načíst vstup sice vypadá jako něco triviálního, co sfouknete zároveň se zbytkem. Jenže v každé části kódu se dají udělat chyby a načítání kódu není výjimka. Dobré je, že je tahle část se dá poměrně jednoduše odladit – stačí si do programu vstup poslat (víc o tom v další sekci) a vypsat si ho. Začít obyčejným načtením vstupu vlastně stejná rada, jakou si přečtete v seberozvojových příručkách proti prokrastinaci: *začněte – jakkoliv, ale hlavně začněte*. 

Podobně jednoduše se dá připravit **výpis výstupu**. Jak na to, když žádný výstup ještě nemáte? Z minulého kroku máte minimálně vstup, a ten se dá prozatím poslat na výstup beze změny. To vám navíc dá skvělou příležitost si připravit kostru programu:

```python

def naparsuj_vstup(vstup):
    # TODO
    return vstup

def zpracuj(x):
    # TODO
    return x

def spocitej_vystup(y):
    # TODO
    return y 


# načítání vstupu
vstup = input() # ...

# hlavní část programu
x = naparsuj_vstup(vstup)
y = zpracuj(x)
vystup = spocitej_vystup(y)

# výpis výstupu
print(vystup)
```

Takto napsaný program zatím nedělá nic moc užitečného, má ale dvě výhody: 1) dá se spustit a něco vypisuje (což je takový záchytný bod) a 2) poskytuje vám způsob, jak přemýšlet nad  implementací zbytku programu. Konkrétně v tomto případě stačí implementovat funkce `naparsuj_vstup()`, `zpracuj()` a `spocitej_vystup()`. A to už nezní tak náročně, ne?

Funkce se následně snažte postupně psát a zároveň testovat jak na běžícím páse. Neustálé testování úplně čehokoliv je základem rychlého odladění programu. V programu je většinou několik mezikroků, které se dají přehledně vypisovat. Pokud jste si program v přechozí fázi dobře rozvrhli, jednotlivé kroky vás budou postupně přibližovat k cíli. Navíc byste v každý okamžik měli mít dost přesnou představu, kolik vám toho ještě zbývá a jak jste na tom s časem.

Tato fáze končí ve chvíli, kdy vám program vypíše správný výstup pro ukázkový vstup.

### Fáze 4 – Testování
*=dotáhnout věci do konce*

*"Hurá, mám vyhráno!"*. Optimismus je skvělá vlastnost do života, u psaní programu se ale vyplatí spíš skepse a podezřívavost. *"To šlo nějak moc jednoduše"* je bohužel často mnohem blíž k pravdě. Na tuto fázi si proto nechte dostatečné množství času.

Že program funguje "jen tak na oko" vám ve škole řekne ReCodEx, v praxi pak na to přijde nějaký tester nebo se to dozvíte z produkčních logů. Žádný případ není ideální a nejlepší způsob (hned po psaní programů bez chyb) je umět programy testovat. Na to dám pár tipů v následující sekci.

Jakmile vám pak program prochází všemi myslitelnými testy, tak nastávají tři možnosti:
1. program stále nefunguje, a to proto, že jsou špatně testy jinde (např. v ReCodExu) → otestovat, např. dotazem
2. program stále nefunguje a jinde jsou testy 100% správně, takže jste asi přece jen na nějaké testy zapomněli → nevzdávat se a ladit dál
3. máte doopravdy vyhráno → **hurá!**


## Praktické tipy

### Ladění s jedním vstupem
Pro fáze 1-3 stačí většinou jeden vstup, který je buď jednoduchý, nebo reprezentativní (ideálně obojí). Takový vstup máte už většinou přímo v zadání. Pokud ne, určitě se vyplatí si ho vytvořit.

Jak vstup do programu zadávat? Pokud program čte ze souboru, je řešení přímočaré – soubor si vytvoříte a vstup uložíte do něj. Pokud program čte ze standardního vstupu, máte v zásadě dvě možnosti:

1. Uložit vstup do souboru a soubor přesměrovat na standardní vstup. Za předpokladu, že spouštíte pythoní program `muj_program.py` a vstup máte uložený v souboru `vstup.txt` ve stejné složce, můžete použít následující příkaz (funguje stejně na všech operačních systémech):
```
python3 muj_program.py < vstup.txt
```
Viz také [8. cvičení](../08/README.md).

2. Starý dobrý copy-paste. Kopírovat ze zadání můžete přes Ctrl+C, v terminálu / VS Code pak funguje na vkladání zkratka Ctrl+Shift+V (případně klik pravým tlačítkem myši). Odřádkování není třeba se bát, vkládat můžete i víc řádků najednou.

### Testování s více soubory
Ve fázi 4 se už pak vyplatí mít způsob, jak pouštět testy automatizovaně. Často se totiž stane, že jakmile opravíte chybu v jednom testu, neprojde vám kvůli tomu jiný test. Nejlepší způsob, jak program rychle odladit, je proto jednoduše pouštět testy všechny naráz.

Z všech možných metod doporučím metodu s přezdívkou *"ReCodEx simulátor"*. Postup je následující:

1. Vytvořte složku `testy`.
2. Ve složce `testy` vytvořte soubory `1.in`, `2.in`, `3.in`... pro každý vstup, který chcete otestovat. Vstupy vymyslete tak, aby na nich bylo něco zajímavého – okrajové hodnoty, triviální případy, atd. Jeden test může samozřejmě být i testovací vstup používáný při ladění programu.
3. Zároveň ve složce `testy` vytvořte soubory `1.out`, `2.out`, `3.out`... – to budou referenční výstupy pro každý vstup. Výstupy ideálně napište a zkontrolujte ručně, podobně jako vstupy. Pokud zatím přesně nevíte, co má být výstupem (proto ostatně píšete program), tak ho můžete nechat zatím prázdný, ale jakmile vám výstup z programu přijde smysluplný, tak ho tam přidejte (výstup se může během ladění rozbít).
4. Testy pouštějte automatizovaně skriptem. Nejpřirozenější je na to skript v shellu (přikládám příklad [v bashi](run_tests.sh)), případně si může posloužit i [skript v Pythonu](run_tests.py), který by měl fungovat napříč OS. Pozor, skripty je potřeba upravit v případě, že program čte ze souboru: v tom případě doporučuju testem přepsat vstupní soubor.


Pokud vám takový přístup nevyhovuje, existují i další (standardnější) přístupy: např. napsat si testovací funkce `test_X()`, `test_Y()`, ..., do nich si přímo zapsat vstupy a kontrolovat výstupy přes funkci `assert`, případně rovnou používat specilizovaný testovací balíček `unittest`. Takový postup se vám bude určitě hodit v praxi u nějakého komplexního softwaru. Výše zmíněný přístup mi ale přijde nejčistší a zároveň nejefektivnější pro jednoduché programy, obzvlášť pokud už máte testovací skript předem připravený a vyzkoušený.

### Debugování
Jakmile nefunguje nějaký test, je podobně důležité rychle zjistit, v čem je chyba a jak ji opravit.


#### Debugger
Debugger umožňuje zastavit v libovolný moment provádění programu a prozkoumat stav proměnných a systémového zásobníku. Program se zastaví na tzv. breakpointu, který nastavíte na konkrétní řádek v kódu. Od breakpointu můžete následně program posunout na další řádek, do prováděné funkce, případně na další breakpoint. Umět rychle a efektivně používat debugger se každému programátorovi rozhodně vyplatí. 

V Pythonu je vestavěný debugger `pdb`, který se ovládá přímo v příkazové řádce. Je to dobrá alternativa pro ty, kterým nevyhovuje těžkotonážní debugger v IDE. Velkou výhodou je, že na spuštění debuggeru stačí přidat do kódu řádek `import pdb; pdb.set_trace()` a můžete program spoustět stejně jako v normálním módu (bez "Start debugging" apod.). Např. pro Sublime Text existuje [plugin](https://packagecontrol.io/packages/Python%20Breakpoints), který breakpoint přidá / odebere pomocí klávesové zkratky. Pokud se chcete o `pdb` dozvědět víc, doporučuju projít [tutorial](https://realpython.com/python-debugging-pdb/) (a následně zkoušet a zkoušet...).

Pokud používáte VS Code, můžete využít jeho [debugger](https://code.visualstudio.com/docs/editor/debugging) (*Run → Start Debugging*). Breakpointy v něm přidáváte a odebíráte jednoduše kliknutím do prostoru vlevo od řádku (kde se zobrazí červené kolečko). Jeho výhodou je přehledné klikací prostředí s panelem pro debugování, ve kterém vidíte najednou hodnoty všech proměnných, krokování pomocí tlačítek atd.. Jeho nevýhodou je, že se nedá přímočaře spustit z příkazové řádky, což komplikuje práci v případě, když chcete program zároveň z příkazové řádky automaticky testovat nebo mu zadávat další argumenty. Pokud se chcete touto cestou vydat, je dobré si nastudovat, jak debugger [konfigurovat](https://code.visualstudio.com/docs/python/debugging). Klíčový je argument `"args"` v konfiguraci, přes který je možné programu zadávat argumenty, případně se přes něj dá [menším hackem](https://stackoverflow.com/questions/59060237/how-to-setup-visual-studio-code-stdin-stdout-redirection-for-python-debugger) i přesměrovat vstup a výstup. Lepší je možná ale v tomhle případě se vydat cestou testů přímo v kódu.


#### Výpisy

Občas místo debuggeru stačí pár vhodně umístěných printů. Obvzlášť se to vyplatí v situacích, kdy chcete naráz vidět víc hodnot, např. jak se vyvíjí nějaká proměnná během cyklu (a nechcete program krokovat). Od Pythonu 3.8 můžete využít syntax `f"{var=}`, kterým vypíšete název proměnné `var` společně s její hodnotou. 

Nezapomeňte výpisy zase skrýt ve finální verzi programu. Může se vyplatit si napsat oddělenou funkci `log()`, která se dá jednoduše vypnout, zatímco `print()` s výstupem zůstane funkční.



### Co nedělat
- **NE: Hardcodovat vstup**, aneb napsat si vstup jako konstanty přímo do programu. Jednak ztratíte čas přepisováním vstupu, jednak pak skoro jistě nějakou tu konstantu v programu zapomenete a program pak nebude na obecných vstupech fungovat.
- **NE: Testovat přes ruční psaní vstupu.** Pokud nejde jen o jedno číslo, tak tím ušetříte čas poprvé, možná podruhé, ale při třetím testu už budete litovat, že jste nezvolili nějakou efektivnější metodu.
- **NE: Panikařit, mlátit do klávesnice, rozbíjet monitor...** Je to kontraproduktivní a prodraží se to. S přístupem ke kódu se dá všechno vydebugovat. Zkuste se pořádně podívat na chybovou hlášku a vypátrat, kde k chybě dochází. Většinou se dá postupně propracovat k řádku, který za to může. Případně zkuste zakomentovat část kódu a vrátit se tím nazpět do stavu, kdy program zaručeně fungoval, následně se postupovat po malých krocích dopředu. Pokud padají nějaké testy a nevíte jaké, testujte všechny případy, co můžou podle zadání potenciálně nastat. Pokud váš program spadl s výjimkou, ReCodEx ji vypíše (např. `IOError` pravděpodobně znamená, že otevíráte špatný soubor). Občas se u ReCodExu může vyplatit i na určitém podezřelém místě chybu vyvolat (např. `raise ValueError`) a něco usoudit na základě toho, jestli se ve výpisu chyba objeví nebo ne.


Přeju do budoucna co nejmíň stresu a hodně úspěšných testů!