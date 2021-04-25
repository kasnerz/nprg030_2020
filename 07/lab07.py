#!/usr/bin/env python3

"""
Kód ke cvičení #7 z NPRG030.
Kód nemá fungovat jako celek a nemusí být kompletní.
Jednotlivé části kódu byly postupně vysvětleny na cvičení.
"""

# ===================
# modul random
# ===================

# modul používaný pro generování pseudonáhodných čísel, prvků, permutací listů...
import random

# opravdová *náhoda* v počítači neexistuje - čísla z generátoru mají pouze náhodný charakter 
# díky tomu nám program může pokaždé vracet stejná (náhodně vypadající) čísla
# pokud nastavíme před generováním seed na konkrétní hodnotu

random.seed(42)     # bez seedu by byla čísla při každém běhu programu různá
                    
# s modulem random můžeme například...
# ...vygenerovat celé číslo z intervalu <0,9> (s tímto seedem zrovna konkrétně jedničku)...
x = random.randint(0,9)
print(x)

l = ["a", "b", "c", "d", "e"]

# ...zamíchat seznam...
random.shuffle(l)
print(l)

# ...vybrat ze seznamu náhodný prvek... 
elem = random.choice(l)
print(elem)

# ...nebo rovnou několik náhodných prvků 
elems = random.sample(l, 3)
print(elems)