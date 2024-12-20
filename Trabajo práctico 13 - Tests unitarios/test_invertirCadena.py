from main import invertirCadena

def test_invertirCadena():
    assert invertirCadena("hola") == "aloh"
    assert invertirCadena("Python") == "nohtyP"
    assert invertirCadena("") == ""
    assert invertirCadena("a") == "a"
