"""
5.	Suma de Filas y Columnas: crear una función que tome una matriz como entrada y devuelva una lista con la suma de cada fila y otra lista con la suma de cada columna.
"""

def sumarFilasYColumnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    sumasFila = []
    sumasColumna = [0] * columnas

    for i in range(filas):
        sumaFila = []
        suma = 0
        for s in range(0, len(matriz[i])):
            suma += matriz[i][s]
        sumasFila.append(suma)

        for j in range(columnas):
            sumasColumna[j] += matriz[i][j]

    return sumasFila, sumasColumna



# Ejemplo de uso
matrizEjemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sumasFilas, sumasColumnas = sumarFilasYColumnas(matrizEjemplo)

print("Matriz de ejemplo:")
for fila in matrizEjemplo:
    print(fila)

print("\nSumas de filas:", sumasFilas)
print("Sumas de columnas:", sumasColumnas)
