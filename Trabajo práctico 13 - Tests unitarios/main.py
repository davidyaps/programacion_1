def suma(a, b):
    return a + b

def esPar(n):
    return n % 2 == 0

def invertirCadena(cadena):
    return cadena[::-1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def esPalindromo(cadena):
    return cadena == cadena[::-1]

def encontrarMaximo(lista):
    if len(lista) >= 1:
        return max(lista)
    return None

def contarVocales(cadena):
    vocales = "aeiou"
    return sum(1 for caracter in cadena if caracter.lower() in vocales)

def numerosPares(n):
    return [x for x in range(n+1) if x % 2 == 0]