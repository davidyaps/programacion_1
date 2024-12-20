"""10.	Crea una función dobleSiEsPar que acepte una lista de números como argumento, devuelva una nueva lista con cada número multiplicado por dos si es par, y elimine todos los números impares de la lista. Utiliza funciones lambda, map y filter para implementarla."""

dobleSiEsPar = lambda numeros: list(map(lambda numero: numero*2, filter(lambda numero: numero%2==0, numeros)))

print(dobleSiEsPar([1, 2, 3, 4, 5]))  #[4, 8]
