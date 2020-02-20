# import pytest
from pig import Player, Die, Robot  # Game

VALUES = [i for i in range(1, 7)]

# Asking for input after starting game doesn't work well with pytest
# def test_create_game():
#     game = Game(6)
#     assert isinstance(game.player1, Player)
#     assert isinstance(game.player2, Player)
#     assert isinstance(game.die, Die)


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


def test_robot():
    bot = Robot('bot')
    assert isinstance(bot, Robot)
    assert isinstance(bot, Player)
    assert bot.name == 'bot'
