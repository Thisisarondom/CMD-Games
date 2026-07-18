import os, random, time, msvcrt

W, H = 20, 15
snake = [(10, 8), (9, 8), (8, 8)]
dirx, diry = 1, 0
food = (5, 5)


def draw():
    os.system('cls')
    grid = [[' ' for _ in range(W)] for _ in range(H)]
    for x, y in snake:
        grid[y][x] = '#'
    grid[food[1]][food[0]] = '*'
    print('Snake - Arrow keys/WASD, Press X to quit')
    for row in grid:
        print('|' + ''.join(row) + '|')


while True:
    draw()
    if msvcrt.kbhit():
        key = msvcrt.getwch()
        if key in ('q', 'Q', 'x', 'X'):
            break
        if key in ('w', 'W', '\x1b[A'):
            if not (dirx == 0 and diry == 1):
                dirx, diry = 0, -1
        elif key in ('s', 'S', '\x1b[B'):
            if not (dirx == 0 and diry == -1):
                dirx, diry = 0, 1
        elif key in ('a', 'A', '\x1b[D'):
            if not (dirx == 1 and diry == 0):
                dirx, diry = -1, 0
        elif key in ('d', 'D', '\x1b[C'):
            if not (dirx == -1 and diry == 0):
                dirx, diry = 1, 0

    headx = snake[0][0] + dirx
    heady = snake[0][1] + diry
    if headx < 0 or headx >= W or heady < 0 or heady >= H or (headx, heady) in snake:
        print('Game Over!')
        break

    snake.insert(0, (headx, heady))
    if (headx, heady) == food:
        while food in snake:
            food = (random.randint(0, W - 1), random.randint(0, H - 1))
    else:
        snake.pop()

    time.sleep(0.12)
