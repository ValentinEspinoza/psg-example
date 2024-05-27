# El usuario Jhon Doe esta en una red social sus amigos son:
amigos_Jhon = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}

# La usuaria Jess Doe tiene los siguientes amigos
amigos_Jess = {'Alice', 'Bob',  'Frank', 'Grace'}

# ¿Tienen Jhon y Jess amigos en común?, ¿Cuáles son?

amigos_comun = amigos_Jhon.intersection(amigos_Jess)
if amigos_comun != set():
    print(f'Jhon Doe y Jess Doe Si tienen amigos en común y son {amigos_comun}')
else:
    print('Jhon Doe y Jess Doe No tienen amigos en común.')