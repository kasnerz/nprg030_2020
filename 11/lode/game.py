from pprint import pprint as pp

# stačí zaměnit tyto dva řádky pro změnu stylu GUI
# from view import TerminalView as View
from view import GraphicalView as View
from structures import BattleField

# obsahuje callbacky, které bude používat View pro obsluhu událostí
class GameControl:
    def field_is_hit(self, field):
        field.is_hit = True


class Game:
    def __init__(self):
        self.gui = View()
        self.game_control = GameControl()


    def play(self):
        game_options = self.gui.draw_initial_dialogue()

        print("Nastavení hry:")
        # pretty printing - vytiskne objekty "pěkně", např. slovník bude zarovnaný po řádcích
        pp(game_options)

        self.field1 = BattleField(game_options["field_size"], game_options["first_player_name"])
        self.field2 = BattleField(game_options["field_size"], game_options["second_player_name"])

        self.field1.random_init(number_of_ships=game_options["ship_cnt"])
        self.field2.random_init(number_of_ships=game_options["ship_cnt"])

        self.gui.render_game(self.game_control, self.field1, self.field2)