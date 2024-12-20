from main import esPar

def test_esPar():
    assert esPar(4) == True
    assert esPar(7) == False
    assert esPar(0) == True
    assert esPar(-2) == True
    assert esPar(-3) == False
