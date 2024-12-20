"""
8.	Escriba una función recursiva (llamada secuencia) que reciba un valor numérico positivo y retorne ese número hasta 0 separados por guiones (-). Ejemplos:
print(secuencia(10)) -> 10-9-8-7-6-5-4-3-2-1-0
print(secuencia(5)) -> 5-4-3-2-1-0
"""
def secuencia(numero):
    if numero == 0:
        return "0"
    else:
        return str(numero) + "-" + secuencia(numero-1)

print(secuencia(10))
print(secuencia(5))