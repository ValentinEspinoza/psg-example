# Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales en peligro de extinción con información sobre sus hábitats amenazados, lo que permite priorizar la protección de áreas críticas para la supervivencia de estas especies
habitats = {"polo norte" : {"especies": {"oso polar", "morsa", "ballena"}}, "amazonas" : {"especies": {"tigre", "mono", "guacamayo"}}}

# Añade al diccionario de habitats 2 habitats más usando update()
habitat_add = {'Arrecifes de coral':{'especies':{'esponjas','almejas','cangrejos'}},'Selvas secas':{'especies':{'zorrillos','armadillos','iguanas'}}}
habitats.update(habitat_add)
print('1. Dict. Habitats actualizado ->', habitats)
print()

# Existe en el diccionario de habitats el habitat 'amazonas'?
buscar = 'amazonas'
print('2. Existe en habitats "amazonas"?:', buscar in habitats)
print()

# Añade al diccionario de amazonas la especie 'anaconda'
agrega = {'anaconda'}
habitats['amazonas']['especies'].update(agrega)
print('3. Añadiendo nuevo animal al dict. amazonas ->', habitats['amazonas']['especies'])
