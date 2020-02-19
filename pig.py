import random as rand


class Game:
    def __init__(self):
        pass

    def __str__(self):
        return


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hold = 0

    def __str__(self):
        return self.name

    def roll(self, die):
        value = die.roll()
        if value == 1:
            self.hold = 0
        else:
            self.hold += value

    def update_score(self):
        self.score += self.hold
        self.hold = 0


class Die:
    def __init__(self):
        self.values = [1, 2, 3, 4, 5, 6]

    def __str__(self):
        return f"{len(self.values)}-sided die"

    def roll(self):
        return rand.choice(self.values)
