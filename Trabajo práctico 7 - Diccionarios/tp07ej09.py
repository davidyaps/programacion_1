"""9.	Supongamos que un coleccionista de figuras Funko Pop de Rick y Morty tiene un carrito de compras con las siguientes figuras y sus respectivas cantidades:

carrito = { 
    "Rick Sanchez" : 2, 
    "Morty Smith" : 3, 
    "Summer Smith" : 1,
    "Mr. Meeseeks" : 4
}


Y además, el coleccionista conoce los precios unitarios (en dólares) de estas figuras:

precios = {
    "Rick Sanchez" : 15,   
    "Morty Smith" : 12,
    "Summer Smith" : 10,
    "Mr. Meeseeks" : 20
}

Cree una función llamada precioTotal que calculará el monto total de la compra en función de estos datos. Cuando se llame a la función precioTotal(carrito, precios) con los diccionarios proporcionados, se debe obtener el monto total de la compra basado en la multiplicación de la cantidad de cada figura por su precio unitario en dólares.
"""

def precioTotal(carrito, precios):
    total = 0
    for figura, cantidad in carrito.items():
        if figura in precios:
            total += precios[figura] * cantidad
        else:
            print(f"No se encontró el precio de {figura} en la lista de precios.")
    return total


carrito = { 
    "Rick Sanchez" : 2, 
    "Morty Smith" : 3, 
    "Summer Smith" : 1,
    "Mr. Meeseeks" : 4
}

precios = {
    "Rick Sanchez" : 15,   
    "Morty Smith" : 12,
    "Summer Smith" : 10,
    "Mr. Meeseeks" : 20
}

total = precioTotal(carrito, precios)
print(f"El monto total de la compra es: ${total}")

