import numpy as np

with open("dan09.txt") as f:
    input = f.read().strip().split("\n")
    podaci = [[int(i) for i in list(line)] for line in input]

redovi = len(podaci)
kolone = len(podaci[0])

p1 = 0
# Find low points
for red in range(redovi):
    for kol in range(kolone):
        low = True
        for i in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            rr = red + i[0]
            kk = kol + i[1]

            if not ((0 <= rr and rr < redovi) and (0 <= kk and kk < kolone)):
                continue
            if podaci[rr][kk] <= podaci[red][kol]:
                low = False
                break

        if low:
            p1 += podaci[red][kol] + 1

print("P1: ", p1)

# P2

low = []
trenutniID = 1
ids = np.zeros((redovi, kolone), dtype=int)

# Find low points
for red in range(redovi):
    for kol in range(kolone):
        jeLow = True
        for i in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            rr = red + i[0]
            kk = kol + i[1]

            if not ((0 <= rr and rr < redovi) and (0 <= kk and kk < kolone)):
                continue

            if podaci[rr][kk] <= podaci[red][kol]:
                jeLow = False
                break

        if jeLow:
            low.append((red, kol))

for red, kol in low:
    stek = [(red, kol)]
    posjeta = set()
    while len(stek) > 0:
        red, kol = stek.pop()

        if (red, kol) in posjeta:
            continue
        posjeta.add((red, kol))

        ids[red, kol] = trenutniID

        for i in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            rr = red + i[0]
            kk = kol + i[1]

            if not ((0 <= rr and rr < redovi) and (0 <= kk and kk < kolone)):
                continue

            if podaci[rr][kk] == 9:
                continue

            stek.append((rr, kk))

    trenutniID += 1

# Pronadji velicine najvecih basins
vel = [0] * trenutniID

for x in ids.flatten():
    vel[x] += 1
vel = vel[1:]

vel.sort()
print("P2: ",vel[-1] * vel[-2] * vel[-3])
