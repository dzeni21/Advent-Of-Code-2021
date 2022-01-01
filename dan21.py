with open("dan21.txt") as f:
    input = f.read().strip().split("\n")

player1, player2 = int(input.strip()[-1]), int(input.strip()[-1])

def wrap(br, ost):
    if br % ost == 0:
        return ost
    return br % ost

def igra(dice, player1, player2):
    bodovi1, bodovi2, brojac = 0, 0, 0
    while bodovi1 < 1000 and bodovi2 < 1000:
        player1 = wrap(player1 + 3 * dice, 10)
        dice = wrap(dice + 3, 100)
        brojac, bodovi1 = brojac + 3, bodovi1 + player1
        if bodovi1 >= 1000:
            break
        player2 = wrap(player2 + 3 * dice, 10)
        dice = wrap(dice + 3, 100)
        brojac, bodovi2 = brojac + 3, bodovi2 + player2
    return (bodovi1, bodovi2, brojac)
p1 = igra(2, player1, player2)
print("P1: ", min(p1[:2]) * p1[-1])

mem = dict()
cts = dict()
for i in range(3):
    for j in range(3):
        for k in range(3):
            cts[i + j + k + 3] = cts.get(i + j + k + 3, 0) + 1

LIMIT = 21

def igraP2(player1, player2, bodovi1, bodovi2, red):
    if (player1, player2, bodovi1, bodovi2, red) in mem:
        return mem[(player1, player2, bodovi1, bodovi2,red)]
    stanje = {0: 0, 1: 0}
    if bodovi1 >= LIMIT or bodovi2 >= LIMIT:
        stanje[int(bodovi2 > bodovi1)] += 1
        mem[(player1, player2, bodovi1, bodovi2,red)] = stanje
        return stanje

    for die in range(3, 10):
        if not red:
            newPlayer1 = wrap(player1 + die, 10)
            pom = igraP2(newPlayer1, player2, bodovi1 + newPlayer1, bodovi2, 1 - red)
        else:
            newPlayer2 = wrap(player2 + die, 10)
            pom = igraP2(player1, newPlayer2, bodovi1, bodovi2 + newPlayer2, 1 - red)
        for i in range(2):
            stanje[i] += cts[die] * pom[i]
    mem[(player1, player2, bodovi1, bodovi2, red)] = stanje
    return stanje
p2 = igraP2(player1, player2, bodovi1=0, bodovi2=0,red=0)

print("P2: ", max(p2.values()))