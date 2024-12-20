"""
7. Contador de palabras: Escribe un programa que lea un archivo de texto y cuente la cantidad de veces que aparece cada palabra en el archivo. Utiliza un diccionario para almacenar las palabras y sus frecuencias. Al final, muestra las 10 palabras más comunes en el archivo.
"""

# Abrir el archivo de texto
with open('archivos/El viento del norte y el sol.txt', 'r', encoding='utf-8') as archivo:
    # Crear un diccionario vacío para almacenar las palabras y sus frecuencias
    diccionario_palabras = {}
    # Leer el archivo línea por línea
    for linea in archivo:
        # Separar cada línea en palabras
        palabras = linea.strip().split()
        # Iterar sobre cada palabra
        for palabra in palabras:
            # Convertir a minúsculas para contar la frecuencia de manera consistente
            palabra = palabra.lower()
            # Incrementar el contador de la palabra en el diccionario
            if palabra in diccionario_palabras:
                diccionario_palabras[palabra] += 1
            else:
                diccionario_palabras[palabra] = 1

# Ordenar el diccionario por frecuencia descendente
palabras_ordenadas = sorted(diccionario_palabras.items(), key=lambda x: x[1], reverse=True)

# Mostrar las 10 palabras más comunes en el archivo
print("Las 10 palabras más comunes en el archivo son:")
for i in range(10):
    print(palabras_ordenadas[i][0], "-", palabras_ordenadas[i][1])
