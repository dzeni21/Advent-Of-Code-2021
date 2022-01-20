import itertools
from pprint import pprint

with open("dan08.txt") as f:
    input = f.read().strip().split("\n")
    podaci = [linija[linija.index("|") + 2:].split(" ") for linija in input]

uredu = [2, 4, 3, 7]
p1 = 0
for output in podaci:
    for cifra in output:
        if len(cifra) in uredu:
            p1 += 1

print("P1: ", p1)

with open("dan08.txt") as f:
    input = f.read().strip().split("\n")
    podaci = [
        [
            sorted(linija[:linija.index("|") - 1].split(" ")),
            linija[linija.index("|") + 2:].split(" ")
        ] for linija in input
    ]

cifreKljuc = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]

cifre = sorted(cifreKljuc)
cifre = tuple(cifre)

p2 = 0

for linija in podaci:
    hint = linija[0]
    assert len(hint) == 10
    num = linija[1]

    # Probaj sve moguce zamjene
    for sig in itertools.permutations("abcdefg"):
        # Ponovno kodiranje cifara
        kljuc = {}
        for c in "abcdefg":
            kljuc[c] = sig["abcdefg".index(c)]

        nHint = [] * 10
        for h in hint:
            x = ""
            for char in h:
                x += kljuc[char]
            x = "".join(sorted(x))
            nHint.append(x)

        nHint.sort()

        if tuple(nHint) == cifre:
            # Uzmi broj koji bi trebao biti
            br = []
            for i in num:
                x = ""
                for char in i:
                    x += kljuc[char]
                x = "".join(sorted(x))
                br.append(cifreKljuc.index(x))

            p2 += int("".join([str(i) for i in br]))
            break

print("P2: ", p2)
