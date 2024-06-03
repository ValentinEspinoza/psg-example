# Dar las felicitaciones a los estudiantes que aprobaron el curso de la siguiente tupla de estudiantes
estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]

for x in range(1, len(estudiantes)):
    if estudiantes[x-1][1] >= 51:
        print(f'Felicidades {estudiantes[x-1][0]}!! aprobaste el curso.')
