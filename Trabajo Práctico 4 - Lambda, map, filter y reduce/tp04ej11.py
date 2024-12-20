"""11.	Crea una función esDivisible que acepte un número como argumento, y una lista de números, y devuelva una nueva lista con los números de la lista que son divisibles por el número dado. Utiliza funciones lambda y filter para implementarla."""

esDivisible = lambda divisor, numeros: list(filter(lambda numero : numero % divisor == 0, numeros))

print(esDivisible(3, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  #[3, 6, 9]
