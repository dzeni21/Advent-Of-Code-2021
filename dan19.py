from math import dist

with open("dan19.txt") as f:
    input = f.read().strip()

redovi = []
pom = []
scanners = []

for red in input.stdin:
    redovi.append(red.strip())

for x in redovi:
    tup = x.split(",")
    if len(tup) == 3:
        pom.append(tuple(map(int, tup)))
    elif pom:
        scanners.append(pom)
        pom = []
scanners.append(pom)

def genSve(scanner):
    def pomFja(scanner):
        pom1 = [(x, y, z) for x, y, z in scanner]
        pom2 = [(x, -z, y) for x, y, z in scanner]
        pom3 = [(x, -y, -z) for x, y, z in scanner]
        pom4 = [(x, z, -y) for x, y, z in scanner]
        return [pom1, pom2, pom3, pom4]
    ret = pomFja(scanner)
    ret.extend(pomFja([(-x, z, y) for x, y, z in scanner]))
    ret.extend(pomFja([(y, z, x) for x, y, z in scanner]))
    ret.extend(pomFja([(-y, x, z) for x, y, z in scanner]))
    ret.extend(pomFja([(z, y, -x) for x, y, z in scanner]))

    ret.extend(pomFja([(-z, x, -y) for x, y, z in scanner]))
    return ret

sveOrijentacije = list(map(genSve, scanners))

def dajMatch(scanner1, scanner2):
    gen1 = sveOrijentacije[scanner1]
    gen2 = sveOrijentacije[scanner2]
    ret = dict()
    for orijentacija1 in range(24):
        for orijentacija2 in range(24):
            d = {}
            for i in gen1[orijentacija1]:
                for j in gen2[orijentacija2]:
                    triple = tuple(map(lambda x: i[x] - j[x], range(3))) + (scanner1*24 + orijentacija1, scanner2*24 + orijentacija2)
                    d[triple] = d.get(triple, 0) + 1
            provjera = list(filter(lambda arg: arg[1] >= 12, d.items()))
            if provjera:
                ret[provjera[0][0][-2]] = (provjera[0][0][-1], provjera[0][0][:3])
    return ret

mem = dict()
preklapanje = dict()
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        if (i, j) not in mem:
            provjera = dajMatch(i, j)
            mem[(i, j)] = provjera
        else:
            provjera = mem[(i, j)]
        if provjera:
            preklapanje[i] = preklapanje.get(i, []) + [j]
            preklapanje[j] = preklapanje.get(j, []) + [i]

pos = {0: (0, (0, 0, 0))}
visible = [False] * len(scanners)
r = [0]
while r:
    i = r.pop()
    visible[i] = True
    for j in preklapanje[i]:
        if not visible[j]:
            if (i, j) not in mem:
                provjera = dajMatch(i, j)
                mem[(i, j)] = provjera
            else:
                provjera = mem[(i, j)]
            if pos[i][0] in provjera:
                r.append(j)
                pos[j] = (provjera[pos[i][0]][0], tuple(map(sum, zip(provjera[pos[i][0]][1], pos[i][1]))))

beacons = set(scanners[0])
for i in range(1, len(scanners)):
    for j in sveOrijentacije[i][pos[i][0] % 24]:
        beacons.add(tuple(map(sum, zip(j, pos[i][1]))))

p1 = len(beacons)
print("P1: ", p1)

manhattanDist = []
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        ctr1 = pos[i][1]
        ctr2 = pos[j][1]
        manhattanDist.append(sum(abs(ctr1[k] - ctr2[k]) for k in range(3)))

p2 = max(manhattanDist)
print("P2: ", p2)
