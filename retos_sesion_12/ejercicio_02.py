# Tienes una página web y un usuario quiere acceder a ella, verifica si el usuario inició sesión para acceder a la página, caso contrario muestra un mensaje de error

db_usuarios = ['user_1', 'user_2','user_3','user_4','user_5']
user_log = input('Usuario: ') #Ej. user_1 al 5

if user_log in db_usuarios:
    print('Inicio sesión exitoso, bienvenido...')
else:
    print('Error, el usuario no se encuentra registrado.')
