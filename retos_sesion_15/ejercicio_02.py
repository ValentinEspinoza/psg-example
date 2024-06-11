# Crear un programa para crear una canasta de frutas, solicitar frutas por teclado y almacenar en una lista, si se ingresa "salir" termina la ejecución. Solo se permiten las siguientes frutas caso contrario lanzar una excepción personalizada
# 🍅🍇🍈🍉🍊🍌🍍🍑

frutas_validas = {1:'🍅', 2:'🍇', 3:'🍈', 4:'🍉', 5:'🍊', 6:'🍌', 7:'🍍', 8:'🍑'}

print('🧺 CANASTA DE FRUTAS 🧺 \nSolamente se permiten las siguientes frutas:')
print('1 = 🍅   2 = 🍇   3 = 🍈   4 = 🍉\n5 = 🍊   6 = 🍌   7 = 🍍   8 = 🍑')
print('Digite un número para ingresar la fruta deseada.')
print('Ingrese "salir" para finalizar.\n')

canasta = []
class fruta_no_permitida(Exception):
    pass

while 1:
    try:
        fruta = input('Ingresa una fruta: ')
        #validación para salir
        if fruta.lower() == 'salir':
            break
        
        fruta = int(fruta)
        #Comprueba si el numero pertenece a una fruta valida
        if fruta not in frutas_validas:
            raise fruta_no_permitida()
        canasta.append(frutas_validas[fruta])
        print(f'Fruta {frutas_validas[fruta]} añadido a la canasta ✅')
        
    
    except KeyboardInterrupt:
        print('🚫 Para salir escriba "salir"')
    
    except Exception:
        print('⚠️ Por favor ingresa un fruta permitida...\n')

#imprime el contenido
print(f'La canasta de frutas contiene: \n🧺 {canasta}')

