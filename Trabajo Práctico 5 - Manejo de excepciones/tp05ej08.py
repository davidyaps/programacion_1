
realizarCarga = True
while realizarCarga:
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: Los valores ingresados deben ser números enteros.")
    except ZeroDivisionError:
        print("Error: El segundo número no puede ser cero.")
    else:
        print(f"El resultado de la división es {resultado:.2f}")
        realizarCarga = False
    finally:
        print("Se ha intentado realizar una división.")
        
print("La división se realizó correctamente.")