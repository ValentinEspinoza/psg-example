# Crear una función anónima para obtener el área de un círculo con radio 5

radio = 5
PI = 3.1416
area_circulo = lambda rad: PI * rad**2

print(f'Área del circulo de radio {radio} unid. es {round(area_circulo(radio), 2)} unid^2.')