import numpy as np
from os import link

with open("dan04.txt") as f:
    input = f.read().strip().split("\n")


def parseLiniju(linija):
    poc, _, kraj = linija.split(" ")
    poc = [int(i) for i in poc.split(",")]
    kraj = [int(i) for i in kraj.split(",")]
    return poc, kraj

linije = [parseLiniju(x) for x in input]

# Odbaci tacke koje nisu vertikalne ili horizontalne
linije = [l for l in linije
         if l[0][0] == l[1][0] or l[0][1] == l[1][1]]

# Pronadji granice mreze
maxX = 0
maxY = 0
for i in linije:
    maxX = max(maxX, i[0][0], i[1][0])
    maxY = max(maxY, i[0][1], i[1][1])

c = np.zeros((maxX + 1, maxY + 1))
for i in linije:
    poc, kraj = i
    if poc[0] == kraj[0]:
        down = min(poc[1], kraj[1])
        up = max(poc[1], kraj[1])
        for y in range(down, up + 1):
            c[poc[0]][y] += 1

    else:
        assert poc[1] == kraj[1]
        lijevo = min(poc[0], kraj[0])
        desno = max(poc[0], kraj[0])
        for x in range(lijevo, desno + 1):
            c[x][poc[1]] += 1

# Saznaj koliko je tacaka pokriveno vise puta
p1 = 0
for count in c.flatten():
    p1 += count >= 2

print("P1: ", p1)


def znak(s):
    if s > 0:
        return 1
    if s < 0:
        return -1
    return 0


def parseLinijuDir(linija):
    poc, _, kraj = linija.split(" ")
    poc = [int(i) for i in poc.split(",")]
    kraj = [int(i) for i in kraj.split(",")]

    # Vektor smjera
    smjer= [znak(kraj[0] - poc[0]), znak(kraj[1] - poc[1])]

    return poc, kraj, smjer


linije = [parseLinijuDir(line) for line in input]

# Pronadji granice mreze
maxX = 0
maxY = 0
for i in linije:
    maxX = max(maxX, i[0][0], i[1][0])
    maxY = max(maxY, i[0][1], i[1][1])

c = np.zeros((maxX + 1, maxY + 1))
for i in linije:
    poc, kraj, smjer= i
    p = poc
    while p != kraj:
        c[p[0], p[1]] += 1
        p[0] += smjer[0]
        p[1] += smjer[1]
    c[kraj[0]][kraj[1]] += 1

p2 = 0
for count in c.flatten():
    p2 += count >= 2

c.transpose()
print("P2", p2)
