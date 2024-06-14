# Simular un tres en raya con funciones donde reciba las jugadas y devuelva el ganador hasta que alguien ingrese salir

'''
Tablero de posiciones para seleccionar la posición a marcar para cada jugador
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
'''


def mostrar_tablero (tablero):
    """
    Imprime los separadores de las posiciones en el tablero
    """
    for i in range (0, 7, 3):
        print(f'{tablero[i]} | {tablero[i+1]} | {tablero[i+2]}')


def posiciones():   
    tablero = [' '] * 9
    sigue = True
    turno = True 
    while sigue:
        siguiente_jugada = False
        
        while not siguiente_jugada:
            try:
                print()    
                print(f'Turno de X: ' if turno == True else f'Turno de O:')
            
                #Solicita la posición para marcar en el tablero
                posicion = input('Ingrese la posición (1-9): ')
                            
                #Finaliza el juego
                if posicion == 'salir':
                    print("Finalizando...")
                    break
            
                posicion = int(posicion)
                if tablero[posicion-1] == ' ':
                    siguiente_jugada = True
                else:
                    print('No es posible marcar ahí, intenta otra posición')
            except KeyboardInterrupt:
                print ("Para finalizar el juego ingresa 'salir'.")
            except:
                print('La posición indicada no existe.')
    
        #Registra la posicion introducida por cada jugador
        tablero[posicion-1] = 'X' if turno else 'O'
    
        #Imprime el registro de las posiciones marcadas
        mostrar_tablero(tablero)
    
        #Comprueba todas la posibles combinaciones para ganar
        if (tablero[0] == tablero[1] == tablero[2] and tablero[0]!=' ' or
        tablero[3] == tablero[4] == tablero[5] and tablero[3]!=' ' or 
        tablero[6] == tablero[7] == tablero[8] and tablero[6]!=' ' or
        tablero[0] == tablero[3] == tablero[6] and tablero[0]!=' ' or
        tablero[1] == tablero[4] == tablero[7] and tablero[1]!=' ' or
        tablero[2] == tablero[5] == tablero[8] and tablero[2]!=' ' or
        tablero[0] == tablero[4] == tablero[8] and tablero[0]!=' ' or
        tablero[2] == tablero[4] == tablero[6] and tablero[2]!=' '):
            print('El ganador es el Jugador 1 🎉🎊\n' if turno else 'El ganador es el Jugador 2 🎉🎊\n')
            sigue = False
            break #Finaliza el juego
    
        #Comprueba si existen mas espacios en blanco en el tablero
        if ' ' not in tablero:
            print('Es un Empate 🤜🤛')
            break
    
        #Alterna a los jugadores para registrar las posiciones
        turno = not turno
    
def juego():
    #Descripción del juego
    print('>>> 3 EN RAYA <<<')
    print('Tablero de Posiciones: \n1 | 2 | 3 \n4 | 5 | 6 \n7 | 8 | 9\n')
    print('Jugador 1: X \nJugador 2: O\n')
    print('Ingrese "salir" para finalizar.\n')
    
    posiciones()

    while 1:
        try:
           opcion = input("Quieren jugar de nuevo? (s/n): ")
           if opcion.lower() == 's':
               posiciones()
           elif opcion.lower() == 'n':
               print("Finalizando...")
               break
           else:
               raise ValueError()
        
        except KeyboardInterrupt:
            print ("Para salir ingresa 'n'.")
        except:
            print ("Por favor, ingresa una opción 's' o 'n'.")
        
            
#Inicia el juego
juego()