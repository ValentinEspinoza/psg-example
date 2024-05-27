# Crea una calculadora por consola que realice las operaciones de suma, resta, multiplicación y división, ingresa dos números y la operación a realizar, verifica si la operación es válida y muestra el resultado
# Número 1: 10
# Número 2: 5
# Operación: +
# -------------
# Resultado: 15

operaciones = ['+','-','*','/']
numero_1 = float(input('Número 1: '))
numero_2 = float(input('Número 2: '))
operador = input('Operación (+-*/): ')


if numero_2 == 0 and operador == '/':
    print('------------------------')
    print('La división entre cero es indeterminado.')
else:    
    if operador not in operaciones:
        print('------------------------')
        print('Ingrese un operador valido como ser + - * /')
        result = 0
    elif operador == '+':
        result = numero_1 + numero_2
    elif operador == '-':
        result = numero_1 - numero_2
    elif operador == '*':
        result = numero_1 * numero_2
    else:
        result = numero_1 / numero_2
        
    print('------------------------')
    print(f'Resultado: {round(result, 2)}')
