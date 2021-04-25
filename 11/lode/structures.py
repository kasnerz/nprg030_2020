import random

random.seed(17)

class BattleField:
    def __init__(self, size, player):
        self.battlefield = [[Field() for _ in range(size)] 
                                        for _ in range(size)]
        self.size = size
        self.player = player

    def random_init(self, number_of_ships=5):
        placed = 0

        while True:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)

            if not self.battlefield[x][y].ship:
                self.battlefield[x][y].ship = BattleShip()
                placed += 1

            if placed == number_of_ships:
                break

    def get_field_by_pos(self, pos):
        for row in self.battlefield:
            for field in row:
                if pos in field:
                    return field


class Field:
    def __init__(self):
        self.is_hit = False
        self.ship = None

    def set_ship(self, ship):
        self.ship = ship

    def set_pos(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __contains__(self, pos):
        if not all([self.x, self.y, self.w, self.h]):
            raise ValueError("Position of the field is undefined")

        return self.x < pos[0] \
            and self.x + self.w > pos[0] \
            and self.y < pos[1] \
            and self.y + self.h > pos[1]

    def __str__(self):
        if self.is_hit:
            return "X"
        if self.ship:
            return "S"
        return " "

class BattleShip:
    pass