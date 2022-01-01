with open("dan09.txt") as f:
    input = f.read().strip().split("\n")


N = len(input)
M = len(input[0])

for red in range(1, len(input)):
    M.append(list(map(int, red.strip())))


def susjedni(y,x):   # gore, dole, lijevo, desno
    s = [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]
    return [(a,b) for a,b in s if 0 <= b < M and 0 <= a < N]

def getBasin(y,x): # Fja za P2
    ret = {(y,x)}
    for a,b in susjedni(y,x):
        if input[a][b] > input[y][x] and input[a][b] < 9:
            ret |= getBasin(a,b)
    return ret

def bigBasin(lowPoint):
    bsize= sorted([len(getBasin(y, x)) for y, x in lowPoint])
    return (bsize[-3] * bsize[-2] * bsize[-1])
    

# P1
lowPoints = []
sum = 0

for i in range(len(N)):
    for j in range(len(M)):
        if all(input[i][j] < input[a][b] for a,b in susjedni(j,i)):
            sum += input[i][j] + 1
            lowPoints.append([i, j])
print("P1: ", sum)

# P2
print("P2: ", bigBasin(lowPoints))
