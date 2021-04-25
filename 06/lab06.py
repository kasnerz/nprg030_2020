#!/usr/bin/env python3

"""
Kód ke cvičení #6 z NPRG030.
Kód nemá fungovat jako celek a nemusí být kompletní.
Jednotlivé části kódu byly postupně vysvětleny na cvičení.
"""

# ===================
# třídy a objekty
# ===================

# třída je "šablona", podle které můžeme vytvářet jednotlivé objekty
# třídu vytvoříme pomocí klíčového slova `class`
# pro název je zvykem je používat podstatné jméno začínající velkým písmenem (s více slovy používáme CamelCase)
class Item:
    pass            # `pass` označuje prázdný blok

# objekty vytváříme voláním konstruktoru třídy
backpack = Item()
sleeping_bag = Item()

# oba objekty jsou odvozené od stejné třídy...
print(type(backpack))
print(type(sleeping_bag))

# ...ale každý z nich existuje samostatně
print(backpack is not sleeping_bag)

del Item     # (mažu třídu, abych ji mohl v tomto kódu zadefinovat znova)

# třída může mít vlastní atributy a metody (proměnné, resp. funkce existující uvnitř třídy)
class Item:
    description = "e-shop item"

    def print_description(self):
        print(self.description)

# každá metoda musí mít jako první argument `self`
# tento argument je předaný automaticky při volání metody nad daným objektem (nepíšeme ho tedy explicitně při volání metody, ale při její definici ano)
# `self` používáme, pokud se chceme odkazovat na samotný objekt (jeho atributy, metody, atd.) uvnitř objektu
torch = Item()
print(torch.print_description())

del Item

# při vytváření objektu se vždy volá metoda .__init__()
# metodu můžeme využít pro inicializaci proměnných a předání parametrů pro jednotlivé objekty
class Item:
    def __init__(self, id, type, price):
        self.id = id            # předaný parametr `id` uložíme do atributu `self.id` pro konkrétní objekt
        self.type = type
        self.price = price      # atributy se můžou jmenovat i jinak, jména jsou tu stejná pro jednoduchost

        print("zavolal se __init__()")

    def print_description(self):
        print(f"Item #{self.id}: {self.type} ({self.price} CZK)")

    def set_price(self, price):
        self.price = price


matress1 = Item(id=1, type="karimatka", price=1500)
matress2 = Item(id=2, type="karimatka", price=1200)
bottle = Item(id=3, type="lahev", price=100)

matress1.print_description()
matress2.print_description()
bottle.print_description()

# všechny atributy jsou viditelné zvenší, můžeme je tedy přímo nastavovat
# není to ale dobrá OOP praxe a měli bychom se tomu přístupu vyhýbat
bottle.price = 50

# správně je volat metodu `.set_price()`, která nám odstíní konkrétní implementaci
# např. pokud se v budoucnu rozhodneme k ceně přičítat DPH, stačí nám změnit kód uvnitř metody
bottle.set_price(50)

# s objekty můžeme dále manipulovat uvnitř jiných objektů apod. a vystavit na nich logickou strukturu našeho programu
class Storage:
    def __init__(self, max_capacity=100):       # parametr `max_capacity` s defaultní hodnotou je nepovinný, podobně jako u funkcí
        self.capacity = max_capacity
        self.items = []

    def is_full(self):
        return self._get_item_count() >= self._get_capacity()

    # metody s prefixem "_" jsou považovány za privátní a neměly by být volány mimo metody objektu
    # jde ovšem pouze o konvenci a Python její dodržování nekontroluje
    def _get_capacity(self):
        return self.capacity

    def _get_item_count(self):
        return len(self.items)

    def add_item(self, item):
        if not self.is_full():
            self.items.append(item)
            print("Item added")
        else:
            print("Storage is full")

    def clear(self):
        self.items.clear()

    def get_items(self):
        return self.items

    # v metodě `__str__` můžeme zadefinovat, jak se objekt převede na string (např. při volání print())
    def __str__(self):
        return f"Storage: {self._get_item_count()}/{self._get_capacity()} items"


# příklad manipulace s objekty
storage = Storage()

for i in range(100):
    bottle = Item(i, type="lahev", price=90)
    storage.add_item(bottle)

print(storage)

storage.add_item(Item(101, type="lahev", price=100))

items = storage.get_items()
storage.clear()

print(storage)
print(storage.is_full())
