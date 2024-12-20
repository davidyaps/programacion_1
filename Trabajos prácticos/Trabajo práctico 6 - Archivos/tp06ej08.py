"""8.	Escribe un programa que lea un archivo CSV con información sobre ventas de una tienda (los valores serán fecha, producto, precio, cantidad por cada fila; por ejemplo: 01/01/2023,Pantalones,50,10). El programa debe calcular el total de ventas y el promedio de ventas por día."""

def acumularValores(matriz, fecha, monto):
    acumulado = matriz.copy()
    existe = False

    for i in range(0, len(matriz)):
        if fecha == acumulado[i][0]:
            acumulado[i][1] += monto
            existe = True
    
    if not existe:
        acumulado.append([fecha, monto])
    
    return acumulado

def imprimirTotalVentas(matriz):
    print(f"DÍA\tTOTAL")
    for i in range(0, len(matriz)):
        print(f"{matriz[i][0]}\t${matriz[i][1]}")

try:
    contenido = open("archivos/ventas.csv")

    caracteres = contenido.read()
    ventas = caracteres.split("\n")
    
    resultado = []
    for venta in ventas:
        fecha, producto, precio, cantidad  = venta.split(",")
        resultado = acumularValores(resultado, fecha, float(precio)*float(cantidad))

    imprimirTotalVentas(resultado)
    contenido.close()

except FileNotFoundError:
    print("No se encontró el archivo")