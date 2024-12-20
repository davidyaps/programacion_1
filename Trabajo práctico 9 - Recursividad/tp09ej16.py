"""
16.	Se requiere implementar una función que permita invertir el contenido de una lista de manera recursiva. La función tomará como parámetro una lista y devolverá una nueva lista que contenga los elementos en orden inverso. 

invertirListaRecursivamente([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]

"""

def invertirListaRecursivamente(lista):
    if len(lista) <= 1:
        return lista
    else:
        return [lista[-1]] + invertirListaRecursivamente(lista[:-1])

miLista = [1, 2, 3, 4, 5]
listaInvertida = invertirListaRecursivamente(miLista)

print("Lista original:", miLista)
print("Lista invertida:", listaInvertida)