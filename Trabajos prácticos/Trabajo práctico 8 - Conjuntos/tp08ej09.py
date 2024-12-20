"""9.	Crear una lista de valores únicos a partir de un diccionario: Crea una función que tome un diccionario como argumento y devuelva una lista con los valores únicos del diccionario."""

def valoresUnicos(diccionario):
    conjunto = set(diccionario.values())
    lista = list(conjunto)
    return lista
    
diccionario = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
print(f"Valores únicos del diccionario: {valoresUnicos(diccionario)}")
