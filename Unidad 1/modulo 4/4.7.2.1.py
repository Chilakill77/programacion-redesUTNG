#Kevin
from random import randrange

def DisplayBoard(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def EnterMove(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento (1 al 9): "))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] != 'X' and board[row][col] != 'O':
                    board[row][col] = 'O'
                    break
                else:
                    print("Esa casilla ya está ocupada. Inténtalo de nuevo.")
            else:
                print("Número fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")

def MakeListOfFreeFields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'X' and board[row][col] != 'O':
                free_fields.append((row, col))
    return free_fields

def VictoryFor(board, sign):
    # Verificar filas y columnas
    for i in range(3):
        if all([board[i][j] == sign for j in range(3)]) or \
           all([board[j][i] == sign for j in range(3)]):
            return True
    # Verificar diagonales
    if all([board[i][i] == sign for i in range(3)]) or \
       all([board[i][2 - i] == sign for i in range(3)]):
        return True
    return False

def DrawMove(board):
    free_fields = MakeListOfFreeFields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def main():
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    print("¡Bienvenido al juego de Tic-Tac-Toe!")
    print("La máquina jugará con 'X'. Tú jugarás con 'O'.")
    DisplayBoard(board)

    # Primer movimiento de la máquina
    board[1][1] = 'X'
    DisplayBoard(board)

    while True:
        EnterMove(board)
        DisplayBoard(board)
        if VictoryFor(board, 'O'):
            print("¡Has ganado!")
            break

        DrawMove(board)
        DisplayBoard(board)
        if VictoryFor(board, 'X'):
            print("¡La máquina ha ganado!")
            break

        if len(MakeListOfFreeFields(board)) == 0:
            print("¡Empate!")
            break

if __name__ == "__main__":
    main()
