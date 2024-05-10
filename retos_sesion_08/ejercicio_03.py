# Ingresa una cadena por teclado y almacena el valor en una tupla

cadena = tuple(input("Ingresa una oración: "))

concatenado = ('¡',) + cadena + ('!',)
print(concatenado)

concatenado_2 = concatenado * 3
print(concatenado_2)
