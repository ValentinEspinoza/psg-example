# Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies
arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}

# Añade al arca 2 especies más usando update()
agrega = {'elefante': 2, 'pinguino': 2}
arca.update(agrega)
print('1. Añadiendo especies al arca ->', arca)
print()

# Toma lista de los animales en el arca iterando el diccionario
iterador = iter(arca.items())
print('2. Tomando lista...') #8

siguiente = next(iterador) #1
print(siguiente)
siguiente = next(iterador) #2
print(siguiente)
siguiente = next(iterador) #3
print(siguiente)
siguiente = next(iterador) #4
print(siguiente)
siguiente = next(iterador) #5
print(siguiente)
siguiente = next(iterador) #6
print(siguiente)
siguiente = next(iterador) #7
print(siguiente)
siguiente = next(iterador) #8
print(siguiente)
print()

# Existe en el arca la especie 'dragon'?
buscar = 'dragon'
print('3. Existe la especie "dragon"?:', buscar in arca)
print()

# Elimina la especie 'unicornio' del arca
elimina = 'unicornio'
arca.pop(elimina)
print('4. Eliminando "unicornio" del arca:', arca)
print()

# Modifica el valor de la especie 'jirafa' por 2
arca['jirafa'] = 2
print('5. Modificando valor "jirafa":', arca)
print()

# Vacía el arca después del diluvio
arca.clear()
print('6. Arca después del diluvio":', arca)
