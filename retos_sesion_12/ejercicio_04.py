# Una tienda ofrece descuentos a sus clientes, si el cliente es mayor de edad y tiene una compra mayor a 1000, se le aplica un descuento del 10%, si es menor de edad y tiene una compra mayor a 500 se le aplica un descuento del 5%, si no cumple ninguna condición se le aplica un descuento del 2%

edad = int(input('Ingrese su edad: '))
monto_compra = float(input('Ingrese el monto de la compra: '))

if edad >=18 and monto_compra > 1000:
    print('Se le aplica un descuento del 10%')
elif edad < 18 and monto_compra > 500:
    print('Se le aplica un descuento del 5%')
else:
    print('Se le aplica un descuento del 2%')
