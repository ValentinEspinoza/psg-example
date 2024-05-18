# Dos mochileros se encuentran en el Salar de Uyuni y se ponen a comparar la cantidad de lugares que han visitado
# Cada uno quiere saber en que parte del mundo ha estado el otro que el no haya visitado

mochilero_a = {"París", "Londres", "Nueva York", "Tokio",
"Peru", "Chile", "Colombia", "Bolivia"}

mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney",
"Argentina","Brasil","Panama","Bolivia"}

# lugares que 'A' no ha estado respecto a 'B'
por_visitar_moch_a = (mochilero_a | mochilero_b) - mochilero_a.intersection(mochilero_b) - mochilero_a

# lugares que 'B' no ha estado respecto a 'A'
por_visitar_moch_b = (mochilero_a | mochilero_b) - mochilero_a.intersection(mochilero_b) - mochilero_b

print("Lugares que el mochilero A no visito respecto del mochilero B:", '\n', por_visitar_moch_a)
print()
print("Lugares que el mochilero B no visito respecto del mochilero A:", '\n', por_visitar_moch_b)

