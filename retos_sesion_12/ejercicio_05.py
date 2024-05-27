# Un usuario ingresa su nombre y gustos musicales por teclado separados por coma, verifica si el usuario ingresó un nombre válido usando truthiness, convertir los gustos musicales en una lista y verifica si tiene el gusto rock en su lista de gustos musicales
# Nombre: Jhon Doe
# Gustos musicales: rock,pop,jazz

print('Ingrese su nombre y gustos musicales separados por coma,\n Ejemplo:\nNombre: Jhon Doe\nGustos musicales: rock,pop,jazz\n')
nombre = input('Nombre: ')
gustos_musicales = input('Gustos musicales: ').split(',')

nombre_valido = all(indice.isalpha() or indice.isspace() for indice in nombre) # valida y devuelve True si en todo el nombre existe letras y/o espacio
    
if nombre_valido:
    if 'rock' in gustos_musicales:
        print('El nombre es válido y tiene el gusto rock en su lista de gustos musicales.')
    else:
        print('El nombre es válido pero NO tiene el gusto rock en su lista de gustos musicales.')
else: 
    print('El nombre ingresado no es valido. Intente nuevamente, el nombre no puede contener números o carácteres especiales.')

