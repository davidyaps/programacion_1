"""1.	Desarrolle un programa que almacene datos de canciones en formato MP3: 
Artista, Título, Duración (en segundos), Tamaño del fichero (en KB). 
Un programa debe pedir los datos de una canción al usuario y después mostrarlos en pantalla. 
Debe interrumpirse la carga cuando el artista ingresado sea vacío."""

canciones = []
artista = input("Ingrese artista: ")
while artista != "":
    cancion = {}
    cancion["artista"] = artista
    cancion["titulo"] = input("Ingrese título: ")
    cancion["duracion"] = int(input("Ingrese duración (seg): "))
    cancion["tamanio"] = float(input("Ingrese el tamaño (KB): "))
    
    canciones.append(cancion)
    
    artista = input("Ingrese artista: ")

for cancion in canciones:
    print(cancion["artista"],"-",cancion["titulo"])
    print(cancion["duracion"],"seg - ",cancion["tamanio"], "KB")
    print("===============================================")