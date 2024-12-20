"""
18.	Crear una función recursiva llamada ocurrenciasLetra(cadena, letra) que cuente y devuelva la cantidad de veces que una letra específica aparece en una cadena de texto dada. 
cadena = "La ciencia es más arte que ciencia"
letra = "a"
resultado esperado: 4
"""
def ocurrenciasLetra(cadena, letra):
    if len(cadena) == 0:
        return 0
    else:
        if cadena[0] == letra:
            return 1 + ocurrenciasLetra(cadena[1:], letra)
        else:
            return 0 + ocurrenciasLetra(cadena[1:], letra)


cadena = "La ciencia es más arte que ciencia"
letra = "a"
print(ocurrenciasLetra(cadena, letra))