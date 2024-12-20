"""
5.	Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma 
ascendente o False en caso contrario. 
Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa 
para verificar el comportamiento de la función.
"""

def listaOrdenada(lista):
    ordenada = lista.copy()
    ordenada.sort()
    if lista == ordenada:
        return True
    return False

print("[1, 2, 3] esta ordenada: ", listaOrdenada([1, 2, 3]))
print("['b', 'a'] esta ordenada: ", listaOrdenada(['b', 'a']))