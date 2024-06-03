# Crea un ciclo infinito que reciba una palabra por teclado y verifique si es palíndrome, termina la ejecución si se ingresa la palabra salir

print('Ingrese una palabra para saber si es palindromo (Para finalizar escriba "salir"): ')
while 1:
    palabra = list(input('Palabra: ').lower())
    palabra_2 = palabra.copy()
    palabra_2.reverse()
    palabra_2 = "".join(palabra_2)
    palabra = "".join(palabra)
    if palabra == 'salir':
        print('Finalizado.')
        break
    elif(palabra == palabra_2):
        print(f'{palabra} es palindromo.')
    else:
        print(f'{palabra} NO es palindromo.')
