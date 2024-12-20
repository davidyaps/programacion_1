"""8.	Crea una función doble que acepte una lista de números como argumento y devuelva una nueva lista con cada número multiplicado por dos. Utiliza la función map para implementarla."""

doble = lambda numeros: list(map(lambda numero: numero*2, numeros))

print(doble([1, 2, 3, 4, 5]))  #[2, 4, 6, 8, 10]