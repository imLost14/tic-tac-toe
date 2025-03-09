# Representación del tablero de Tic Tac Toe
tablero = [[str(3 * i + j + 1)for j in range(3)] for i in range(3)]

while True:      
    # Mostrar el tablero
    for fila in tablero:
            print('----+---+---*')
            print('|', ' | '.join(fila), '|')

    mi_movimiento = (int(input('Digite su movimiento:')))
    if(1 <= mi_movimiento <= 9):
        for i in range(len(tablero)):
                for j in range(len(tablero[i])):
                    if tablero[i][j] == str(mi_movimiento):
                        tablero[i][j]= 'o'
                        break
    elif mi_movimiento == 0:
        break
    else:
        print('Movimiento invalido')