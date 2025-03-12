import random


def create_tablero():
    return [[str(3 * i + j + 1)for j in range(3)] for i in range(3)]


def mostrar_tablero(tablero):
     for fila in tablero:
            print('----+---+---*')
            print('|', ' | '.join(fila), '|')


def marcar_tablero(tablero, numero, marca):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if (tablero[i][j] == numero):
                tablero[i][j] = marca
                return True
    return False


def verificar_ganador(tablero):
    # verificacion en filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2]:
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i]:
            return tablero[0][i]
        # verificacion en diagonal
    if tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return tablero[0][2]
    return None


'''
def verificar_tablero(tablero):
    for fila in tablero:
        for casilla in fila:
            if isinstance(casilla, int):
                return False
    return True
'''
def verificar_tablero(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla not in ['x', 'o']:  # Si hay algo que no sea 'X' o 'O'
                return False
    return True



def jugar_tic_tac_toe():
    print("Bienvenido a jugar tic tac toe")
    tablero = create_tablero()
    while True:
        mostrar_tablero(tablero)

        # Turno de usuario
        while True:
            numero = int(
    input("Ingrese un numero del 1 al 9 para marcar y 0 para salir: "))
            if numero == 0:
                print("Hasta pronto")
                return False
            if not 1 <= numero <= 9 or not marcar_tablero(
                tablero, str(numero), 'o'):
                print("Ingrese un numero entre 1 y 9 o ya esta marcado")
                continue
            marcar_tablero(tablero, str(numero), 'o')
            print("numero marcado")
            # mostrar_tablero(tablero)
            break
        # Verificar si el usuario ganó
        ganador = verificar_ganador(tablero)
        if ganador:
            if ganador == "o":
                print("¡Felicidades, ha ganado el ususrio!")
            elif ganador == "x":
                print("La máquina ha ganado. ¡Mejor suerte la próxima vez!")
            break
        if  verificar_tablero(tablero):
            print("El tablero se ha llenado, es un empate!")
            break



        #Turno de maquina
        while True:
            mov_maquina = random.randrange(1,10)
            if not 1 <= mov_maquina <= 9 or not marcar_tablero(tablero, str(mov_maquina), 'x'):
                continue
            marcar_tablero(tablero, str(mov_maquina), "x")
            break
        # Verificar si el usuario ganó
        ganador = verificar_ganador(tablero)
        if ganador:
            if ganador == "o":
                print("¡Felicidades, ha ganado el usuario!")
            elif ganador == "x":
                print("La máquina ha ganado. ¡Mejor suerte la próxima vez!")
            break
        if verificar_tablero(tablero):
            print("El tablero se ha llenado, es un empate!")
            break


    mostrar_tablero(tablero)
    
            
jugar_tic_tac_toe()
            
                 
     

