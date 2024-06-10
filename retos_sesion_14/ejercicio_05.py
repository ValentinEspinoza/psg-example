# Crear una función que reciba una cadena y devuelva la cadena invertida

cadena = input('Escriba la cadena: \n >> ')

def invertir_cadena(cadena):
    """
    Invierte una cadena desde el ultimo caracter hasta el primero.
    """
    cadena = list(cadena)
    inverso = cadena[::-1]
    return "".join(inverso)

invertido = invertir_cadena(cadena)
print(f'La cadena invertida es: \n {invertido}')
