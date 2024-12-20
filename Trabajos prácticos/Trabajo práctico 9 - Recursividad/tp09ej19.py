"""
19.	Crear una función recursiva llamada contarDigitosImpares(numero) que cuente y devuelva la cantidad de dígitos impares que tiene un número. 
numero = 6174
resultado esperado: 2
"""
def contarDigitosImpares(numero):
    if numero >= -9 and numero <= 9:
        if numero % 2 != 0:
            return 1
        else:
            return 0
    else:
        if (numero % 10) % 3 != 0:
            return 1 + contarDigitosImpares(numero // 10)
        else:
            return 0 + contarDigitosImpares(numero // 10)

print(contarDigitosImpares(6174))        