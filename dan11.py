import numpy as np
from itertools import product

with open("dan11.txt") as f:
    input = f.read().strip()
podaci = np.array([[int(x) for x in list(i)]
                for i in input.split("\n")], dtype=int)

p1 = 0

n = len(podaci)

okt = podaci

for korak in range(100):
    flash = np.zeros((n, n), dtype=bool)

    for i, j in product(range(n), repeat=2):
        okt[i, j] += 1

    while True:
        checkNastavi = False

        promjena = np.zeros((n, n), dtype=int)

        for i, j in product(range(n), repeat=2):
            if not flash[i, j] and okt[i, j] > 9:

                p1 += 1
                flash[i, j] = True
                checkNastavi = True

                for di, dj in product(range(-1, 2), repeat=2):
                    if di == dj == 0:
                        continue

                    ni = i + di
                    nj = j + dj

                    if not (0 <= ni < n and 0 <= nj < n):
                        continue

                    promjena[ni, nj] += 1

        okt += promjena

        if not checkNastavi:
            break

    for i, j in product(range(n), repeat = 2):
        if flash[i, j]:
            okt[i, j] = 0

print("P1: ", p1)

p2 = 0
korak = 1

while True:
    flash = np.zeros((n, n), dtype=bool)

    for i, j in product(range(n), repeat = 2):
        okt[i, j] += 1

    while True:
        checkNastavi = False

        promjena = np.zeros((n, n), dtype=int)

        for i, j in product(range(n), repeat = 2):
            if not flash[i, j] and okt[i, j] > 9:

                p2 += 1
                flash[i, j] = True
                checkNastavi = True

                for di, dj in product(range(-1, 2), repeat=2):
                    if di == dj == 0:
                        continue

                    ni = i + di
                    nj = j + dj

                    if not (0 <= ni < n and 0 <= nj < n):
                        continue

                    promjena[ni, nj] += 1

        okt += promjena

        if not checkNastavi:
            break

    flashBrojac = 0
    for i, j in product(range(n), repeat=2):
        if flash[i, j]:
            flashBrojac += 1
            okt[i, j] = 0

    if flashBrojac == n * n:
        break

    korak += 1

print("P2: ", korak)
