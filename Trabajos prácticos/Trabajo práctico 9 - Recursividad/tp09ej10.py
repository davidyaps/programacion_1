"""
Dado un número entero, implementa una función recursiva llamada multiplicador que tome como parámetros un número, un múltiplo (el valor con el que se va a ir multiplicando el numero resultante con cada llamado) y un límite; e imprima en cada iteración el resultado de multiplicar el número por el múltiplo a cada llamada recursiva hasta que se alcance el límite especificado por el límite.

Ejemplo de llamado: multiplicador(5, 2, 100), resultado:
10
20
40
80
"""

def multiplicador (numero, multiplo, limite):
    if numero * multiplo <= limite:
        print (numero * multiplo)
        multiplicador(numero*multiplo, multiplo, limite)

multiplicador(5, 2, 100)