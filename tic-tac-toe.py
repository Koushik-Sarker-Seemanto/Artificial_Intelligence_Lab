import os
import time

gamer = 'x'
ai = 'o'

def move_left_available(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return True
    return False

def position_check(board, row, col):
    if board[row][col] == '_':
        return True
    return False

def evaluate_board(board):
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == ai:
                return +10
            elif board[row][0] == gamer:
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == ai:
                return +10
            elif board[0][col] == gamer:
                return -10

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == ai:
            return +10
        elif board[0][0] == gamer:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == ai:
            return +10
        elif board[0][2] == gamer:
            return -10


def mini_max_algo(board, depth, is_max):
    result = evaluate_board(board)

    if result == 10:
        return result
    if result == -10:
        return result

    if not move_left_available(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = ai
                    best = max(best, mini_max_algo(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = gamer
                    best = min(best, mini_max_algo(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best


def get_best_move(board):
    best_value = -1000
    best_move = Move(-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = ai
                move_val = mini_max_algo(board, 0, False)
                board[i][j] = '_'
                if move_val > best_value:
                    best_move.row = i
                    best_move.col = j
                    best_value = move_val
    return best_move


def display_board(board):
    print(" %c | %c | %c " % (board[0][0], board[0][1], board[0][2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[1][0], board[1][1], board[1][2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[2][0], board[2][1], board[2][2]))
    print("   |   |   ")

class Move:
    def __init__(self, row, col):
        self.row = row
        self.col = col


if __name__ == "__main__":
    tic_toc_board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    while True:
        display_board(tic_toc_board)
        val = evaluate_board(tic_toc_board)
        if val == 10:
            print("=========== Bot win ===========")
            break
        elif val == -10:
            print("=========== You win ===========")
            break
        elif (val is not 10 or -10) and move_left_available(tic_toc_board) is False:
            print("=========== Draw ===========")
            break
        choice = int(input("Enter your move [1-9]"))
        if choice == 1:
            if position_check(tic_toc_board, 0, 0):
                tic_toc_board[0][0] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        if choice == 2:
            if position_check(tic_toc_board, 0, 1):
                tic_toc_board[0][1] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        if choice == 3:
            if position_check(tic_toc_board, 0, 2):
                tic_toc_board[0][2] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        if choice == 4:
            if position_check(tic_toc_board, 1, 0):
                tic_toc_board[1][0] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        if choice == 5:
            if position_check(tic_toc_board, 1, 1):
                tic_toc_board[1][1] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        if choice == 6:
            if position_check(tic_toc_board, 1, 2):
                tic_toc_board[1][2] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        if choice == 7:
            if position_check(tic_toc_board, 2, 0):
                tic_toc_board[2][0] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        if choice == 8:
            if position_check(tic_toc_board, 2, 1):
                tic_toc_board[2][1] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        if choice == 9:
            if position_check(tic_toc_board, 2, 2):
                print("-------")
                tic_toc_board[2][2] = gamer
            else:
                os.system('clear')
                print("Choice is not available!")
                continue
        os.system('clear')
        display_board(tic_toc_board)
        if move_left_available(tic_toc_board):
            os.system('clear')
            print("waiting for the ai's move")
            time.sleep(3)
            move = get_best_move(board=tic_toc_board)
            tic_toc_board[move.row][move.col] = ai
        os.system('clear')
