# Comparar los números 123 y 890, comprobar si tienen la misma paridad ambos pares o ambos impares

dato1 = 123
dato2 = 890

# son pares?
dato1 = (dato1%2 == 0)
dato2 = (dato2%2 == 0)

#print(dato1)
#print(dato2)
print("Los números tienen la misma paridad?", not((dato1 or dato2) and not(dato1 and dato2)))