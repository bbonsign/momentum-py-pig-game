# import pytest
from pig import Game, Player, Die

VALUES = [i for i in range(1, 7)]


def test_create_player():
    player = Player('Human')
    assert player is not None
    assert player.name == 'Human'
    assert player.score == 0


def test_create_game():
    game = Game()
    assert game is not None


def test_create_die():
    die = Die()
    assert die is not None
    assert die.values == VALUES


def test_roll_die():
    die = Die()
    rolls = {die.roll() for i in range(1000)}
    assert rolls == set(VALUES)
    for i in range(50):
        assert die.roll() in VALUES
