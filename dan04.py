import numpy as np
import re

class Board:
    def __init__(s, br):
        s.board = [
            [[br[i][j], False] for j in range(5)]
            for i in range(5)
        ]

    def winDetect(s):
        for red in range(5):
            if all([s.board[red][i][1] for i in range(5)]):
                return True
        for kol in range(5):
            if all([s.board[i][kol][1] for i in range(5)]):
                return True
        return False

    def getPoeni(s, prethodni):
        suma = 0
        for red in range(5):
            for kol in range(5):
                if not s.board[red][kol][1]:
                    suma += s.board[red][kol][0]

        return suma * prethodni

    def markiraj(s, br):
        for red in s.board:
            for m in red:
                if m[0] == br:
                    m[1] = True


def parse_board(linije):
    return [[int(i) for i in re.split(" +", linija.strip())] for linija in linije]


with open("dan04.txt") as f:
    input = f.read().strip().split("\n")

brojevi = [int(i) for i in input[0].split(",")]

boards = []
i = 2
while i < len(input):
    x = parse_board(input[i:i+5])
    boards.append(Board(x))
    i += 6

odg = None
for x in brojevi:
    for b in boards:
        b.markiraj(x)
    for b in boards:
        if b.winDetect():
            ans = b.getPoeni(x)
            break

    if odg != None:
        break

print("P1: ", odg)

pobjednici = []
for x in brojevi:
    for i in range(len(boards)):
        boards[i].markiraj(x)

        if i not in pobjednici and boards[i].winDetect():
            pobjednici.append(i)

    if len(pobjednici) == len(boards):
        break

p2 = boards[pobjednici[-1]].getPoeni(x)
print("P2: ", p2)
