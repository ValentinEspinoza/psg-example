# Calculadora flexible: Crea una calculadora que acepte diferentes operaciones matemáticas como argumentos de palabras clave y realice los cálculos correspondientes, las operaciones son suma, resta, multiplicación y división

print('Calculadora -> On')
numeros = []

def calculadora (**datos):
    """
    Realiza la operación solicitada a una serie de números ingresada previamente.
    """
    resultado = 0
    if 'dividir' in datos:
        resultado = datos['dividir'][0]
        for i in datos['dividir'][1:]:
            if i == 0:
                return 'La división entre cero es indeterminado'
            resultado /= i
            return f'División = {round(resultado, 2)}'

    elif 'sumar' in datos:
        resultado = sum(datos['sumar'])
        return f'Suma = {resultado}'

    elif 'restar' in datos:
        resultado = datos['restar'][0]
        for i in datos['restar'][1:]:
            resultado -= i
        return f'Resta = {resultado}'

    else:
        resultado = 1
        for i in datos['multiplicar']:
            resultado *= i
        return f'Multiplicación = {round(resultado, 2)}'


def lista_numeros():
    """
    Solicita la serie de números a procesar.
    """
    print('Ingrese los números:')
    print('Presione "=" para finalizar') 
    while 1:
        num_nuevo = input('Número >> ')
        if num_nuevo == '=': # finaliza la solicitud de números
            print('Calculando...')
            break
        else:
            num_nuevo = float(num_nuevo)
            numeros.append(num_nuevo)


lista_numeros()
# Solicita a la función calculadora procesar segun requerimiento y lista de números
print(calculadora(sumar = numeros))
print(calculadora(restar = numeros))
print(calculadora(multiplicar = numeros))
print(calculadora(dividir = numeros))

print('Calculadora -> Off')                                    