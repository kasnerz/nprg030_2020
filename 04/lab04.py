#!/usr/bin/env python3

"""
Kód ke cvičení #4 z NPRG030.
Kód nemá fungovat jako celek a nemusí být kompletní.
Jednotlivé části kódu byly postupně vysvětleny na cvičení.
"""

# ===================
# funkce
# ===================

# základní návratová hodnota funkce je None
def log():
    print("Logging...")

print(log())

# výsledek vracíme pomocí `return`, vrátit můžeme i víc parametrů najednou
def add_and_subtract(a, b):
    return a+b, a-b

res = add_and_subtract(6, 4)

# výsledkem je potom n-tice (tuple)
print(res)

# ...kterou můžeme indexovat podle zvyku...
sum = res[0]
diff = res[1]

# ... případně rovnou přiřadit do příslušných proměnných
sum, diff = res

# funkce může přijímat předem neurčený počet pozičních a klíčových parametrů
def max_list(*numbers, **kwargs):
    print(kwargs)

    return max(numbers)

max_list(1, 2, 3, 4, log=True, verbose=False)

# funkce je v zásadě pouze objekt
obj = add_and_subtract

# ...který má nadefinovanou magic metodu __call__
print(dir(add_and_subtract))

# ...a můžeme s ní jako s objektem manipulovat
arr = []
arr.append(add_and_subtract)
arr.append(max_list)

res = arr[0](6, 4)

# funkce se dají zanořovat
# to se hodí v případě, že funkce je pouze pomocná a nemá být viditelná zvenku (=mimo vnější funkci)
def outer(text):  
    def inner():  
        print(text)  
    
    inner()
    return text.split()

res = outer("Hello world")
print(res)

# pokud chceme ve funkci měnit proměnné definované mimo funkci (a nepředané jako parametry), musíme použít klíčové slovo `global`
# této praxi se většinou snažíme vyhnout např. dobrým objektovým návrhem
constant = 666

def do_magic():
    global constant
    constant = 777

do_magic()
print(constant)

# podobně funguje klíčové slovo `nonlocal` pro přístup k proměnným ve funkci o úroveň výš 
def outer2():
    my_local_variable = 7

    def inner():
        nonlocal my_local_variable  
        my_local_variable = 8
    
    inner()
    print(my_local_variable)

outer2()
