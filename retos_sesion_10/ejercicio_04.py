# Ahora quieren saber en que ciudades han estado ambos mochileros

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
"Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
"Argentina","Brasil","Panama","Bolivia"}

# lugares que ambos mochileros visitaron
ambos_visitado = mochilero_a.intersection(mochilero_b) 

print("Lugares que visitaron ambos mochileros:", '\n', ambos_visitado)
