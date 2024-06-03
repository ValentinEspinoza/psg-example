# Crear una serie de números del 1 al 100, si el número es divisible por 3 imprimir Fizz, si el número es divisible por 5 imprimir Buzz, si el número es divisible por 3 y 5 imprimir FizzBuzz

serie = [x+1 for x in range(0,100)]

for y in range(0, len(serie)):
    if serie[y]%3 == serie[y]%5 == 0:
        print(f'{y+1}: FizzBuzz')
    elif serie[y]%3==0:
        print(f'{y+1}: Fizz')
    elif  serie[y]%5==0:
        print(f'{y+1}: Buzz')
