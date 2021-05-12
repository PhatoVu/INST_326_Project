from INST_326_Project.type_test_game import Game
import pytest
from type_test_game import Game

new_game = Game()
def test_get_results():
    assert(new_game.get_results(.5, 30)) == 60
    assert(new_game.get_results(.237, 10)) == pytest.approx(42.1941)
    assert(new_game.get_results(.4, 20)) == pytest.approx(50)
    assert(new_game.get_results(.425, 100)) == pytest.approx(235.2940)
    assert(new_game.get_results(39, 999)) == pytest.approx(25.6154)
