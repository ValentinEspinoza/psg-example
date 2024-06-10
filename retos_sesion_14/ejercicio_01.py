# Un estudiante desea saber cuál es su promedio de calificaciones en la materia de matemáticas, cree una función que reciba las calificaciones como lista y devuelva el promedio las calificaciones son 20,40,60,51,13

notas = [20,40,60,51,13]
def calcular_promedio(lista):
    print(f'El promedio de calificaciones es {round(sum(lista)/len(lista), 2)}')

calcular_promedio(notas)
