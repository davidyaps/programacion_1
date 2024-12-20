from main import esPalindromo

def test_esPalindromo():
    assert esPalindromo("radar") == True
    assert esPalindromo("python") == False
    assert esPalindromo("ana") == True
    assert esPalindromo("") == True
    assert esPalindromo("a") == True
