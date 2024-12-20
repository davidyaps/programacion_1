"""12.	Crea una función ordenaPalabras que acepte una lista de palabras como argumento, y devuelva una nueva lista con las palabras ordenadas alfabéticamente en orden inverso. Utiliza funciones lambda, map y sorted para implementarla."""

ordenaPalabras = lambda palabras: list(map(lambda palabra : palabra[::-1], sorted(palabras, key=lambda palabra: palabra[::-1])))

print(ordenaPalabras(['Python', 'es', 'un', 'lenguaje', 'de', 'programación']))  #['ed', 'ejaugnel', 'nohtyP', 'nu', 'nóicamargorp', 'se']
