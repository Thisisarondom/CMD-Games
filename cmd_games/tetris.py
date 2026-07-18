import os, random, time, sys
import msvcrt

WIDTH = 10
HEIGHT = 18

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 1, 0]],
]

board = [[0] * WIDTH for _ in range(HEIGHT)]

def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]


def valid_move(shape, top, left):
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if not cell:
                continue
            rr = top + r
            cc = left + c
            if cc < 0 or cc >= WIDTH or rr >= HEIGHT:
                return False
            if rr >= 0 and board[rr][cc]:
                return False
    return True


def merge(shape, top, left):
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if cell:
                rr = top + r
                cc = left + c
                if rr >= 0:
                    board[rr][cc] = 1


def clear_lines():
    global board
    board = [row for row in board if any(v == 0 for v in row)]
    while len(board) < HEIGHT:
        board.insert(0, [0] * WIDTH)


shape = random.choice(SHAPES)
shape_top = -1
shape_left = WIDTH // 2 - len(shape[0]) // 2
last_tick = time.time()

while True:
    os.system('cls')
    if msvcrt.kbhit():
        key = msvcrt.getwch()
        if key in ('q', 'Q'):
            print('Thanks for playing!')
            sys.exit(0)
        if key in ('a', 'A', '\x1b[D'):
            if valid_move(shape, shape_top, shape_left - 1):
                shape_left -= 1
        elif key in ('d', 'D', '\x1b[C'):
            if valid_move(shape, shape_top, shape_left + 1):
                shape_left += 1
        elif key in ('s', 'S', '\x1b[B'):
            if valid_move(shape, shape_top + 1, shape_left):
                shape_top += 1
            else:
                merge(shape, shape_top, shape_left)
                clear_lines()
                shape = random.choice(SHAPES)
                shape_top = -1
                shape_left = WIDTH // 2 - len(shape[0]) // 2
                if not valid_move(shape, shape_top, shape_left):
                    print('Game Over!')
                    sys.exit(0)
        elif key in ('w', 'W', ' '):
            rotated = rotate(shape)
            if valid_move(rotated, shape_top, shape_left):
                shape = rotated
    if time.time() - last_tick > 0.45:
        last_tick = time.time()
        if valid_move(shape, shape_top + 1, shape_left):
            shape_top += 1
        else:
            merge(shape, shape_top, shape_left)
            clear_lines()
            shape = random.choice(SHAPES)
            shape_top = -1
            shape_left = WIDTH // 2 - len(shape[0]) // 2
            if not valid_move(shape, shape_top, shape_left):
                print('Game Over!')
                sys.exit(0)

    display = [row[:] for row in board]
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if cell and shape_top + r >= 0:
                display[shape_top + r][shape_left + c] = 1

    for row in display:
        print('|' + ''.join('#' if x else '.' for x in row) + '|')
    print('Controls: A/D move, S drop, W rotate')
    time.sleep(0.03)
