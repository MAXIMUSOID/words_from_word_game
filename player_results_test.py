from player_results import Player_results
from player import Player
from config import RESULT_FILE_NAME_TEST

def test_file_clear():
    with open(RESULT_FILE_NAME_TEST, mode="w") as f:
        f.write('{}')

def test_1():
    pl = Player_results()
    
    pl.add_result("Игрок1", 6)
    assert pl.get_current_result('Игрок1') == 1
    
def test_2():
    pl = Player_results()
    
    pl.add_result("Игрок2", 8)
    assert pl.get_current_result('Игрок2') == 1
    
def test_3():
    pl = Player_results()
    
    pl.add_result("Игрок3", 9)
    assert pl.get_current_result('Игрок3') == 1
    
def test_4():
    pl = Player_results()
    
    pl.add_result("Игрок4", 10)
    pl.add_result("Игрок5", 0)
    pl.add_result("Игрок6", 0)
    pl.add_result("Игрок7", 0)
    pl.add_result("Игрок8", 0)
    pl.add_result("Игрок9", 0)
    pl.add_result("Игрок10", 0)
    pl.add_result("Игрок11", 0)
    pl.add_result("Игрок12", 0)
    assert pl.get_current_result('Игрок4') == 1
    
def test_5():
    pl = Player_results()
    p = Player()
    p.set_player("Игрок12")
    print(pl.get_all_user_statistic(p))
    
    
    
if __name__ == "__main__":
    test_file_clear()
    Player_results().init(RESULT_FILE_NAME_TEST)
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()