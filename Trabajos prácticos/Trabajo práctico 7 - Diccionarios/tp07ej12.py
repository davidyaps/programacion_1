def coloresFaltantes (colores, banderas):
    resultado = {}
    for pais, coloresBandera in banderas.items():
        resultado[pais] = list(coloresBandera.difference(colores))
        
    return resultado


def banderasPosibles(colores, banderas): 
    resultado = []
    for pais, coloresBandera in banderas.items():
        if coloresBandera.intersection(colores) == coloresBandera:
            resultado.append(pais) 
        
    return resultado


colores = { "azul", "blanco", "rojo"}

banderas = {
    "Argentina" : { "blanco", "celeste" },
    "Francia" : { "azul", "blanco", "rojo"},
    "Polonia" : { "blanco", "rojo"}
}


print (f"Banderas posibles: {banderasPosibles(colores, banderas)}")
print (f"Colores de banderas faltantes: {coloresFaltantes(colores, banderas)}")