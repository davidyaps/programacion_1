"""
4.	Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. 
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

"""

def eliminarPalabras(listaOriginal, listaAEliminar):
    resultado = []
    for palabra in listaOriginal:
        if palabra not in listaAEliminar:
            resultado.append(palabra)
    
    return resultado

palabras = ["Hola", "Chau", "Adiós", "Buenas"]
palabrasEliminar = ["Hola", "Buenas"]

print (eliminarPalabras(palabras, palabrasEliminar))