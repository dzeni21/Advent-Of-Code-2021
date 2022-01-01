import sys, heapq

with open("dan15.txt") as f:
    input = f.read().strip()

def racunajMinRizik(cavern):
    n, m = len(cavern), len(cavern[0])
    rizik = [[-1]*m for _ in range(n)]
    rizik[0][0] = 0
    q = [(0, 0, 0)]
    while rizik[-1][-1] == -1:
        # i - red, j - kolona
        rizik, i, j = heapq.heappop(q)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i1, j1 = i + di, j + dj
            if 0 <= i1 < n and 0 <= j1 < m and rizik[i1][j1] == -1:
                rizik[i1][j1] = rizik + cavern[i1][j1]
                heapq.heappush(q, (rizik[i1][j1], i1, j1))
    return rizik[-1][-1]

def get5xCavern(cavern):
    n, m = len(cavern), len(cavern[0])
    newCavern = [[0] * (5 * m) for _ in range(5 * n)]
    for red in range(5):
        for kolona in range(5):
            for i in range(n):
                for j in range(m):
                    i1, j1 = n * red + i, m * kolona + j
                    newCavern[i1][j1] = cavern[i][j] + red + kolona
                    if newCavern[i1][j1] > 9:
                        newCavern[i1][j1] -= 9
    return newCavern

assert len(input.argv) == 2
cavern = [list(map(int, list(line))) for line in open(input.argv[1]).read().splitlines()]

p1 = racunajMinRizik(cavern)
p2 = racunajMinRizik(get5xCavern(cavern))

print("P1: ", p1)
print("P2: ", p2)