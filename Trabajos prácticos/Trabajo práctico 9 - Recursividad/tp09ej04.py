"""
4.	Desarrollar una función que reciba un número binario y lo devuelva convertido a base decimal.
"""

def binarioADecimal(binario):
    if binario == 0:
        return 0
    else:
        return (binario % 10 + 2 * binarioADecimal(binario//10))

print(binarioADecimal(1))
print(binarioADecimal(10))
print(binarioADecimal(101))
print(binarioADecimal(111))
print(binarioADecimal(100000))