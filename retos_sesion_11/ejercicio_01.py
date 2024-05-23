# Registro de un zoológico, utiliza un diccionario para almacenar información de un animal del zoológico, registra información como especie, habitat, dieta, estado de salud, edad, en una lista los responsables de su cuidado

info = [('especie', 'Felis silvestris'), ('habitat', 'doméstico'), ('dieta','carnívoros'), ('estado de salud', 'Saludable'), ('edad', 2) ]
responsables = ['resp_A', 'resp_B', 'resp_C', 'resp_D']

registro_zoo = dict(info)
registro_zoo['responsables'] = responsables

print('Información almacenada:\n', registro_zoo)
