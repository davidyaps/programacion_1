"""
Se tienen dos variables del tipo diccionario, en una de ella se almacena la información de los artículos y la cantidad que tiene una persona en un carrito de compras:
carrito = { 
"lapiceras" : 12, 
"borrador" : 1, 
"carpeta" : 2
}

En una segunda variable, se almacenan el stock (cantidad de artículos disponibles) de cada uno de los artículos:
stock = {
"lapiceras" : 13, 
"borrador" : 10, 
"carpeta" : 1
}

En función de dicha información, deberá elaborar la siguiente función: 
 
•	hayStock(articulo, cantidad, stock): Recibe un articulo y verifica si hay stock disponible (True o False)
•	procesarPedido(carrito, stock): Recibe los artículos solicitados en carrito y realiza el descuento de stock correspondiente. Debe retonar como resultado el stock actualizado. No afectar la varible recibida como parámentro.
"""

def hayStock(articulo, cantidad, stock):
    return stock[articulo] >= cantidad

def procesarPedido(carrito, stock):
    stockActualizado = stock.copy()
    for articulo, cantidad in carrito.items():
        stockActualizado[articulo] -= cantidad

    return stockActualizado


carrito = { 
        "lapiceras" : 12, 
        "borrador" : 1, 
        "carpeta" : 2
        }

stock = {
        "lapiceras" : 13, 
        "borrador" : 10, 
        "carpeta" : 3
        }

print("¿Hay 1 unidad de borrador?:", hayStock("borrador", 1, stock))
print("¿Hay 13 unidad de borrador?:", hayStock("borrador", 13, stock))

print(procesarPedido(carrito, stock))