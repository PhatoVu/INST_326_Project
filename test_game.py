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

def test_get_rank():
    assert(new_game.get_rank(0)) == "Newb"
    assert(new_game.get_rank(60)) == "Newb"
    assert(new_game.get_rank(60.2)) == "Basic"
    assert(new_game.get_rank(80)) == "Basic"
    assert(new_game.get_rank(80.3)) == "Speedy"
    assert(new_game.get_rank(99)) == "Speedy"
    assert(new_game.get_rank(100.7)) == "Flashster"
    assert(new_game.get_rank(120)) == "Flashster"
    assert(new_game.get_rank(120.5)) == "Master Typer"
    assert(new_game.get_rank(140)) == "Master Typer"
    assert(new_game.get_rank(141.2)) == "Demi-God Typer"
    assert(new_game.get_rank(160)) == "Demi-God Typer"
    assert(new_game.get_rank(160.434)) == "Ascended Typer"
    assert(new_game.get_rank(179.3)) == "Ascended Typer"
    assert(new_game.get_rank(180.2)) == "Grandmaster Typer"
    assert(new_game.get_rank(400)) == "Grandmaster Typer"
    assert(new_game.get_rank(400.34342)) == "Grandmaster Typer"
