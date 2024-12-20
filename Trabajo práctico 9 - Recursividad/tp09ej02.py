"""
2.	Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.
"""

def multiplicacion(a, b):
    if b == 0:  
        return 0
    elif b > 0: 
        return a + multiplicacion(a, b-1)
    else:  
        return -multiplicacion(a, -b)


print("0 x 3 = ", multiplicacion(0,3))
print("3 x 0 = ", multiplicacion(3,0))
print("2 x 2 = ", multiplicacion(2,2))
print("11 x 22 = ", multiplicacion(11,22))
print("-11 x -22 = ", multiplicacion(-11,-22))
print("-11 x 3 = ", multiplicacion(-11, 3))
print("11 x -3 = ", multiplicacion(11, -3))