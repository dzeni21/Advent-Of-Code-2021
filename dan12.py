from collections import defaultdict, deque
from pprint import pprint

with open("dan12.txt") as f:
    input = f.read().strip()
podaci = [i.split("-") for i in input.split("\n")]


def jeMalo(cave):
    return cave.islower()

adj = defaultdict(list)

for i, j in podaci:
    adj[i].append(j)
    adj[j].append(i)


global odg
odg = 0
posjeta = set()

def dfs(cave):
    global odg

    if cave == "end":
        odg += 1
        return

    if jeMalo(cave) and cave in posjeta:
        return

    if jeMalo(cave):
        posjeta.add(cave)

    # Dodaj sve susjede u red 
    for nbr in adj[cave]:
        if nbr == "start":
            continue
        dfs(nbr)

    if jeMalo(cave):
        posjeta.remove(cave)

dfs("start")
print("P1: ", odg)


odg = 0
posjeta = defaultdict(int)

def dfs(cave):
    global odg

    if cave == "end":
        odg += 1
        return

    if jeMalo(cave):
        posjeta[cave] += 1

        checkPosjeta = 0  
        for i in posjeta:
            checkPosjeta += posjeta[i] > 1

            # Ni jedna mala pecina moze biti posjecena vise od 2 puta
            if posjeta[i] > 2:
                posjeta[cave] -= 1
                return

        if checkPosjeta > 1:
            posjeta[cave] -= 1
            return

    # Dodaj sve susjede u red
    for nbr in adj[cave]:
        if nbr == "start":
            continue
        dfs(nbr)

    if jeMalo(cave):
        posjeta[cave] -= 1


dfs("start")

print("P2: ", odg)
