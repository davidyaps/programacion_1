"""
1.	Crea un programa que vaya leyendo las frases que el usuario teclea y las guarde en un fichero de texto llamado 
“frases.txt”. Terminará cuando la frase introducida sea "fin" (esa frase no deberá guardarse en el fichero).
2.	En base al primer punto, luego de generar la carga de las frases, visualizar el archivo cargado.
"""
try:
    archivo = open("archivos/frases.txt", "w")

    frase = ""
    while (frase != "fin"):
        frase = input("Ingrese una frase: ")
        if (frase != "fin"):
            archivo.write(frase + "\n")

    archivo.close()
except Exception as e:
    print(f"Ha ocurrido el error {e}")

print("Contenido del archivo: ")
try:
    contenido = open("archivos/frases.txt", "r")
    caracteres = contenido.read()

    print(caracteres)
    contenido.close()
except FileNotFoundError:
    print("No existe el archivo")
