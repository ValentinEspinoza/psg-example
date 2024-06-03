# Crea un ciclo infinito que reciba un número por teclado y verifique si es un número primo, termina la ejecución si se ingresa el número 0

print('Ingrese una número para saber si es primo (Para finalizar escriba número "0"): ')
while 1:
    numero = int(input('Número: '))
    if numero <= 0:
        print('Finalizado.')
        break
    for x in range(2, numero):
        if numero % x == 0:
            print(f'{numero} No es primo.')
            break
    else: # solo se ejecuta si el bucle no se interrumpe con break
        print(f'{numero} es primo.✅')
