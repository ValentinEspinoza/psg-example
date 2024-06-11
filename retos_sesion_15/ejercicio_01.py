# Crear una calculadora que solicite dos números y realice las operaciones básicas de suma, resta, multiplicación y división con manejo de excepciones, para salir del programa se debe ingresar "salir"

print('CALCULADORA 🧮 \nIngresa dos números y luego la operación requerida ( + - * / ) \nIngrese "salir" para finalizar:\n')
operaciones = ('+', '-', '*', '/')

class error_cero(ZeroDivisionError):
    pass

while 1:
    try: 
        num_1 = input("Ingresa el primer número: ")
        #Finaliza el bucle si ingresa 'salir'
        if num_1.lower() == "salir":
            print('🔚 Finalizando...')
            break
        num_2 = input("Ingresa el segundo número: ")
        if num_2.lower() == "salir":
            print('🔚 Finalizando...')
            break
        #Convierte a float 
        num_1 = float(num_1)
        num_2 = float(num_2)
        
        #Valida el operador ingresado
        while 1:
            operador = input('Ingrese la operación (+ - * /): ')
            if operador in operaciones:
                break
            else:
                print('❌ Ingrese un operador válido. Ej. + - * / ')
            
        #Realiza las operaciones
        if operador == '+':
            resultado = num_1 + num_2
        elif operador == '-':
            resultado = num_1 - num_2
        elif operador == '*':
            resultado = num_1 * num_2
        elif num_2 != 0: 
            resultado = num_1 / num_2   
        else:
            raise error_cero()
        

        print(f'🧮Resultado: {round(resultado,2)}\n')
    
    except KeyboardInterrupt:
        print('🚫 Para salir escriba "salir"')
        
    except ZeroDivisionError:
        print('❌ No es posible realizar la división entre cero "0". \n')

    except Exception:
        print('⚠️ Por favor ingresa números válidos...\n')
    