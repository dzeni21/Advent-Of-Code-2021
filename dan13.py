import string

with open("dan13.txt") as f:
    input = f.read().strip()

naredba = []
d = []
tacke = True

for red in input.stdin:
    red = red.strip()
    if not red:
        tacke = False
        continue
    if tacke:
        red = red.split(",")
        d.append([int(red[0]), int(red[1])])
    else:
        red = red.split("=")
        naredba.append([red[0][-1], int(red[1])])

x = max(map(lambda arg: arg[1], d)) + 1
y = max(map(lambda arg: arg[0], d)) + 1

for coord, n in naredba:
    noviD = dict()
    for px, py in d:
        if coord == 'x':
            noviD[(n - abs(px - n), py)] = True
        else:
            noviD[(px, n - abs(py - n))] = True
    d = noviD
    if coord == 'x':
        y = max(map(lambda arg: arg[0], d.keys())) + 1
    else:
        x = max(map(lambda arg: arg[1], d.keys())) + 1
    if (coord, n) == tuple(naredba[0]):
        print("P1: ", len(d))

final = []
for _ in range(x):
    final.append(["."] * y)
for dx, dy in d:
    final[dy][dx] = "#"

print("P2: ")
for row in final:
    print(str().join(row))