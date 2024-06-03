# Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *

for x in range (1,9):
    if x%2 == 0:
        for y in range(1,9):
            print('#' if y%2==0 else '*', end='')
        print()
    else:
        for y in range(1,9):
            print('*' if y%2==0 else '#', end='')
        print()
