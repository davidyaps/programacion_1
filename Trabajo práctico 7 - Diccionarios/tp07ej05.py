"""
5.	Se debe gestionar los datos de stock de una tienda de comestibles, la información a recoger será: nombre del producto, precio, cantidad en stock. La tienda dispone de 10 productos distintos. El programa debe ser capaz de:
	Dar de alta un producto nuevo.
	Buscar un producto por su nombre.
	Modificar el stock y precio de un producto dado.
"""

def mostrarMenu():
    print("1. Dar de alta un producto")
    print("2. Buscar un producto")
    print("3. Modificar stock y precio de un producto")
    print("")
    print("0. Salir")


def nuevoProducto(nombre, precio, cantidad):
    producto = {}
    producto["nombre"] = nombre
    producto["precio"] = precio
    producto["cantidad"] = cantidad

    return producto

def listarProductos(productos, nombre):
    if len(productos) > 0:
        for producto in productos:
            if producto["nombre"] == nombre:
                print("Nombre del producto: ", producto["nombre"])
                print("Precio: $", producto["precio"])
                print("cantidad: ", producto["cantidad"])
    else:
        print("No hay productos cargados")


def modificarProducto(productos, nombre, precio, cantidad):
    for producto in productos:
        if producto["nombre"] == nombre:
            producto["precio"] = precio
            producto["cantidad"] = cantidad


def existeProducto(productos, nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            return True
    return False


opcion = -1
productos = []

while opcion != 0:
    mostrarMenu()
    opcion = int(input("Ingrese opción de menú: "))

    if opcion == 1:
        if len(productos) <= 10:
            nombre = input("Ingrese nombre del producto: ")
            precio = float(input("Ingrese el precio: $"))
            cantidad = int(input("Ingrese cantidad: "))
            producto = nuevoProducto(nombre, precio, cantidad)
            productos.append(producto)
        else:
            print("Se han cargado la cantidad máxima de productos (10)")
    if opcion == 2:
        nombre = input("Ingrese nombre del producto a buscar: ")
        listarProductos(productos, nombre)
    if opcion == 3:
        nombre = input("Ingrese nombre del producto a modificar: ")
        if (existeProducto(productos, nombre)):
            precio = float(input("Ingrese el precio a modificar: $"))
            cantidad = int(input("Ingrese cantidad: "))
            modificarProducto(productos, nombre, precio, cantidad)
        else:
            print("No existe el producto ingresaro")

    print("============================================")