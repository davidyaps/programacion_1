"""
7.	Crear dos archivos:
	.: Paises.txt  Con el contenido de los países de Latinoamérica
	.: Provincias.txt  Con el contenido de las provincias de Argentina

Crear un programa que le pregunte al usuario si quiere ver los países o provincias, de acuerdo a su selección, debe mostrar su contenido en pantalla (que elija 1 o 2 con el teclado).

"""
try:
    opcion = int(input("¿Qué desea ver? 1. Países de Latinoamérica | 2. Provincias de Argentina: "))

    if (opcion != 1 and opcion != 2):
        raise ValueError("Opción incorrecta, debe ser 1 o 2")
    else:
        if (opcion == 1):
            archivo = "archivos/paises.txt"
        if (opcion == 2):
            archivo = "archivos/provincias.txt"

    contenido = open(archivo, "r", encoding="UTF-8")
    caracteres = contenido.read()

    print(caracteres)

    contenido.close()

except ValueError:
    print("Opción seleccionada incorrecta")
except FileNotFoundError:
    print("No existe el archivo")