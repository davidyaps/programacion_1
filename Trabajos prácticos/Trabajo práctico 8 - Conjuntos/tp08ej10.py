"""10.	Eliminar elementos comunes de un diccionario: Crea una función que tome dos diccionarios como argumentos y devuelva un nuevo diccionario que contenga solo las claves del primer diccionario que no estén en el segundo diccionario."""


def eliminarElementosComunes(diccionario1, diccionario2):
    conjunto = set(diccionario2.keys())
    nuevoDiccionario = {clave: valor for clave, valor in diccionario1.items() if clave not in conjunto}
    return nuevoDiccionario
    
diccionario1 = {'a': 1, 'b': 2, 'c': 3}
diccionario2 = {'b': 4, 'c': 5, 'd': 6}
resultado = eliminarElementosComunes(diccionario1, diccionario2)
print(f"Resultado: {resultado}") 