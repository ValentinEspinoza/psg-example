# Depuración
# Debug en Visual Studio Code

def suma(a, b):
    c = a + b
    return c

def resta_final(x,y):
    return x-y

def resta(a, b):
    return resta_final(a,b)


def multiplicacion(x, y):
    z = x * y
    return z

def division(x, y):
    return x / y

def division_controlada(x,y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return "Division entre cero"

a = 11
b = 1
print (suma(a, b))
print (resta(a, b))
print (multiplicacion(a, b))
print (division_controlada(a, b))
print (division(a, b))