import random


def create_tablero():
    tablero = [[str(3 * i + j + 1)for j in range(3)] for i in range(3)]

def mostrar_tablero():
     tablero = create_tablero()
     for fila in tablero:
            print('----+---+---*')
            print('|', ' | '.join(fila), '|')
def marcar_tablero(tablero, numero, marca):
	for i in range(len(tablero)):
		for j in range(len(tablero)):
			if (tablero[i][j]) == numero):
				tablero[i][j] = marca
				return True
	return False
 
while True:      
    # Mostrar el tablero
       mi_movimiento = (int(input('Digite su movimiento:')))
    if(1 <= mi_movimiento <= 9):
        for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    if tablero[i][j] == numero:
                         
                         str(mi_movimiento):
                        tablero[i][j]= 'o'
                        print(tablero)
                        mov_maquina = random.randrange(1,9)
                        print(mov_maquina)
                        for a in range(len(tablero)):
                            for b in range(len(tablero[a])):
                                if (tablero[a][b] != 'o' or1 tablero[a][b] != 'x'):
                                    if tablero[a][b] == str(mov_maquina):
                                        tablero[a][b] = 'x'
                                        break
                                else:
                                    mov_maquina = random.randrange(1,9)
                        break
    elif mi_movimiento == 0:
        break
    else:
        print('Movimiento invalido')