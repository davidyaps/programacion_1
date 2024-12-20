"""4.	Escriba un programa Python para encontrar números divisibles por 3 de una lista de números usando Lambda."""

def contarDivisiblesPor(lista, divisor):
    return list(filter(lambda numero : numero % divisor == 0, lista))

def contarDivisiblesPor3(lista):
    return contarDivisiblesPor(lista, 3)

valores = [0, 1, 1, 2, 3, 5, 8, 13, 21]

print("Números divisibles por 3: ", contarDivisiblesPor3(valores))