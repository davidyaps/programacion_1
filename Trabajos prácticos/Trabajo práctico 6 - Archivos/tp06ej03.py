"""
3.	Crear un archivo que se llame “montos.txt”, en el mismo se almacenarán valores numéricos. 
Realizar un proceso que visualice su contenido y, al finalizar, muestre el total (sumatoria de los valores) y promedio.
"""

try:
    contenido = open("archivos/montos.txt", "r")
    caracteres = contenido.read()
    montos = caracteres.split("\n")

    montos = list(map(float, montos))

    print("Sumatoria: ", sum(montos))
    print("Promedio: ", sum(montos)/len(montos))

    contenido.close()
except FileNotFoundError:
    print("No existe el archivo")