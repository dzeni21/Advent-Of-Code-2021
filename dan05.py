with open("dan05.txt") as f:
    input = f.read().strip().split("\n")

d1 = dict()
d2 = dict()

for red in range(1, len(input)):
    lCoord, dCoord = red.split(" -> ")
    (x1, y1), (x2, y2) = lCoord.split(","), dCoord.split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            d1[(x1, i)] = d1.get((x1, i), 0) + 1
            d2[(x1, i)] = d2.get((x1, i), 0) + 1
    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            d1[(i, y1)] = d1.get((i, y1), 0) + 1
            d2[(i, y1)] = d2.get((i, y1), 0) + 1

    # dijagonalno gornje lijevo - donje desno
    if x1 + y1 == x2 + y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            d2[(i, x1 + y1 - i)] = d2.get((i, x1 + y1 - i), 0) + 1
    # dijagonalno donje lijevo - gornje desno
    if x1 - y1 == x2 - y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            d2[(i, i + y1 - x1)] = d2.get((i, i + y1 - x1), 0) + 1

# Ispisi result
print("P1: ", len(list(filter(lambda arg: arg > 1, d1.values()))))
print("P2: ", len(list(filter(lambda arg: arg > 1, d2.values()))))