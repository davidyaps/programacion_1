from main import numerosPares

def test_numerosPares():
    assert numerosPares(10) == [0, 2, 4, 6, 8, 10]
    assert numerosPares(1) == [0]
    assert numerosPares(0) == [0]
    assert numerosPares(-1) == []
