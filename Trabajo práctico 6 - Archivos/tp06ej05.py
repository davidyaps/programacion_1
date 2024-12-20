"""
5.	Crear un programa que permita recuperar la información del archivo generado y muestre los promedios de edad y estaturas.
Muestre todos los datos al procesar.
"""
try:
    contenido = open("archivos/personas.txt", "r")
    caracteres = contenido.read()

    registros = caracteres.split("\n")

    edades = []
    estaturas = []

    edadMasAlta = 0
    estaturaMasAlta = 0

    print("Nombre\tApellido\tEdad\tEstatura")
    for registro in registros:
        if (registro != ""):
            nombre, apellido, edad, estatura = registro.split(";")
            print(f"{nombre}\t{apellido}\t{edad}\t{estatura}")
            edades.append(edad)
            estaturas.append(estatura)
        
    edades = list(map(lambda valor : float(valor), edades))
    estaturas = list(map(lambda valor : float(valor), estaturas))

    print("")
    print(f"Promedio de edad: {sum(edades)/len(edades)}")
    print(f"Promedio de estaturas: {sum(estaturas)/len(estaturas)}")

    contenido.close()
except FileNotFoundError:
    print("No existe el archivo")