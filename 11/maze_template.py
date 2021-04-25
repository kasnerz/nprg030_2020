#!/usr/bin/env python3
from collections import deque

# ===================================
# fronta jen tak pro radost (či ne?)
# ===================================
class Queue:
    def __init__(self):
        self.q = deque()

    def dequeue(self):
        return self.q.popleft()

    def enqueue(self, elem):
        self.q.append(elem)

    def empty(self):
        return not bool(self.q)


def is_free(x,y,fields):
    """
    Kontroluje, zda se na pole dá vstoupit.

    Parametry:
    x: x-ová souřadnice pole
    y: y-ová souřadnice pole
    fields (list): seznam o velikosti MxN, kde každý prvek obsahuje "#" (zeď) nebo " " (volno)

    Vrací:
    bool: 
        - True pokud se souřadnice nachází v bludišti a pole je prázdné
        - False pokud je pole obsazené nebo se souřadnice nenachází v bludišti
    """
    return x >= 0 \
        and y >= 0 \
        and x < len(fields) \
        and y < len(fields[0]) \
        and fields[x][y] == " "


def find_path(fields):
    """
    Najde cestu v bludišti.

    Parametry:
    fields (list): seznam o velikosti MxN, kde každý prvek obsahuje "#" (zeď) nebo " " (volno)

    Vrací:
    coordinates (list): seznam n-tic (X,Y) se souřadnicemi cesty
    """
    M = len(fields)        # počet řádků bludiště
    N = len(fields[0])     # počet sloupců bludiště

    path_coordinates = []

    # =======================================================================================
    # TODO: doplňte kód, který do listu path_coordinates doplní souřadnice (n-tice (X,Y))
    # nejkratší cesty ze startu (0,0) do cíle (M-1, N-1)
    # =======================================================================================
    
    # prohledám graf do šířky ze startovního pole
    # ukládám si zároveň do pomocného pole vzdáleností (MxN), na kolik kroků jsem došel na konkrétní pole 
    # jakmile dojdu do cíle, můžu prohledávání ukončit

    # pak procházím pole vzdáleností *z cíle* až *do startu*
    # vždy přejdu na pole, na které jsem došel o krok dřív
    # (pokud jich je víc, nezáleží, které vyberu)
    # souřadnice polí, která procházím, ukládám do path_coordinates

    # zavolám path_coordinates.reverse() -> hotovo! 

    return path_coordinates


def parse_maze(maze):
    """
    Načte bludiště ze stringu a vrátí 2D seznam s políčky.

    Parametry:
    maze (string): bludiště v textové podobě

    Vrací:
    list: seznam o velikosti MxN, kde každý prvek obsahuje "#" (zeď) nebo " " (volno)
    """
    fields = []

    for line in maze.split("\n")[1:-1]:
        fields.append(list(line))

    return fields


def draw_path(fields, coordinates, numerical=False):
    """
    Vykreslí cestu v bludišti.

    Parametry:
    fields (list): 2D seznam s bludištěm
    coordinates (list): seznam n-tic (X,Y) se souřadnicemi cesty
    numerical (bool): True: vykreslí pořadí souřadnic pomocí čísel, False: pouze pomocí teček
    """
    for i, (x,y) in enumerate(coordinates):
        if not is_free(x, y, fields):
            raise ValueError(f"Chyba: souřadnice ({x},{y}) se nachází ve zdi nebo mimo pole.")

        fields[x][y] = str(i)[-1] if numerical else "."

    for line in fields:
        for field in line:
            print(field, end="")
        print()



# ================================
# seznam vstupních bludišť
# ================================
inputs = [
"""
  ######
# #    #
# # #  #
#   #  #
##     #
######  
""",
"""
  #######
#   #   #
# # #   #
### #   #
##    # #
#######  
""",
"""
  #######
#       #
# # #   #
# # ### #
### #   #
##      #
#######  
""",
# vypůjčeno z https://github.com/vituscze/prog1
""" 
  ###########################################################
#         #       #     #     #   # #     #   #             #
# ### # # # # ##### ### ### # ### # ### ### ### # ####### # #
#   # # # # #     # #       #       #       # # # #   #   # #
# # ############# ####### ##### ### ##### # # ### ### ##### #
# # # #             #         #   # #     #   # # #   #     #
### # ### ### ### ############# # ######### ### ### ####### #
#     # # #   # # #     #   #   # #   # # #   #   #   #     #
### ### ### # # # ### ##### ##### ### # # # ##### ### ##### #
# # #     # #   # #       #             #         # #     # #
# # ##### # ### ##### # # # ### ####### # ######### # ### # #
# # # #       #   #   # # # # # #   #               # #   # #
# # # # ### # ####### # ### # # # ### ####### # # ### ### # #
# # #   #   # #       # #   #       #   #     # #       #   #
# # # # ### # ######### ##### ##### ### ### ##### ### ##### #
# #   # # # # #     # #       #       #   #     #   #     # #
# ##### # # # ### ### # # # # ##### ### ############# #######
#       # # # #         # # # # #     # # # # # #       #   #
### # ### ### ####### ##### ### ### ### # # # # ##### ##### #
#   #       #   # #       # #         #     #       #   #   #
# ### ########### # # ### ##### ### ####### ### # # # ##### #
# #       #     #   # #     #   #       #     # # #     # # #
# ### # ####### ### # ######### # ##### ####### # ####### # #
# #   # #   # #   # # #   # #   # #       #   # #     #     #
### # ##### # # ##### ### # ####### ##### # # ##### ####### #
#   #   # #   #   # #       # # #   # # # # # #         #   #
# ##### # # ### ### # # ##### # ### # # ##### # ####### ### #
# #   #     #   # #   #     #   #             #   # # # #   #
# # ### ### # ### # ### ### ### ##### ### ######### # # # # #
#   #   # # # # # # #   # #       #     #     # # #       # #
##### ### # # # # ### ### ####### ##### ### ### # # # # #####
#       # # #   #   #       #     #     # #   #   # # #     #
# ### # # # # # ### # # # ### # ##### ### # ### ####### ### #
#   # #   #   # #     # # # # # #   # #           #   #   # #
##### ### # # ####### # ### # ### ##### ### # # # ### ##### #
# #   #   # # #     # #     #     #     #   # # #   #     # #
# ##### # # ### ##### ################### ####### # ### # # #
#     # # #     #         # #               #     #     # # #
### # ##### ####### # # ### ######### # # ############# #####
#   # # #         # # #     #       # # #     # # # #   #   #
# ### # ######### ####### # ### ### # ##### ### # # # ### ###
#   # #   #   # # #     # # #     # #   #     #   # # #   # #
### ### ### # # # ### ####### ##### # ##### ### # # # # ### #
#       #   # # #     #     # # # #   # #   #   #     #     #
# ##### ##### # ### # # ### ### # # ### ####### ######### # #
# # #     #       # #     #     #   #       #   # #       # #
# # ### ##### # # ### ### # # ### ####### ##### # # ### # # #
#   #         # #   # #   # #   # #       # #   #   # # # # #
# # # ### ##### ######### # ####### ##### # # # ### # # # ###
# # #   # #               # #   #     # # #   # # # # # #   #
### ################# ### # ### ##### # ### ##### # # ### ###
#       #       #   # # # #   # #       #         #   # #   #
# # ##### ####### # # # ####### ##### ##### ##### ### # # # #
# # #     #       # #   #     #     #     #   #         # # #
# ### ### ##### ### # ##### ####### ##### # ####### # #######
#   #   #     # # # #     # # #       #           # #     # #
######### # ### # # # ### # # # ### ##### # ##### # # # # # #
#         #   #   # #   # # #   #   # # # # #   # # # # #   #
# ##### ##### ##### ##### # # ##### # # # # ### # # # ##### #
#     #     #                   #         # #     # # #     #
###########################################################  
""" 
]
# hlavní smyčka
for i, maze in enumerate(inputs):
    print("\n==========================")
    print(f"Bludiště #{i+1}")
    print("==========================")

    # print(maze)
    input("Stiskněte Enter pro nalezení cesty v bludišti nebo Ctrl+C pro ukončení programu.\n")
    fields = parse_maze(maze)
    coordinates = find_path(fields)
    draw_path(fields, coordinates, numerical=True)
