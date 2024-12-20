"""
1.	Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento 
imprimiendo la lista luego de invocar a cada función:
a.	Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos. Realice la composición de la lista por comprensión y de la forma habitual (tendrá dos funciones distintas).
b.	Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c.	Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
d.	Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. 
Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

"""

import random

def listaAlAzar():
    lista = []
    for i in range(0, random.randint(10, 99)):
        lista.append(random.randint(1000, 9999))
    
    return lista

def listaAlAzarComprension():
    return [ random.randint(1000, 9999) for i in range(0, random.randint(10, 99)) ]

def sumatoria(lista):
    return(sum(lista))

def eliminarValor(lista, valor):
    return [ elemento for elemento in lista if elemento != valor ]

def esCapicua(lista):
    return lista == lista[::-1]

print("listaAlAzar: ", listaAlAzar())
print("listaAlAzarComprension: ", listaAlAzarComprension())
print("Sumatoria: ", sumatoria(listaAlAzarComprension()))

lista = [50, 17, 91, 17, 50]
print ("Eliminar valor 50: ", eliminarValor(lista, 50), lista)
print ("Es capicúa: ", esCapicua(lista))
