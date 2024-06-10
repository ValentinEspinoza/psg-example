# Crear una función que reciba una lista de números y devuelva solo los números pares

import random

def genera_num_aleatorios (hasta, rango_lista):
    """
    Genera números aleatorios enteros:
    rango de números: (0, hasta)
    Tamaño lista: rango_lista 
    """
    num_int = [random.randint(0, hasta) for x in range(rango_lista)]
    return num_int

numeros = genera_num_aleatorios(2024, 100) # rango: (0 - 2024) y tamaño lista: 100

def num_pares(lista):
    pares = [] 
    for i in lista:
        if i%2 == 0:
            pares.append(i) # almacena solo numeros pares
    return pares

print(f'Los números pares son: \n {num_pares(numeros)}')
print(f'Tamaño de la lista de números pares: {len(num_pares(numeros))}')