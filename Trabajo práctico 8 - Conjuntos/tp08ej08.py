"""8.	Contar elementos únicos en una lista: Crea una función que tome una lista como argumento y devuelva el número de elementos únicos en la lista."""
def contarElementosUnicos(lista):
    return len(set(lista))
    
lista = [1, 2, 3, 2, 4, 1]
print(f"Cantidad de elementos únicos: {contarElementosUnicos(lista)}")
      
