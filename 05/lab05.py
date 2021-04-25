#!/usr/bin/env python3

"""
Kód ke cvičení #5 z NPRG030.
Kód nemá fungovat jako celek a nemusí být kompletní.
Jednotlivé části kódu byly postupně vysvětleny na cvičení.
"""

# ===================
# množiny
# ===================

# množina (set) je datová struktura, která obsahuje každý prvek pouze jednou
# množinu vytvoříme pomocí set()
s1 = set()

# ...případně ji můžeme rovnou nainicializovat pomocí složených závorek
s2 = {1, 2, 3, 4}

# množinu můžeme procházet např. pomocí for cyklu
for elem in s2:
    print(elem)

# ale neměli bychom se spoléhat na pořadí prvků
# množinu nelze ani indexovat
print(s2[0])    # TypeError: 'set' object is not subscriptable

# do množiny můžeme přidávat prvky pomocí .add() (pozor, ne .append() jako u listu)
s2.add(5)

# prvek se můžeme "beztrestně" pokusit přidat i podruhé, prvek se pouze do množiny nepřidá
s2.add(5)

# s množinami se dají dělat podobné věci jako s listem
s2.remove(3)                # odstranění prvku
print(len(s2))              # délka

# ...ale i nějaké věci specifické pro množiny
s3 = {4, 5, 6, 7}
s4 = s2.union(s3)           # sjednocení
s5 = s2.intersection(s3)    # průnik

# ===================
# slovníky
# ===================

# slovník (`dictionary`) je datová struktura, která poskytuje přístup k hodnotám pomocí klíčů
# (množina byla vlastně specifickým případem slovníku, obsahujícím pouze hodnoty)
# slovník vytvoříme pomocí dict()
d1 = dict()

# nebo pomocí složených závorek (-> pozor, prázdné složené závorky vytvoří slovník a ne množinu)
d2 = {}

# ...případně slovník můžeme rovnou i nainicializovat
prices = {
    "mrkev" : 20,
    "cibule" : 10,
    "česnek" : 30
}

# prvky do slovníku přidáváme přiřazením hodnoty ke klíči
prices["ředkvičky"] = 15

# k hodnotám ve slovníku přistupujeme přes klíče
print(prices["mrkev"])

# ...které si můžeme vypsat pomocí .keys()
print(prices.keys())

# ...podobně jako hodnoty pomocí .values()
print(prices.values())

# slovník můžeme také procházet pomocí for cyklu
# metoda .items() vrací postupně n-tice (klíč, hodnota)
for key, value in prices.items():
    print(f"{key} stojí {value} Kč/kg")


# ===================
# defaultdict
# ===================

# občas se může hodit slovník, co má pro každý klíč implicitní hodnotu, např. nulu
# pythoní slovník tohle v základu neumí
d3 = {}

d3["pórek"] += 1  # KeyError: 'pórek'

# můžeme ale použít strukturu `defaultdict` z modulu collections
from collections import defaultdict

d3 = defaultdict(int)
d3["pórek"] += 1

# implicitní hodnota závisí na parametru předaném v konstruktoru
# pokud předáme např. list, můžeme pro každý klíč rovnou přidávat prvky do listu
d4 = defaultdict(list)
d4["nákupní seznam"].append("celer")


# ===================
# textové soubory
# ===================

# od práce se soubory nás odstiňuje operační systém - nemůžeme do nich proto přímo zapisovat nebo z nich číst
# každý soubor je proto potřeba nejprve otevřít pomocí open()
f = open("test.txt", "w")

# a na konci i zavřít pomocí close()
f.close()

# na zavírání se ale často zapomíná, v systému pak zůstávají viset otevřené popisovače souborů (file handles)
# také se může stát, že se obsah ani nezapíše a zůstane v bufferu
# proto pro otevírání souborů používáme kontextový manažer s klíčovým slovem `with`
with open("test.txt", "w") as f:    
    f.write("a")

# (všimněte si, že soubor nemusíme zavírat - kontextový manažer ho automaticky zavře na konci bloku)

# soubor můžeme otevřít v různých módech
# "w" = write, otevíráme nový soubor pro zápis
with open("test.txt", "w") as f:    
    f.write("test")

# "a" = append, otevíráme nový/existující soubor pro zápis a přidáváme obsah na konec souboru
with open("test.txt", "a") as f:    
    f.write("test")

# "r" = read, otevíráme soubor pro čtení (defaultní mód, "r" můžeme i vynechat)
with open("test.txt", "r") as f:    
    data = f.read()

# do souboru můžeme zapsat buďto string pomocí .write()...
content = "abc\ndef\nghi"

with open("test.txt", "w") as f:    
    f.write(content)

# ...případně list s jednotlivými položkami pomocí .writelines()
lines = ["abc\n", "def\n", "ghi\n"]     # pozor, stále musíme specifikovat '\n' jako konec řádku

with open("test.txt", "w") as f:    
    f.writelines(lines)
# (všimněte si, že ve write-módu si soubor pokaždé přepíšeme)

# obdobně funguje i čtení přes .read() a .readlines()
with open("test.txt") as f:         # mód "r" můžeme vynechat
    content = f.read()
    lines = f.readlines()

# proměnné vytvořené uvnitř `with` bloku můžeme používat i mimo blok
print(content)
print(lines)    # ale pozor, v `lines` nic není - pomocí read() jsme již posunuli čtecí hlavu až na konec souboru

# soubor je od Pythonu 3 automaticky uložen / načten v kódování utf-8, ale můžeme specifikovat i jiná kódování
with open("test.txt", "w", encoding="ISO-8859-2") as f:    
    f.write("ěščřžýáíé")


# ===================
# třídění v Pythonu
# ===================

# list můžeme setřídit pomocí metody .sort(), která používá algoritmus TimSort
l = [6, 3, 4, 5, 1, 2, 2]
l.sort()
print(l)

# někdy se hodí ponechat list v originálním stavu a pracovat se setříděnou kopií listu
# to nám umožňuje vestavěná funkce sorted()
l2 = [6, 3, 4, 5, 1, 2, 2]
print(sorted(l2))
print(l2)

# vše, co následuje, funguje jak pro metodu .sort(), tak pro funkci sorted()
# třídit v opačném pořadí můžeme pomocí parametru `reverse`
print(sorted(l2, reverse=True))

# pokud potřebujeme třídit pomocí méně triviálního klíče, můžeme použít vlastní funkci pro výpočet klíče a předat ho pomocí parametru `key`
# funkce nám musí vrátit porovnatelný klíč, podle kterého může Python list seřadit
# pokud např. jako klíč předáme funkci `len`, můžeme řadit prvky podle délky
l = ["b", "aaa", "dddd", "cc"]
print(sorted(l, key=len))

# pokud chceme např. seřadit dvojice podle druhého prvku a v případě shody pozpátku podle prvního prvku, můžeme si napsat vlastní funkci
l = [(0, 1), (3, 2), (2, 0), (4, 2)]

def compute_key(elem):
    return (elem[1], -elem[0])

print(sorted(l, key=compute_key))

# zápis můžeme zkrátit pomocí lambda funkcí
# lambda funkce je anonymní funkce - nemusíme ji pojmenovávat a můžeme ji zapsat rovnou jako parametr
# zapisujeme `lambda PARAM1, PARAM2, ...: VÝRAZ`
# lambda funkce může obsahovat jen jeden výraz, který je zároveň její návratovou hodnotou
# zápis stejného řešení pomocí lambda funkce bude tedy vypadat takto:
print(sorted(l, key=lambda elem: (elem[1], -elem[0])))