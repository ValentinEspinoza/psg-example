# Imprimir los 20 primeros números de la serie de Fibonacci
#1 1 2 3 5 8 13 21
n = 20
num_1 = 0 
num_2 = 1

print(f'Serie Fibonacci para {n} primeros números:')
for i in range(n):
    aux = num_1 + num_2
    num_1 = num_2
    num_2 = aux
    print(num_1, end=' ')
