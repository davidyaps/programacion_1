"""
 4.	Crear un programa que maneje un archivo donde se almacena la siguiente información de una determinada cantidad personas:
 Nombre, Apellido, Edad y Estatura. El programa deberá almacenar la información a medida que se vayan cargando. 
 El formato a ser almacenado será cada dato separado por el carácter punto y coma (;) en el mismo orden que se carga. 
 Tenga en cuenta que cada vez que se ejecuta el programa, se debe incrementar el contenido del archivo (agregar al final).
"""
snABoolean = lambda sn : sn == 'S' or sn == 's'

try:
    archivo = open("archivos/personas.txt", "a")

    continuar = True

    while (continuar):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad = input("Ingrese la edad: ")
        estatura = input("Ingrese la estatura: ")

        archivo.write(f"{nombre};{apellido};{edad};{estatura}\n")

        continuar = snABoolean(input("¿Desea continuar? (S/N): "))

    archivo.close()
except Exception as e:
    print(f"Ocurrió el siguiente error: {e}")