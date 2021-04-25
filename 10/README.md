# Cvičení č. 10 – 4.12.2020

## Programování

- dokončení skupinové práce z [minulého cvičení](../09/README.md)
- [moje řešení úloh](geometry.py)


## Algoritmizace
Opakování z přednášky

### Grafy
- **graf**: `G = (V, E)`
  - V: množina vrcholů (resp. uzlů, jde o synonyma; angl. vrchol=vertex, uzel=node)
  - E: množina hran  (angl. edge)
  - hrana spojuje vždy **dva vrcholy** (jinak by to byl [hypergraf](https://cs.wikipedia.org/wiki/Hypergraf))
- **sled**: posloupnost vrcholů spojených hranou
- **tah**: sled, ve kterém se neopakuje žádná hrana
- **cesta**: tah, ve kterém se neopakuje žádný vrchol
- speciální typy grafů
  - **prázdný graf**: neobsahuje žádné vrcholy ani hrany
  - **úplný graf**: každé dva vrcholy jsou spojené hranou
  - **souvislý graf**: existuje cesta mezi libovolnými dvěma uzly
  - **bipartitní graf**: uzly můžeme rozdělit do dvou množin tak, že hrany vedou pouze mezi množinami

### Reprezentace grafu
- grafická reprezentace - pouze pro názornost
- matice sousednosti (vrcholy x vrcholy) - vhodné pro grafy s malým počtem vrcholů a velkým počtem hran
- matice incidence (vrcholy x hrany) - vhodné pro grafy s malým počtem hran
- seznam následníků - dynamická reprezentace - seznam (index = číslo uzlu), prvky seznamu jsou seznamy s indexy sousedních uzlů
  - pokud průměrný počet hran `m` vedoucí z jednoho uzlu je řádově menší, než celkový počet hran `M` (tzn. graf není úplný, ani k tomu nemá "blízko"), průchod grafem bude řádově rychlejší
  - v Pythonu jednoduchá implementace pomocí listů
- objektová reprezentace - podobné jako seznam následníků, ale uzly jsou objekty, která si drží odkazy na svoje sousedy
  - vhodná, pokud uzly nejsou jen čísla, ale obsahují další data


### Prohledávání grafu
- DFS - depth first search - prohledávání do hloubky
  - rekurzivně zavolám funkci `vypiš(uzel)` na všechny sousedy uzlu
  - jiná možnost: globální zásobník, všechny sousedy uzlu přidávám na zásobník a další uzel vybírám ze zásobníku
- BFS - breadth first search - prohledávání do šířky
  - globální fronta, všechny sousedy uzlu přidávám do fronty a další uzel vybírám ze fronty
  - prochází uzly postupně podle vzdálenosti od výchozího uzlu - při hledání cesty mezi uzly najde zaručeně nejkratší cestu
- u obou algoritmů si musím značit uzly, které jsem již otevřel (=navštívil, pokud jde o rekurzi, nebo přidal na zásobník / do fronty), a uzly již podruhé neotvírat

### Komponenty souvislosti grafu
- komponenta grafu: podgraf (podmnožina uzlů a hran mezi těmito uzly), který je souvislý
- hledání komponent souvislosti
  - postupně pouštím algoritmus prohledávání na všechny dosud neobarvené uzly
  - všechny uzly jsou na začátku neobarvené
  - algoritmus prohledávání obarví všechny uzly, které navštíví 
  - při každém spuštění algoritmu prohledávání na dosud neobarveném uzlu použiju novou barvu (=nové id komponenty)
  - jakmile nezbývá žádný neobarvený uzel, všechny uzly stejné barvy tvoří jednu komponentu