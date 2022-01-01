import copy

with open("dan25.txt") as f:
    input = f.read().strip()
    grid = [list(red) for red in input.split("\n")]

redovi = len(grid)
kolone = len(grid[0])


def napraviKorak(grid, ch):
    # ch moze biti "v" ili ">"
    noviGrid = copy.deepcopy(grid)
    checkPomak = False

    for i in range(redovi):
        for j in range(kolone):
            if ch != grid[i][j]:
                continue

            if grid[i][j] == "v":
                udaljenost = (i + 1) % redovi, j
            else:
                udaljenost = i, (j + 1) % kolone

            if grid[udaljenost[0]][udaljenost[1]] == ".":
                checkPomak = True
                noviGrid[udaljenost[0]][udaljenost[1]] = grid[i][j]
                noviGrid[i][j] = "."

    return noviGrid, checkPomak

korak = 0
while True:
    grid, checkPomak_e = napraviKorak(grid, ">")
    grid, checkPomak_s = napraviKorak(grid, "v")
    korak += 1
    if not (checkPomak_e or checkPomak_s):
        break

print("P1: ", korak)