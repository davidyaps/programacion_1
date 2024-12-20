"""
12.	Escribe una función recursiva imprimirValoresImpares(numero) que tome un número entero como parámetro e imprima desde ese valor hasta 1 (inclusive) todos los valores impares que se encuentran en el rango (de a uno). 

Por ejemplo, si se llama a la función imprimirValoresImpares (5), se debe mostrar la siguiente salida:

5
3
1
"""
def imprimirValoresImpares(numero):
    if numero == 1:
        print(numero)
    else:
        if numero % 2 != 0:
            print(numero)
        imprimirValoresImpares(numero-1)


imprimirValoresImpares(5)