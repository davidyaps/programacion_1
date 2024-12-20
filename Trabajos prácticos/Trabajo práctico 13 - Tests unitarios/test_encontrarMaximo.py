from main import encontrarMaximo

def test_encontrarMaximo():
    assert encontrarMaximo([1, 2, 3, 4, 5]) == 5
    assert encontrarMaximo([-1, -2, -3, -4]) == -1
    assert encontrarMaximo([3]) == 3
    assert encontrarMaximo([]) == None
