"""
Escribir un programa que dadas dos tuplas de tres elementos, realice el producto de cada elemento existente en la primera tupla con todos los restantes del segundo y almacene cada resultado en otra tupla. 
Por ejemplo, el producto escalar entre (1, 2, 3) y (4, 5, 6); debería retornar: ((4, 5, 6),(8, 10, 12), (12, 15, 18)).
"""

def sumarTuplas(tupla1, tupla2):
    resultado = []
    for valor1 in tupla1:
        producto = []
        for valor2 in tupla2:
            producto.append(valor1 * valor2)
        resultado.append(tuple(producto))

    resultado = tuple(resultado)

    return resultado

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)



print(sumarTuplas(tupla1, tupla2))