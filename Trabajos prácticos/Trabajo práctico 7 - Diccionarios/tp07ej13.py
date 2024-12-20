
def recetasPosibles (ingredientes, recetas):
    listaRecetas = []
    for receta, recetaIngredientes in recetas.items():
        if ingredientes.intersection(recetaIngredientes) == recetaIngredientes:
            listaRecetas.append(receta)

    return listaRecetas

def ingredientesFaltantes(ingredientes, recetas):
    resultado = {}
    for receta, recetaIngredientes in recetas.items():
        resultado[receta] = list(recetaIngredientes.difference(ingredientes))

    return resultado            



ingredientes = { "huevo", "aceite", "papas"}

recetas = {
    "Papas fritas" : { "aceite", "papas" },
    "Huevo frito" : { "huevo", "aceite" },
    "Pure de papas" : { "papas", "manteca" }
}

print(recetasPosibles (ingredientes, recetas))

print(ingredientesFaltantes(ingredientes, recetas))