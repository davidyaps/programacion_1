"""
5.	Desarrollar una función que extraiga una subcadena de una cadena de caracteres, indicando la posición y la 
cantidad de caracteres deseada. Devolver la subcadena como valor de retorno. 
Escribir también un programa para verificar el comporta- miento de la misma. 
Ejemplo, dada la cadena "El número de teléfono es 4356- 7890" extraer la subcadena que comienza en la posición 25 
y tiene 9 caracteres, resultando la subcadena "4356-7890". Escribir una función utilizando rebanadas.
"""

def extraer (cadena, comienzo, longitud):
    return cadena[comienzo:comienzo+longitud]

print (extraer("El número de teléfono es 4356-7890", 25, 9))
