from math import *
with open("dan17.txt") as f:
    input = f.read().strip()

# Parcing
red = input().strip().split(" ")
posX = list(map(int, red[2].replace("x=", "").replace(",", "").split("..")))
posY = list(map(int, red[3].replace("y=", "").split("..")))


# vx - brzina po x
# vy - brzina po y

def provjera(vx, vy):
    x, y = 0, 0
    while True:
        x, y = x + vx, y + vy
        vx = max(0, vx - 1) 
        vy -= 1
        if x in range(posX[0], posX[1] + 1) and y in range(posY[0], posY[1] + 1):
            return True
        if x > posX[1] or y < posY[0]:
            return False

maxY = 0
valid = []
for vx in range(int(sqrt(2 * posX[0])) - 2, posX[1] + 1):
    for vy in range(posY[0], 250):
        if provjera(vx, vy):
            maxY = max(maxY, vy)
            valid.append([vx, vy])

print("P1: ", maxY * (maxY + 1) // 2)
print("P2: ", len(valid)) 