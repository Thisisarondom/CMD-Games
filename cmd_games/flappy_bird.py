import os, time, random, msvcrt

WIDTH = 40
HEIGHT = 12
bird_x = 8
bird_y = 5
vel = 0
pipes = []
score = 0
frame = 0


def draw():
    os.system('cls')
    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for pipe in pipes:
        x, gap_y = pipe
        for y in range(HEIGHT):
            if y < gap_y or y > gap_y + 3:
                if 0 <= x < WIDTH:
                    grid[y][x] = '|'
    grid[round(bird_y)][bird_x] = '^'
    print('Flappy Bird - Space to jump, X to quit')
    print(f'Score: {score}')
    for row in grid:
        print(''.join(row))


while True:
    if msvcrt.kbhit():
        key = msvcrt.getwch()
        if key == ' ':
            vel = -1
        elif key in ('q', 'Q', 'x', 'X'):
            break

    frame += 1
    vel += 0.18
    bird_y += vel
    if frame % 10 == 0:
        gap_y = random.randint(2, HEIGHT - 5)
        pipes.append([WIDTH, gap_y])

    for pipe in pipes:
        pipe[0] -= 1
        if pipe[0] == bird_x:
            if bird_y < pipe[1] or bird_y > pipe[1] + 3:
                print('Game Over!')
                raise SystemExit
        if pipe[0] < 0:
            pipes.remove(pipe)
            score += 1

    if bird_y <= 0 or bird_y >= HEIGHT - 1:
        print('Game Over!')
        raise SystemExit

    draw()
    time.sleep(0.08)
