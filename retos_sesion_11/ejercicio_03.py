#  Crea un diccionario con las siguientes tuplas de animales
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))

animales = dict(tupla) #convertido a diccionario
print('Nuevo diccionario ->', animales)

# Del diccionario obtén y elimina el valor de la clave 'aves'
aves = animales.get('aves')
print('1. Aves->', aves)
animales.pop('aves')
print('1. Diccionario ->', animales)
print()

# Modifica el valor de la clave 'gato' por '🐈'
valor_new_gato = '🐈'
animales['gato'] = valor_new_gato
print('2. Dict. modificado ->', animales)
print()

# Cambia la clave perro por perros y su valor por ['🐶','🐕']
valor_new_perro = ['🐶','🐕']
animales['perro'] = valor_new_perro
print('3. Dict. modificado ->', animales)
