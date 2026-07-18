import os, msvcrt

board = [' '] * 9


def print_board():
    os.system('cls')
    print('Tic Tac Toe - choose 1-9')
    for i in range(0, 9, 3):
        print(f' {board[i]} | {board[i+1]} | {board[i+2]} ')
        if i < 6:
            print('---+---+---')


def win(b):
    lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b1, c in lines:
        if b[a] == b[b1] == b[c] != ' ':
            return True
    return False


def empty_cells(b):
    return [i for i, x in enumerate(b) if x == ' ']


def best_move(b):
    for cell in empty_cells(b):
        b[cell] = 'O'
        if win(b):
            b[cell] = ' '
            return cell
        b[cell] = ' '
    for cell in empty_cells(b):
        b[cell] = 'X'
        if win(b):
            b[cell] = ' '
            return cell
        b[cell] = ' '
    corners = [0, 2, 6, 8]
    for c in corners:
        if b[c] == ' ':
            return c
    center = 4
    if b[center] == ' ':
        return center
    return empty_cells(b)[0]


while True:
    print_board()
    move = input('Your move (1-9) or q to quit: ')
    if move.lower() == 'q':
        print('Thanks for playing!')
        break
    if not move.isdigit() or int(move) < 1 or int(move) > 9:
        continue
    idx = int(move) - 1
    if board[idx] != ' ':
        continue
    board[idx] = 'X'
    if win(board):
        print_board()
        print('You win!')
        break
    if all(cell != ' ' for cell in board):
        print_board()
        print('Draw!')
        break
    comp = best_move(board)
    board[comp] = 'O'
    if win(board):
        print_board()
        print('Computer wins!')
        break
    if all(cell != ' ' for cell in board):
        print_board()
        print('Draw!')
        break
