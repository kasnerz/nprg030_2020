# Cvičení č. 2 – 9.10.2020

## Domácí úlohy

*   vyhodnocování v ReCodExu - testy vstupů a výstupů; výstup musí přesně odpovídat referenci
*   `input()` vždy načte string, porovnávání stringů postupně porovnává pozice znaků v [Unicode](https://www.ssec.wisc.edu/~tomw/java/unicode.html)
    *   funkce `ord()`
*   používání vestavěných funkcí - v pořádku (ale mít představu, jak jsou implementované)

## Algoritmizace

*   vztah mezi časovou a paměťovou složitostí
    *   časová složitost je vždy vyšší nebo stejná, než paměťová složitost - vždy strávíme čas alespoň načítáním dat do paměti
*   [převody](https://matematika.cz/prevod)
    *   z desítkové soustavy do dvojkové
    *   z dvojkové soustavy do desítkové
*   důkaz, že binární vyhledávání má časovou složitost log(N), kde N je počet prvků v seřazeném poli
*   vyhledávání v seřazeném poli nekonečné velikosti  - [exponential search](https://www.geeksforgeeks.org/exponential-search/)
*   [interpolation search](https://www.geeksforgeeks.org/interpolation-search/) - hledání s časovou složitostí log(log(N)), pokud jsou prvky v poli nejen seřazené, ale i rovnoměrně rozložené

## Programování
*   [print() a formátování stringů](https://www.programiz.com/python-programming/methods/built-in/format): separator, `.format()`, f-strings
    *   modifikátory - počet desetinných míst, zarovnání
    *   `f"{var=}"` - nová syntaxe v Pythonu 3.8 pro výpis názvu a hodnoty proměnné
*   porovnávání floatů
*   komentáře - jednořádkový, víceřádkový
    *   kdy komentovat a kdy ne
    *   zakomentování kódu
*   celočíselné dělení `//` a modulo `%`
*   listy
    *   heterogenní prvky
    *   tvorba - `\[\]`, `list()`, `.split()`
    *   přístup k prvkům - `l\[index\]`, negativní indexy - odzadu
    *   `range(start, end)` - generování seznamu čísel
    *   `.append()`, `.clear()`, `.reverse()`, `.count()`
    *   `len(l)` - počet prvků v objektu
    *   `"".join(l)` - metoda stringu pro spojení listu
*   funkce `dir()` - vestavěné metody objektu, [magic methods](https://www.geeksforgeeks.org/dunder-magic-methods-python/)
*   `for` cyklus
    *   procházení iterovatelného objektu: `for elem in obj`
    *   funkce `enumerate()`: (index, prvek)
    *   `break` - předčasné ukončení cyklu
    *   `continue` - okamžitá další iterace
