from collections import defaultdict
from pprint import pprint

with open("dan06.txt") as f:
    input = f.read().strip().split(",")
    podaci = [int(i) for i in input]

dani = 80

for _ in range(days):
    n = len(podaci)
    for i in range(n):
        if podaci[i] == 0:
            podaci[i] = 6
            podaci.append(8)
        else:
            podaci[i] -= 1

p1 = len(podaci)
print(p1)


with open("dan06.txt") as f:
    input = f.read().strip().split(",")
    ponavljanja = defaultdict(int)
    for i in input:
        ponavljanja[int(i)] += 1

dani = 256

for _ in range(days):
    newPonavljanje = defaultdict(int)

    for key in ponavljanja:
        if key == 0:
            newPonavljanje[6] += ponavljanja[key]
            newPonavljanje[8] = ponavljanja[key]
        else:
            newPonavljanje[key - 1] += ponavljanja[key]

    ponavljanja = newPonavljanje

p2 = 0
for key in ponavljanja:
    p2 += ponavljanja[key]
print(p2)
