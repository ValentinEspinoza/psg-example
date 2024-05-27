# Crear un script que pida un número entero y verifique si es par o impar usando operador ternario

numero = int(input('Escriba un número entero:'))
evaluac = "es par" if numero%2 == 0 else 'es impar'
print(f'El número {numero} {evaluac}.')