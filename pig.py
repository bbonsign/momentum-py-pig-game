import random as rand

###############################################################
def update_stats(game):
    pass


def clear_stats():
    with open('stats', 'w') as f:
        f.write('')


def center(value):
    return str(value).center(15)
##############################################################


class Game:
    def __init__(self, die_size):
        # self.die_size = die_size
        self.player1 = Player('Human')
        self.player2 = Player('Bot')
        self.die = Die(die_size)
        self.stop = False
        self.winner = 0
        self.start_game()

    last_winner = None

    def __str__(self):
        return "A game of Pig"

    def start_game(self):
        """
        Choose a random player to start with,
        otherwise the previous loser starts
        """
        if Game.last_winner is None:
            if rand.choice([0, 1]) == 1:
                self.player1, self.player2 = self.player2, self.player1
        elif Game.last_winner == 'Human':
            self.player1, self.player2 = self.player2, self.player1
        self.update()

    def print_turn(self, player):
        player_announce = f"{player.name} player's turn"
        print(f"""
{' '*11}{player_announce}
{' '*11}{'='*len(player_announce)}\n""")

    def print_state(self):
        player1 = self.player1
        player2 = self.player2
        print(f"""
{'_'*60}\n
{' '*11}{' '*14}{'Totals:'}
{' '*11}{'='*33}
{' '*11}|{center(player1.name)}||{center(player2.name)}|
{' '*11}|{center(player1.score)}||{center(player2.score)}|
{' '*11}{'='*33}
""")

    def end_game(self):
        pass

    def update(self):
        die = self.die
        while not self.stop:
            self.print_turn(self.player1)
            self.player1.turn(die)
            self.print_state()
            if self.player1.score >= 100:
                self.winner = self.player1
                self.stop = True
                break
            self.print_turn(self.player2)
            self.player2.turn(die)
            self.print_state()
            if self.player2.score >= 100:
                self.winner = self.player2
                self.stop = True
                break
        self.end_game()


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hold = 0
        self.action = 'roll'

    def __str__(self):
        return self.name

    def roll(self, die):
        value = die.roll()
        if value == 1:
            self.hold = 0
            self.action = 'hold'
            self.update_score()
        else:
            self.hold += value
        return value

    def update_score(self):
        self.score += self.hold
        self.hold = 0

    def turn(self, die):
        while self.action == 'roll':
            value = self.roll(die)
            if value == 1:
                print(f"  {self.name} player rolled {value}. Now its the other player's turn\n")
                break
            print(f"  {self.name} player rolled {value}. The running total is {self.hold}\n")
            inp = input('  roll or hold?: ')
            while not( inp == 'roll' or inp == 'hold'):
                inp = input('  roll or hold?: ')
            if inp == 'hold':
                self.action = 'hold'
                self.update_score()
            elif inp == 'roll':
                continue
        self.action = 'roll'  # reset action so the next turn works the same


class Robot(Player):
    pass


class Die:
    def __init__(self, sides):
        self.values = [i for i in range(1, sides+1)]

    def __str__(self):
        return f"{len(self.values)}-sided die"

    def roll(self):
        return rand.choice(self.values)


if __name__ == '__main__':
    Game(6)
