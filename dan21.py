from functools import lru_cache

with open("dan21.txt") as f:
    input = f.read().strip().split("\n")


class Igrac:
    def __init__(player, poz):
        player.poz = poz
        player.poeni = 0

    def unaprijed(player, die):
        player.poz += die.roll()
        player.poz = (player.poz - 1) % 10 + 1
        player.poeni += player.poz

    def pobjeda(player):
        return player.poeni >= 1000


class Dice:
    def __init__(player):
        player.val = 1
        player.rolls = 0

    def roll(player, times = 3):
        s = 0
        for _ in range(times):
            s += player.val
            player.val += 1
        player.rolls += times
        return s

d = Dice()
p1 = Igrac(int(input[0][input[0].index(": ")+2:]))
p2 = Igrac(int(input[1][input[1].index(": ")+2:]))

while True:
    p1.unaprijed(d)
    if p1.pobjeda():
        odg1 = p2.poeni * d.rolls
        break

    p2.unaprijed(d)
    if p2.pobjeda():
        odg1 = p1.poeni * d.rolls
        break

print("P1: ", odg1)


p1 = int(input[0][input[0].index(": ")+2:])
p2 = int(input[1][input[1].index(": ")+2:])

freq = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}


def unaprijed(poz, kolicina):
    return (poz + kolicina - 1) % 10 + 1


def unazad(poz, kolicina):
    return (poz - kolicina - 1) % 10 + 1


@lru_cache(None)
def dp(poz, poeni, red, init_poz):
    # Koliko postoji nacina da se dodje do odredjene tacke, na datu poziciju
    if red == 0:
        return 1 if (poeni == 0 and poz == init_poz) else 0

    if poeni <= 0:
        return 0

    odg2 = 0
    for kolicina in freq:
        if poeni - poz >= 21:
            continue

        dpVal = dp(unazad(poz, kolicina),
                    poeni - poz, red - 1, init_poz)
        odg2 += freq[kolicina] * dpVal

    return odg2


# Broj nacina do pobjede
def countPobjede(poz, drugaPoz, jeP1):
    odg2 = 0
    for endPoz in range(1, 11):
        for poeni in range(21, 31):
            for red in range(40):
                for drugiEnd_poz in range(1, 11):
                    for drugiPoeni in range(21):
                        odg2 += dp(endPoz, poeni, red, poz) * \
                        dp(drugiEnd_poz, drugiPoeni,
                               red - jeP1, drugaPoz)

    return odg2


p1 = countPobjede(p1, p2, True)
p2 = countPobjede(p2, p1, False)
print(max(p1, p2))
