with open("dan04.txt") as f:
    input = f.read().strip().split("\n")

sekvenca = list(map(int, input().split(",")))

multiBingo = []
bingo = []

for red in range(1, len(input)):
    r = list(map(int,red.split()))
    if not r:
        multiBingo.append(bingo)
        bingo = []
    else:
        bingo.append(r)
multiBingo.append(bingo)

def transponiraj(x):
    return [[x[i][j] for i in range(len(x))] for j in range(len(x[0]))]

def checkBingo(x):
    for red in x:
        if sum(red) == 0:
            return True
    for red in transponiraj(x):
        if sum(red) == 0:
            return True

    # Pretpostavljamo da je x kvadratna matrica
    return sum(x[i][i] for i in range(len(x))) == 0 or \
        sum(x[i][-i-1] for i in range(len(x))) == 0

p1Solved = False
for k in sekvenca:
    for b in multiBingo:
        for j in range(len(b)):
            b[j] = list(map(lambda arg: 0 if arg == k else arg, b[j]))
        if checkBingo(b):
            if not p1Solved:
                print("P1: ", k * sum(map(sum, b)))
                p1Solved = True
            if len(multiBingo) == 1:
                print("P2: ", k * sum(map(sum, b)))

    multiBingo = list(filter(lambda arg: not checkBingo(arg), multiBingo))