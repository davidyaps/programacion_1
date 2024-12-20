"""3.	Escriba un programa para contar los números pares e impares en una lista dada de enteros usando Lambda."""

def obtenerCantidadParesEImpares(lista):
    listaPares = len(list(filter(lambda numero : numero % 2 == 0, lista)))
    listaImpares = len(list(filter(lambda numero : numero % 2 != 0, lista)))
    return listaPares, listaImpares

valores = [0, 1, 1, 2, 3, 5, 8, 13, 21]

pares, impares = obtenerCantidadParesEImpares(valores)

print("Pares: ", pares, "Impares: ", impares)
