import random

mines = [[0, 0], [0, 0], [0, 0]]
placed = 0
while placed < 3:
    x = random.randint(0, 2)
    y = random.randint(0, 1)
    if mines[x][y] == 0:
        mines[x][y] = 1
        placed += 1

print(mines)
