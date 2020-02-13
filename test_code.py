""""
Дана доска размером M × N клеток. Клетка может находиться в одном из двух состояний: 1 — живая, 0 — мёртвая.
Каждая клетка взаимодействует с восемью соседями. Правила таковы:

Живая клетка, у которой меньше двух живых соседей, погибает.

Живая клетка, у которой два или три живых соседа, выживает.

Живая клетка, у которой больше трёх живых соседей, погибает.

Мёртвая клетка, у которой три живых соседа, возрождается.

Напишите программу, которая будет:
— случайным образом генерить стартовое состояние;
— уметь получать его из файла (способ выбирается через параметры запуска в консоли);
— каждую секунду выводить в консоль новое состояние доски.
"""
import random
import time
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-m')
parser.add_argument('-n')
parser.add_argument('-file')
args = parser.parse_args()
new_dict = {key: value for key, value in vars(args).items()}


def new_cell(board, i, j, cell):
    neighbors = []
    neighbors_shift = range(-1, 2)
    for k in neighbors_shift:
        for l in neighbors_shift:
            if not(k == 0 and l == 0):
                if i + k >= 0 and j + l >= 0:
                    try:
                        neighbors.append(board[i + k][j + l])
                    except IndexError:
                        pass

    alive = neighbors.count(1)
    if cell:

        if alive < 2 or alive > 3:
            return 0
        else:
            return 1

    else:
        if alive == 3:
            return 1
        else:
            return 0


# Random start condition generation
if new_dict['m']:
    M = int(new_dict['m'])
    N = int(new_dict['n'])
    board = [[random.randint(0, 1) for _ in range(M)] for _ in range(N)]
# or board from file
elif new_dict['file']:
    board = []
    with open(new_dict['file']) as table:
        for row in table:
            row = row.split(' ')
            row = list(map(int, row))
            board.append(row)
    N = len(board)
    M = len(board[0])
for row in board:
    print(row)
print()

new_time = time.time()

while True:

    new_board = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            new_board[i][j] = new_cell(board, i, j, board[i][j])
    while (time.time() - new_time) < 1:
        pass
    else:
        new_time = time.time()
        print(time.ctime(new_time)[11:19])
        board = new_board
    for row in new_board:
        print(row)
    print()
