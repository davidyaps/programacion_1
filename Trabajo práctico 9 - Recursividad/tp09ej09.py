"""
9.	Dado un número entero, implementa una función recursiva llamada escalador que tome como parámetros un número, un paso (la cantidad en la que se va a ir incrementado el valor con cada llamado) y un límite; e imprima en cada iteración el resultado de sumar el paso a cada llamada recursiva hasta que se alcance el límite especificado por el límite.

Ejemplo de llamado: escalador(10, 20, 100), resultado:
30
50
70
90

"""

def escalador(numero, paso, limite):
    if numero + paso <= limite:
        print (numero + paso)
        escalador(numero+paso, paso, limite)

escalador(10, 20, 100)