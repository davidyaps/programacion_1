def buscarPalabra(matriz, palabra):
    for fila in range(0, len(matriz)):
        for columna in range(0, len(matriz[fila])):
            if matriz[fila][columna] == palabra:
                return True
    return False

matrizEjemplo = [
    ['Hola', 'cómo', 'estás'],
    ['Estoy', 'bien', 'gracias']
]

resultado = buscarPalabra(matrizEjemplo, 'bien')
print(resultado) 
