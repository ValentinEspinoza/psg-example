# Imprimir los 20 primeros números primos

cantidad = 20
num_primo = []
numero = 2
# 20 primeros numeros primos
while len(num_primo) < cantidad:
    for x in range(2, numero):
        if numero % x == 0:
            break
    else: # solo se ejecuta si el bucle no se interrumpe con break
        num_primo.append(numero)
        print(numero, end=' ')
    numero += 1
