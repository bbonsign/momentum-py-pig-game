# import pytest
from pig import Game, Player, Die

VALUES = [i for i in range(1, 7)]


def test_create_game():
    game = Game(6)
    assert isinstance(game.player1, Player)
    assert isinstance(game.player2, Player)


def test_create_player():
    player = Player('Human')
    assert player.name == 'Human'
    assert player.score == 0
    assert player.hold == 0
    assert player.action == 'roll'


def test_create_die():
    die = Die(6)
    assert die.values == VALUES
    assert str(die) == "6-sided die"


def test_roll_die():
    die = Die(6)
    rolls = {die.roll() for i in range(10000)}
    assert rolls == set(VALUES)
    for i in range(50):
        assert die.roll() in VALUES


def test_player_roll():
    player = Player('Human')
    player.roll(Die(6))
