def obtenerFrases(matriz):
    frases = []
    for fila in range(0, len(matriz)):
        frase = ''
        for columna in range(0, len(matriz[fila])):
            frase += matriz[fila][columna] + ' '
        frases.append(frase.strip()) 
    return frases

matrizEjemplo = [
    ['Hola', 'cómo', 'estás'],
    ['Estoy', 'bien', 'gracias']
]

resultado = obtenerFrases(matrizEjemplo)
print(resultado)
