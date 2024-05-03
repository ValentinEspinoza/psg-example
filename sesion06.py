#Datos booleanos
print ("Tipos de datos booleanos")
print (True)
print (False)


print (True + True)
print (True * True)
print (True * False)
print (False + False)
print (False * False)


print ("Números y booleanos")
print (10 + True)
print (10 + False)

print (10 * True)
print (10 * False)

print ("Declarar variables booleanas")
var_booleana = True
print (var_booleana)
print (type(var_booleana))


var_booleana = False
print (var_booleana)
print (type(var_booleana))

print ("Declarar mediante función bool()")
var_booleana = bool(1)
print (var_booleana)
print (type(var_booleana))

var_booleana = bool(0)
print (var_booleana)
print (type(var_booleana))

var_booleana = bool(15)
print (var_booleana)
print (type(var_booleana))


print ("Operadores de comparación")
print (10 == 10)
print (10 != 10)
print (10 < 10)
print (10 > 10)
print (10 <= 10)
print (10 >= 10)
print (10 is 10)
print (10 is not 10)
print (10 is 10.0)
print (10 is not 10.0)


print ("Asignación de variables")
x = 10
mayor_que_cero = x > 0
print (mayor_que_cero)
diferente_de_10 = x != 10
print (diferente_de_10)


print ("Operadores lógicos")
print (True and True)
print (True and False)
print (False or True)
print (False or False)
print (not True)
print (not False)

print ("Operadores lógicos y prioridad")
print (False and False or True)
print (False and (False or True))
print (not True and False or True)
print (not (True and False or False))
print (not True and (False or False))
print (not True and False or False)


print ("Operador AND")
print (True and True)
print (True and False)
print (False and True)
print (False and False)


print ("Operador OR")
print (True or True)
print (True or False)
print (False or True)
print (False or False)


print ("Operador NOT")
print (not True)
print (not False)
print ("Operador NAND")
print (not (True and True))
print (not (True and False))
print (not (False and True))
print (not (False and False))


print ("Operador NOR")
print (not (True or True))
print (not (True or False))
print (not (False or True))
print (not (False or False))


print ("Operador XOR")
a = True
b = False
print ((a or b) and not (a and b))
a = True
b = True
print ((a or b) and not (a and b))



print ("Ejemplo de uso Sensor y Batería")
sensor = True
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = True
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)

##reto
print ("Ejemplo 1 - Comparación y Lógicos")
numero = 20
print (numero >= 0 and numero <= 100)

numero = 20
print(numero >= 0 and numero <= 100)

## reto
print ("Ejemplo 2 - Aritméticos y comparación")
nota1 = 15
nota2 = 20
nota3 = 16
print ((nota1 + nota2 + nota3) > 50)

##reto
num = 15
print((num%3==0) and (num%5==0) and (num%2!=0))

print ("Ejemplo 3 - Aritméticos, comparación y lógicos")
numero = 15
print ((numero % 3 ==0) and (numero % 5 ==0) and (numero % 2 !=0))



print ("Cortocircuito con operador and")
x = 1
y = 0
print (x > 2 and (x/y) > 2)
## print (x > 0 and (x/y) > 0)
print (x > 0 or (x/y) > 0)


