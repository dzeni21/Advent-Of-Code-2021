with open("dan10.txt") as f:
    input = f.read().strip()
podaci = input.split("\n")

poeni = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
parovi = ["()", "[]", "<>", "{}"]

def parse(linija):
    stek = []
    for c in linija:
        checkUredu = False
        for p in parovi:
            if c == p[0]:
                stek.append(c)
                checkUredu = True
            elif c == p[1]:
                if stek[-1] == p[0]:
                    stek.pop()
                    checkUredu = True

        if not checkUredu:
            return poeni[c]

    return 0

p1 = 0
for linija in podaci:
    p1 += parse(linija)

print("P1: ", p1)

errorPoeni = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
incrPoeni = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def parse(linija):
    stek = []
    for c in linija:
        checkUredu = False
        for p in parovi:
            if c == p[0]:
                stek.append(c)
                checkUredu = True
            elif c == p[1]:
                if stek[-1] == p[0]:
                    stek.pop()
                    checkUredu = True

        if not checkUredu:
            return errorPoeni[c]

    return 0


def zavrseno(linija):
    stek = []
    p2 = 0
    for c in linija:
        for p in parovi:
            if c == p[0]:
                stek.append(c)
            elif c == p[1]:
                if stek[-1] == p[0]:
                    stek.pop()

    for c in stek[::-1]:
        p2 *= 5
        p2 += incrPoeni[c]

    return p2


# Izbrisi ostecene stvari
podaci = [linija for linija in podaci if parse(linija) == 0]

poeni = []
for linija in podaci:
    poeni.append(zavrseno(linija))

poeni.sort()
p2 = poeni[len(poeni) // 2]
print("P2: ", p2)
