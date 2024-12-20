from main import contarVocales

def test_contarVocales():
    assert contarVocales("hello") == 2
    assert contarVocales("world") == 1
    assert contarVocales("AEIOU") == 5
    assert contarVocales("bcdfg") == 0
