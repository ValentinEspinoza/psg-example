# Simular un cajero automático que solicite un monto a retirar, si el monto es mayor al saldo lanzar una excepción personalizada y si el monto es mayor a 1000 lanzar una excepción genérica

saldo_disponible = 855 # Bs.

print('Bienvenido a BANCO ALASITA 🏦\nMódulo Retiro de Dinero: \n')
print('Ingrese "salir" para finalizar.\n')

class saldoInsuficiente(Exception):
    pass

class montoExcedido(Exception):
    pass

while 1:
    try:
        monto = input('Monto a retirar: ')
        #validación para salir
        if monto == 'salir':
            print('🔚 Finalizando...')
            break
        
        monto = int(monto)
        #Validación del monto ingresado
        if monto > saldo_disponible:
            raise saldoInsuficiente()
        elif monto > 1000:
            raise montoExcedido()
        else:
            saldo_disponible -= monto
            print('🏧 Procesando... \nRetire el dinero... 💵')
            print(f'Retiro exitoso ✅ \nSaldo actual: {saldo_disponible}')
            print('🔚 Finalizando...')
            break

    except KeyboardInterrupt:
        print('🚫 Para finalizar escriba "salir"')

    except saldoInsuficiente:
        print('❌ No es posible retirar el monto indicado, Saldo insuficiente. Intente nuevamente... \n')
    
    except montoExcedido:
        print('❌ No es posible retirar más de 1000 Bs., Limite de retiro. Intente nuevamente...\n')
    except Exception:
        print('❌ No es posible reconocer el monto. Intente nuevamente...\n')