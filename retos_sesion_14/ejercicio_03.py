# Crear una función recursiva para obtener el N número de la serie de Fibonacci
# 1, 1, 2, 3, 5, 8, 13, 21, 34

posicion = int(input('Posición requerida en la serie de Fibonacci: '))

def serie_fibonnaci(posicion):
    """
    Devuelve el N número de la posición requerida en la serie de Fibanacci.
    """
    if posicion == 0:
        return 0
    elif posicion == 1: 
        return 1
    else: 
        return serie_fibonnaci(posicion-1) + serie_fibonnaci(posicion-2)


result = serie_fibonnaci(posicion)
print(f'Posición {posicion}°: {result}')
