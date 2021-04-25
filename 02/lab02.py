# #!/usr/bin/env python3

"""
Kód ke cvičení #2 z NPRG030.
Kód nemá fungovat jako celek a nemusí být kompletní.
Jednotlivé části kódu byly postupně vysvětleny na cvičení.
"""

# ============
# FORMÁTOVÁNÍ
# ============

city = "Praha"
temp = 15
speed = 8.6

# funkce print() může vytisknout více argumentů
print("Ve městě", city, "je", temp, "stupňů a vítr fouká rychlostí", speed, "km/h")

# oddělovač můžeme změnit
print("Ve městě", city, "je", temp, "stupňů a vítr fouká rychlostí", speed, "km/h", sep="|")

# většinou je ale lepší string formátovat, a to buď pomocí metody format()
s = "Ve městě {} je {} stupňů a vítr fouká rychlostí {} km/h"
print(s.format(city, temp, speed))

# nebo přímo přes f-stringy
s = f"Ve městě {city} je {temp} stupňů a vítr fouká rychlostí {speed} km/h"
print(s)

# v Pythonu 2 se formátovalo jinak, ale tento způsob už by se neměl používat
s = "Ve městě %s je %d stupňů a vítr fouká rychlostí %f km/h" % (city, temp, speed)
print(s)

# s metodou .format() i s f-stringy můžeme používat různé formátovací značky a text (nejen) zarovnávat
print(f"{speed:.2f}")
print(f"{speed:.5f}")
print(f"{speed:06.1f}")
print(f"{temp:5d}")

# od Pythonu 3.8 můžeme jednoduše vypisovat název proměnné společně s její hodnotou
print(f"{speed=}")

# ============
# DĚLENÍ
# ============

# čísla můžeme dělit nejen ve floatech
a = 5 / 2

# ...a následně zaokrouhovat
b = round(a)

# ale i celočíselně
c = 5 // 2

# a také zjišťovat zbytek
d = 5 % 2

# ============
# STRINGY
# ============

# string je řetězec znaků
s = "abcde"

# Python 3 používá Unicode, proto můžeme používat téměř libovolné znaky
s1 = "ň"
s2 = "😄"
s3 = "て"

# porovnávání stringů porovnává postupně Unicode hodnoty znaků
print(s1 < s2)

# ...které můžeme zjistit pomocí vestavěné funkce ord()
print(ord(s1))
print(ord(s2))
print(ord(s3))

# ============
# LISTY
# ============

# listy můžeme vytvořit dvěma způsoby
l1 = []
l2 = list()

# přes syntaxi [] můžeme list rovnou i nainicializovat
l1 = [0, 1, 2, 3, 4, 5]

# přes list() můžeme vytvořit list z jiného iterovatelného objektu
r = range(6)
l2 = list(r)

# list můžeme vytvořit i ze stringu pomocí funkce split(), separátor je defaultně mezera (lze změnit)
s = "Hello world"
l3 = s.split()
print(l3)

# pokud chceme dělit po znacích, musíme opět použít list()
l4 = list(s)
print(l4)

# znaky můžeme opět spojit
# POZOR, .join() je metoda stringu, přes který spojujeme, a ne listu
print(",".join(l4))

# s listem jde dělat řada věcí
l1.append(6)         # přidávat prvky
l1.reverse()         # obracet pořadí prvků
print(l1.count(3))   # počítat výskyt konkrétních prvků
l1.clear()           # mazat všechny prvky

# ...a řadu dalších, které objevíme pomocí funkce dir()...
print(dir(l1))

# ...nebo v dokumentaci, případně na Stack Overflow ;)

# list můžeme také indexovat...
print(l2[0])        # první prvek, v Pythonu indexujeme od nuly
print(l2[4])        # pátý prvek
print(l2[-1])       # poslední prvek - můžeme využívat záporné indexy pro indexování odzadu 

l2[1] = 2           # přiřadí dvojku na druhé místo

# ...a používat nad nimi vestavěné funkce
print(min(l2))      # minimum
print(max(l2))      # maximum
print(len(l2))      # počet prvků

# ============
# FOR CYKLUS
# ============

# for ELEM in ITERABLE:
# v Pythonu se for cyklus chová jako "for each" - do proměnné ELEM postupně načítá prvky z ITERABLE
# iterable je například list
for elem in l2:
    print(elem)

# indexy můžeme získat pomocí funkce enumerate()
for i, elem in enumerate(l2):
    print(i, elem)

# cyklus můžeme předčasně ukončit pomocí příkazu break
for elem in l2:
    print(elem)
    if elem >= 3:
        break

# a iteraci můžeme přeskočit pomocí příkazu continue
for elem in l2:
    if elem == 3:
        continue
    print(elem)
