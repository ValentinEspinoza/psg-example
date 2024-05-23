# Crea un diccionario para almacenar información de comidas de animales por ejemplo

comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}

# Añade al diccionario de comidas 4 alimentos más usando update(clave=valor)

comidas.update(hierbas={'animales': ['vaca', 'jirafa']})
comidas.update(insectos={'animales': ['murcielago', 'oso hormiguero']})
comidas.update(semillas={'animales': ['Gorrión', 'Canario']})
comidas.update(flores={'animales': ['iguana', 'conejo']})

print('1. Añadiendo comidas al dict. -> ', comidas)
print()

# Existe en el diccionario de comidas la comida 'carne'?
buscar = 'carne'
print('2. Existe la comida "carne"?:', buscar in comidas)
print()

# Elimina la comida 'frutas' del diccionario de comidas
elimina = 'frutas'
comidas.pop(elimina)
print('3. Eliminando "frutas" del dict.:', comidas)
