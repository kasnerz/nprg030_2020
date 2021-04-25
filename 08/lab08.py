#!/usr/bin/env python3

"""
Kód ke cvičení #8 z NPRG030.
Kód nemá fungovat jako celek a nemusí být kompletní.
Jednotlivé části kódu byly postupně vysvětleny na cvičení.
"""

# ==================
# ternární operátor
# ==================

# způsob, jak zjednodušit podmínku na jeden řádek
# syntax: EXPR1 if COND else EXPR2
# výsledkem výrazu je EXPR1, pokud je COND vyhodnocena jako pravdivá, v opačném případě je výsledkem výrazu EXPR2

age = 10
price = 50 if age < 18 else 100

# ...což je zkrácený výraz pro

if age < 18:
    price = 50
else:
    price = 100

# jsou případy, kde je použití ternárního operátoru vhodné
# a jsou případy, kdy ne) - je vhodné to rozlišovat


# ==================
# pickle
# ==================
# modul pro serializaci dat: ukládání datových struktur do souborů
import pickle

game_state = [1, 2, 3, "a", "b", {"c": 4}]

# pro zápis i načítání musíme soubor otevřít v binárním modu
with open("game.bin", "wb") as f:
    pickle.dump(game_state, f)

# data si můžeme kdykoliv ze souboru znovu načíst
with open("game.bin", "rb") as f:
    loaded_game_state = pickle.load(f)
