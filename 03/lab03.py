#!/usr/bin/env python3

"""
Kód ke cvičení #3 z NPRG030.
Kód nemá fungovat jako celek a nemusí být kompletní.
Jednotlivé části kódu byly postupně vysvětleny na cvičení.
"""
# ============
# unicode
# ============
# znak můžeme nejen převádět na Unicode hodnotu...
ch = "a"
print(ord(ch))

# ...ale i naopak
code = 97
print(chr(code))

# ===============
# logické operace
# ===============
# nad výrazy můžeme provádět logické operace
a = 5
b = 7

# and: oba výrazy platí zároveň
if a < 5 and b < 5:
    print("Platí oba")
# or: platí alespoň jeden výraz (nebo oba zároveň)
elif a < 5 or b < 5:
    print("Platí alespoň jeden")

# s logickými hodnotami můžeme přímo pracovat
t = True
f = False

print(t and f)
print(t or f)

# ===============
# None
# ===============
# speciálním typem objektu je None...
obj = None

# ...třídy NoneType
print(type(obj))

# pozor, None není 0, False ani prázdný string...
print(None == 0)
print(None == False)
print(None == "")

# ...ale v podmínce se vyhodnotí na False
if obj:
    print("Funguje to")
else:
    print("Nefunguje to")

# jestli je objekt None kontrolujeme správně explicitně přes is (not) None
if obj is None:                     # (aka náš `obj` ukazuje na stejné místo v paměti, jako None)
    print("Náš objekt je None")
elif:
    print("V obj máme hodnotu")

# většinou se používá na označení prázdné návratové hodnoty, neinicializované proměnné apod.
l = [1, 2, 3, 4, 5]
print(l.append(6))      # prázdná návratová hodnota
var = None              # var existuje, ale neukazuje na žádný objekt (technicky ukazuje, ale pouze na None)

# None je schovaný např. ve slicingu listu:
l2 = l[1:]

# ...je to samé jako
l2 = l[1:None]

# což můžeme použít např. takto
start = 1
end = None
l2 = l[start:end]

# ===============
# konstanty
# ===============
# konstanty nepíšeme přímo do kódu:
if a == 42:
    print("Máme odpověď")

# ...ale snažíme se je vhodně pojmenovat ;)
answer = 42
if a == answer:
    print("Máme odpověď")

# ===============
# 2D pole
# ===============
# listy do sebe můžeme zanořovat, čímž vytvoříme 2D (3D, ...) pole
l = [[1,2], [3,4], [5,6]]

# indexujeme postupně - každý index z listu vrátí jeho prvek (tzn. na vnějším listu sublist, na vnitřním listu přímo hodnotu)
sublist = l[1]
elem = l[1][0]

# procházet 2D list můžeme např. pomocí dvou for cyklů
for sublist in l:
    for elem in sublist:
        print(elem, end=" ")
    print()

# ===================
# list comprehensions
# ===================
# často používaný způsob, jak vytvořit list a další
# iterovatelné objekty z jiných iterovatelných objektů
l1 = [1, 2, 3, 4, 5]
l2 = [x for x in l1]                # vytvoří kopii listu
l3 = [x+1 for x in l1]              # vytvoří list s prvky o jedničku vyšší
l4 = [x*x for x in l1]              # vytvoří list druhých mocnin
l5 = [x for x in l1 if x < 3]       # vyfiltruje prvky, které jsou menší než 3

# ===================
# tuples
# ===================
# tuple je seznam prvků podobně jako list
t = (1, 2, 3)

# ale narozdíl od listu je immutable - nemůžeme ji po vytvoření nijak změnit
t.append(4)         # vyvolá výjimku

# můžeme z ní ale list udělat
l = list(t)

# tuples se v Pythonu vyskutují často na nečekaných místech
# vrací nám je např. funkce enumerate()
for t in enumerate(["a", "b", "c"]):
    print(t)
    print(type(t))

# a můžeme je "zneužít" na výměnu hodnot prvků
a = 1
b = 2

b, a = a, b     # provede swap(a,b)


# ===================
# funkce
# ===================
# základ pro modularizaci a znovupoužitelnost kódu

def add(a, b):
    # vrátí součet dvou čísel a,b
    c = a + b
    return c

vysledek = add(1, 1)

# funkci můžeme argumenty předávat pozičně, ale i přes názvy parametrů
vysledek = add(a=3, b=1)

# parametry můžou mít tzv. defaultní (přednastavenou) hodnotu
def add_verbose(a, b, verbose=False):
    # vrátí součet dvou čísel a,b
    c = a + b

    if verbose:
        print(f"Sčítám {a} a {b}, vyšlo mi {c}")

    return vysledek
    
vysledek = add_verbose(a,b)
vysledek = add_verbose(a,b, verbose=True)