# Agregar 5 Ejemplos con otras funciones no vistas en la sesión

# 1. Método partition()
# Este método busca la primera ocurrencia de la cadena especificada.
frase = "Yo debo comer licuado de banana todos los días"
particion = frase.partition("banana")
print(particion) # ('Yo debo comer licuado de ', 'banana', ' todos los días')


# 2. Método index()
oracion = "Yo debo comer licuado de banana todos los días"
index_oracion = oracion.index("licuado")
print(index_oracion)


# 3. Método splitlines() 
# Divide una cadena en una lista donde cada línea sea un elemento de lista
frase_2 = "Yo debo comer \nlicuado de banana \ntodos los días"
splitliness = frase_2.splitlines()
print(splitliness)


# 4. Método expandtabs() 
# Devuelve una cadena en la que todos los caracteres '\t' se reemplazan por caracteres de espacio en blanco hasta el siguiente múltiplo del parámetro.
cadena = "xyz\t12345\tabc"
print('Original cadena:', cadena)

# tabsize is set to 2
print('Tabsize 2:', cadena.expandtabs(2))

# tabsize is set to 3
print('Tabsize 3:', cadena.expandtabs(3))

# tabsize is set to 4
print('Tabsize 4:', cadena.expandtabs(4))

# tabsize is set to 5
print('Tabsize 5:', cadena.expandtabs(5))

# tabsize is set to 6
print('Tabsize 6:', cadena.expandtabs(6))


# 5. Método endswith() 
# endswith() con parámetros start y end
texto = "Python programming is easy to learn."
# start parameter: 7
# "programming is easy to learn." string is searched
result = texto.endswith('learn.', 7)
print(result)
# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched
result = texto.endswith('is', 7, 26)
# Returns False
print(result)
result = texto.endswith('easy', 7, 26)
# returns True
print(result)
