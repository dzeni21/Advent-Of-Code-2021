import numpy as np
from collections import defaultdict

with open("dan22.txt") as f:
    input = f.read().strip().split("\n")

def checkUnutarGranica(xRange, yRange, zRange):
    for t in xRange, yRange, zRange:
        if not (t[1] <= 100 and 0 <= t[0]):
            return False
    return True

koraci = []

for red in input:
    dio = red.split(" ")
    stanje = dio[0] == "on"
    granice = []
    for axis in dio[1].split(","):
        axis = axis.split("..")
        granice.append((int(axis[0][2:]) + 50, int(axis[1]) + 50))

    koraci.append((stanje, granice))

grid = np.zeros((101, 101, 101), dtype = bool)

for stanje, granice in koraci:
    xRange, yRange, zRange = granice
    if not checkUnutarGranica(xRange, yRange, zRange):
        continue
    for i in range(xRange[0], xRange[1] + 1):
        for j in range(yRange[0], yRange[1] + 1):
            for k in range(zRange[0], zRange[1] + 1):
                grid[i, j, k] = stanje
p1 = 0
for x in grid.flatten():
    p1 += x
print("P1: ", p1)

# P2

koraci = []

def zapremina(granice):
    # Racuna zapreminu cuboid-a
    v = 1
    for g in granice:
        assert g[1] >= g[0]
        v *= abs(g[1] - g[0]) + 1
    return v


def intersection(granica1, granica2):
    # presjek dva kuboida kako bi dobili novi kuboid
    rez = []
    for g1, g2 in zip(granica1, granica2):
        if g1[1] < g2[0] or g2[1] < g1[0]:
            return None

        granice = (max(g1[0], g2[0]), min(g1[1], g2[1]))
        rez.append(granice)

    return tuple(rez)

for red in input:
    dio = red.split(" ")
    stanje = dio[0] == "on"
    granice = []
    for axis in dio[1].split(","):
        axis = axis.split("..")
        granice.append((int(axis[0][2:]), int(axis[1])))

    koraci.append((stanje, tuple(granice)))


brojac = defaultdict(int)
for i in range(len(koraci)):
    stanje, granice = koraci[i]

    noviBrojac = defaultdict(int)
    keys = set(brojac.keys())
    for nCube in keys:
        nStanje = brojac[nCube] > 0
        n = intersection(granice, nCube)
        if n == None:
            continue

        noviBrojac[n] -= brojac[nCube]  # Resetuj na 0

    if stanje:
        noviBrojac[granice] += 1

    for c in noviBrojac:
        brojac[c] += noviBrojac[c]


p2 = 0
for cube in brojac:
    p2 += zapremina(cube) * brojac[cube]
print("P2: ", p2)