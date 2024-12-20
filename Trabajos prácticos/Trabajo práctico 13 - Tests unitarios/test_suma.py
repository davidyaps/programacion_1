from main import suma

def test_suma():
    assert suma(3, 4) == 7
    assert suma(-1, 1) == 0
    assert suma(-1, -1) == -2
