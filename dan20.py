with open("dan20.txt") as f:
    input = f.read().strip().split("\n")

algo = input.strip()
skip = input

D = dict()
brojac = 0
for red in input.stdin:
    pom = list(red.strip())
    for i in range(len(pom)):
        D[(brojac, i)] = int(pom[i] == "#")
    brojac += 1

def susjedni(i, j):
    return [(i + x, j + y) for x in range(-1, 2) for y in range(-1, 2)]

def bin2Dec(lst):
    ret = 0
    for i in lst:
        ret *= 2
        ret += i
    return ret

minX, maxX, minY, maxY = [0, 100]*2
brojac = 0
def istakni():
    global D, minX, maxX, minY, maxY, brojac
    noviD = dict()
    for i in range(minX - 1, maxX + 1):
        for j in range(minY - 1, maxY + 1):
            noviD[(i, j)] = int(algo[bin2Dec(list(map(lambda x: D.get(x, brojac % 2), susjedni(i, j))))] == "#")
    D = noviD
    brojac += 1
    minX, maxX, minY, maxY = minX - 1, maxX + 1, minY - 1, maxY + 1

for _ in range(2):
    istakni()

p1 = sum(D.values())
print("P1: ", p1)

for _ in range(48):
    istakni()
    
p2 = sum(D.values())
print("P2: ", p2)
