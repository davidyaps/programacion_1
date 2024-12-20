"""14.	Crea una función masCorto que acepte una lista de strings como argumento y devuelva el string más corto de la lista. Utiliza la función reduce y una función lambda para implementarla."""

from functools import reduce

masCorto = lambda palabras: reduce(lambda x, y: x if len(x) < len(y) else y, palabras)

# Ejemplo de uso
print(masCorto(['Python', 'es', 'un', 'lenguaje', 'de', 'programación']))  #'de'
