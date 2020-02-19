import pytest
from pig import Game, Player, Die


def test_create_player():
    player = Player('Human')
    assert player != None
    assert player.name = 'Human'

def test_create_game():
    game = Game()
    assert game != None

def test_create_die():
    die = Die()
    assert die != None