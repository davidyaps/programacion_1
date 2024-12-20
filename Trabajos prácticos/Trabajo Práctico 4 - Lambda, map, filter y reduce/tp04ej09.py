"""9.	Crea una función filtraMayores que acepte una lista de números como argumento y devuelva una nueva lista con los números mayores que 5. Utiliza la función filter para implementarla."""

filtraMayores = lambda numeros: list(filter(lambda numero: numero > 5, numeros))

print(filtraMayores([1, 6, 2, 8, 3, 9]))  #[6, 8, 9]
