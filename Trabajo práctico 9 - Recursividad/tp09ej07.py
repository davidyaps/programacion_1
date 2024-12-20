"""
7.	Programe una función recursiva para verificar si una palabra es un palíndromo.
"""
def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return palindromo(palabra[1:-1])

print(palindromo('radar'))  #True
print(palindromo('python'))  #False
