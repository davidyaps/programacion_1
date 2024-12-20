"""13.	Crea una función productoPares que acepte una lista de números como argumento y devuelva el producto de todos los números pares de la lista. Utiliza la función reduce y una función lambda para implementarla.
"""

from functools import reduce

productoPares = lambda numeros: reduce(lambda valor1, valor2: valor1*valor2, filter(lambda numero: numero%2==0, numeros))

print(productoPares([1, 2, 3, 4, 5]))  #8
