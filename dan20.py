from itertools import product

with open("dan20.txt") as f:
    input = f.read().strip().split("\n")

algo = input[0]
slikaInput = input[2:]

slika = set()

for red in range(len(slikaInput)):
    for kol in range(len(slikaInput[0])):
        if slikaInput[red][kol] == "#":
            slika.add((red, kol))


def get_granice(slika):
    minRed = 1 << 60
    maxRed = -(1 << 60)
    minKol = 1 << 60
    maxKol = -(1 << 60)
    for red, kol in slika:
        minRed, maxRed = min(minRed, red), max(maxRed, red)
        minKol, maxKol = min(minKol, kol), max(maxKol, kol)

    return minRed, maxRed, minKol, maxKol

def enhance(slika, granice):
    output = set()
    minRed, maxRed, minKol, maxKol = granice

    for red in range(minRed, maxRed + 1):
        for kol in range(minKol, maxKol + 1):
            nPix = ""

            for dred in range(-1, 2):
                for dkol in range(-1, 2):
                    nr = red + dred
                    nk = kol + dkol
                    nPix += "1" if (nr, nk) in slika else "0"

            if algo[int(nPix, base=2)] == "#":
                output.add((red, kol))

    return output


minX, maxX, minY, maxY = get_granice(slika)
minX -= 200
maxX += 200
minY -= 200
maxY += 200

for i in range(2):
    slika = enhance(slika, (minX, maxX, minY, maxY))
    minX += 3
    maxX -= 3
    minY += 3
    maxY -= 3

print("P1: ", len(slika))
