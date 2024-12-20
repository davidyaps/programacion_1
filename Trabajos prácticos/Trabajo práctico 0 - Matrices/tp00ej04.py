"""
4.	Producto Escalar: crear una función que tome una matriz y un número como entrada, y devuelva la matriz resultante de multiplicar cada elemento por el número dado.
"""

def productoEscalar(matriz, numero):
    filas = len(matriz)
    columnas = len(matriz[0])

    matrizResultante = []

    for i in range(filas):
        filaResultante = []
        for j in range(columnas):
            productoElemento = matriz[i][j] * numero
            filaResultante.append(productoElemento)
        matrizResultante.append(filaResultante)

    return matrizResultante



# Ejemplo de uso
matrizOriginal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

numero = 2

resultado = productoEscalar(matrizOriginal, numero)

print("Matriz original:")
for fila in matrizOriginal:
    print(fila)

print("\nNúmero para el producto escalar:", numero)

print("\nResultado del producto escalar:")
for fila in resultado:
    print(fila)
