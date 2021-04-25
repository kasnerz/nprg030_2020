import tkinter as tk
from PIL import ImageTk, Image

# lepší by bylo TerminalView a GraphicalView oddělit do samostatných souborů
# a pygame importovat jen u GraphicalView
import pygame
import time

class View:
    def draw_initial_dialogue(self):
        raise NotImplementedError

    def render_game(self, battlefield_player, battlefield_enemy):
        raise NotImplementedError


class TerminalView(View):
    def draw_initial_dialogue(self):
        field_size = int(input("Zadejte velikost pole: "))
        ship_cnt = int(input("Zadejte počet lodí: "))
        first_player_name = input("Zadejte jméno prvního hráče: ")
        second_player_name = input("Zadejte jméno druhého hráče: ")

        # + kontroly vstupu

        # hezčí než slovník by bylo vytvořit objekt GameOptions s těmito parametry
        return {
            "field_size" : field_size,
            "ship_cnt" : ship_cnt,
            "first_player_name" : first_player_name,
            "second_player_name" : second_player_name
        }

    def render_game(self, battlefield_player, battlefield_enemy):
        # nedokončeno
        raise NotImplementedError
        # lines = []
        # for line in field.battlefield:
        #     lines.append("|" + "|".join([str(f) for f in line]) + "|")

        # print("\n".join(lines))


class GraphicalView(View):
    def __init__(self):
        pygame.init()
        self.window_width = 1000
        self.window_height = 600
        self.font = pygame.font.SysFont(None, 40)


    def _start_game(self):
        field_size = int(self.ent_field_size.get())
        ship_cnt = int(self.ent_ship_cnt.get())
        first_player_name = self.ent_first_player_name.get()
        second_player_name = self.ent_second_player_name.get()

        # zde by mohla být kontrola, jestli hodnoty dávají smysl
        self.game_options = {
            "field_size" : field_size,
            "ship_cnt" : ship_cnt,
            "first_player_name" : first_player_name,
            "second_player_name" : second_player_name
        }
        self.window.destroy()

    
    def _render_field(self, battlefield, start_pos, is_enemy):
        """
        Tady (a všude jinde) chybí tyto dokumentační komentáře popisující, co funkce dělá
        """
        field_size = 40

        for i, row in enumerate(battlefield.battlefield):
            for j, field in enumerate(row):
                x = start_pos[0] + i * field_size
                y = start_pos[1] + j * field_size

                # použijeme později pro určení, na jaké pole uživatel kliknul
                field.set_pos(x, y, field_size, field_size)

                # vykreslení jednoho pole
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, y, field_size, field_size), width=1)
                center = (x+field_size/2, y+field_size/2)

                # lodě a zásahy vykreslujeme jinak podle toho, jestli vykreslujeme vlastní, nebo nepřátelské
                if is_enemy:
                    if field.is_hit:
                        pygame.draw.circle(self.screen, (0, 0, 0), center, 10)
                        if field.ship:
                            pygame.draw.circle(self.screen, (255, 0, 0), center, 10)
                else:
                    if field.is_hit and field.ship:
                        pygame.draw.circle(self.screen, (255, 0, 255), center, 10)
                    elif field.ship:
                        pygame.draw.circle(self.screen, (0, 0, 255), center, 10)
                    elif field.is_hit:
                        pygame.draw.circle(self.screen, (0, 0, 0), center, 10)


    def _render_info(self, player1, player2):
        # zobrazení jmen hráčů
        info1 = self.font.render(f"{player1}", True, "blue")
        self.screen.blit(info1, (self.window_width//4 - 60, self.window_height-100))

        info2 = self.font.render(f"{player2}", True, "red")
        self.screen.blit(info2, (self.window_width//4 * 3 - 60, self.window_height-100))


    def _get_field_by_pos(self, battlefield, pos):
        # low-effort verze, lepší by bylo použít funkci collidepoint()
        return battlefield.get_field_by_pos(pos)

    def _handle_click(self, event):
        # kliknutí levým tlačítkem myši
        if self.state == "NEXT_TURN":
            # pokud jen čekáme na příchod dalšího hráče, změníme stav
            self.state = "PLAYING"

            # a prohodíme, kdo je nepřítel a kdo hráč
            self.battlefield1, self.battlefield2 = self.battlefield2, self.battlefield1

        elif self.state == "PLAYING":
            # pokud je hráč na tahu, zjistíme, jestli kliknul na nepřátelské políčko
            pos = pygame.mouse.get_pos()
            field = self._get_field_by_pos(self.battlefield2, pos)

            if field:
                # voláme game control, protože jde o logiku hry a nemělo by to řešit view...
                self.game_control.field_is_hit(field)

                # podobně by v game control mohly být i stavy (ale zde nejsou)
                self.state = "NEXT_TURN"



    def render_game(self, game_control, battlefield_player, battlefield_enemy):
        self.game_control = game_control
        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        self.battlefield1 = battlefield_player
        self.battlefield2 = battlefield_enemy
        self.state = "PLAYING"      # "PLAYING", "NEXT_TURN"; lepší by bylo použít Enum
        
        running = True

        # odsazení
        margin = 30

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._handle_click(event)

            self.screen.fill("white")

            if self.state == "PLAYING":
                # vykreslíme pole a jména hráčů
                self._render_field(self.battlefield1, start_pos=(margin,margin), is_enemy=False)
                self._render_field(self.battlefield2, start_pos=(self.window_width//2 + margin, margin), is_enemy=True)
                self._render_info(self.battlefield1.player, self.battlefield2.player)

            elif self.state == "NEXT_TURN":
                # vykreslíme hlášku, že čekáme na dalšího hráče
                player_name = self.battlefield1.player
                info = self.font.render(f"Na tahu je {player_name}, klikněte pro pokračování...", True, "blue")
                self.screen.blit(info, (margin, self.window_height//2))

            # vykreslí všechny změny na obrazovku
            pygame.display.flip()

        pygame.quit()


    def draw_initial_dialogue(self, field_size_defaults=(2,20,10), ship_cnt_defaults=(1,15,8)):
        # hlavní okno
        self.window = tk.Tk()
        self.window.configure(bg="white")   # při použití ttk se dá styl (jako např. bílé pozadí) nastavit všem widgetům najednou
        
        # ikona hry
        self.header_img = ImageTk.PhotoImage(Image.open("img/battleship.png"))
        self.lbl_header_img = tk.Label(image=self.header_img, bg="white")

        # nadpis
        # pozor, height a width se nepočítá v pixelech, ale jako násobky velikosti fontu
        self.lbl_heading = tk.Label(text=u"LODĚ",
                                    bg="white",
                                    fg="blue",
                                    height=2,
                                    width=10,
                                    font=("Century Gothic", 44, "bold"))

        # kontejner, který použijeme pro rozmístění nastavení do mřížky
        self.frm_options = tk.Frame(bg="white")

        # nastavení: velikost pole
        self.lbl_field_size = tk.Label(master=self.frm_options,
                                        bg="white",
                                       text="Velikost pole")
        self.ent_field_size = tk.Scale(master=self.frm_options, 
                                        from_=field_size_defaults[0],
                                        to=field_size_defaults[1],
                                        bg="white",
                                        orient=tk.HORIZONTAL)
        self.ent_field_size.set(field_size_defaults[2])

        # nastavení: počet lodí
        self.lbl_ship_cnt = tk.Label(master=self.frm_options,
                                    bg="white",
                                    text="Počet lodí")
        self.ent_ship_cnt = tk.Scale(master=self.frm_options, 
                                        from_=ship_cnt_defaults[0],
                                        to=ship_cnt_defaults[1],
                                        bg="white",
                                        orient=tk.HORIZONTAL)
        self.ent_ship_cnt.set(ship_cnt_defaults[2])


        self.frm_players = tk.Frame(bg="white")
        # tlačítko Spustit hru
        self.btn_start = tk.Button(bg='white',
                                    text="Spustit hru",
                                    command=self._start_game)
    
        self.lbl_first_player_name = tk.Label(master=self.frm_players, bg="white", text="Jméno prvního hráče")
        self.ent_first_player_name = tk.Entry(master=self.frm_players, bg="white")
        self.ent_first_player_name.insert(tk.END, "Player 1")

        self.lbl_second_player_name = tk.Label(master=self.frm_players, bg="white", text="Jméno druhého hráče")
        self.ent_second_player_name = tk.Entry(master=self.frm_players, bg="white")
        self.ent_second_player_name.insert(tk.END, "Player 2")

        # umístění widgetů do okna
        self.lbl_header_img.pack(pady=10)
        self.lbl_heading.pack()
        self.frm_options.pack()
        self.lbl_field_size.grid(column=0,row=0, padx=20)
        self.ent_field_size.grid(column=0,row=1, padx=20)
        self.lbl_ship_cnt.grid(column=1, row=0, padx=20)
        self.ent_ship_cnt.grid(column=1, row=1, padx=20)

        self.frm_players.pack(pady=20)   # pad{x,y} - odsazení na ose x / y
        self.lbl_first_player_name.pack()
        self.ent_first_player_name.pack()
        self.lbl_second_player_name.pack()
        self.ent_second_player_name.pack()
        self.btn_start.pack(pady=20)

        # spuštění hlavní smyčky - zobrazení okna a odchytávání událostí v okně
        self.window.mainloop()

        # sem se kód dostane, jakmile je okno zavřeno (buď pomocí .destroy(), nebo uživatelem)
        return self.game_options