"""2.	Escriba un programa para generar una función (utilizando filter) y lambdas para separar los números 
pares e impares de una lista de números. La función debe retornar dos valores resultantes."""

def obtenerParesEImpares(lista):
    listaPares = list(filter(lambda numero : numero % 2 == 0, lista))
    listaImpares = list(filter(lambda numero : numero % 2 != 0, lista))
    return listaPares, listaImpares

valores = [0, 1, 1, 2, 3, 5, 8, 13, 21]

pares, impares = obtenerParesEImpares(valores)

print("Pares: ", pares, "Impares: ", impares)