input = dict()
with open("dan11.txt") as f:
    for y, red in enumerate(f.readlines()):
        for x, br in enumerate(red.strip()):
            input[(x, y)] = int(br)

ukupnoFlashes = 0
granica = ((1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
korak = 0

while 1:
    korak += 1
    for i in input:
        input[i] += 1

    stack = [i for i in input if input[i] == 10]
    while stack:
        x, y = stack.pop()
        for dx, dy in granica:
            x1 = x + dx
            y1 = y + dy
            if (x1, y1) in input and input[x1, y1] < 10:
                input[x1, y1] += 1
                if input[x1, y1] == 10:
                    stack.append((x1, y1))

    flashes = 0
    for i in input:
        if input[i] == 10:
            input[i] = 0
            flashes += 1

    ukupnoFlashes += flashes
    if korak == 100:
        print("P1: ", ukupnoFlashes)

    if flashes == 100:
        print("P2: ", korak)
        break