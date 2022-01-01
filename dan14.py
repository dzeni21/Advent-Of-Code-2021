import string
from collections import defaultdict
import copy

with open("dan14.txt") as f:
    input = f.read().strip().split("\n")

elementi = string.ascii_uppercase

polimerTemplate = input[0]
pairIns = [red.split(" -> ") for red in input[2:]]

def zamijeni(string):
    noviStr = ""
    i = 0
    while i < len(string):
        noviStr += string[i]
        for start, end in pairIns:
            if string[i:i + 2] == start:
                noviStr += end
                break
        i += 1
    return noviStr

# P1
for i in range(10):
    polimerTemplate = zamijeni(polimerTemplate)

brojac = [polimerTemplate.count(i) for i in elementi if polimerTemplate.count(i) != 0]

p1 = max(brojac) - min(brojac)
print("P1: ", p1)

# P2
brojac = defaultdict(int)
for i in range(len(polimerTemplate) - 1):
    brojac[polimerTemplate[i:i + 2]] += 1

def zamijeni(brojac):
    noviBrojac = copy.copy(brojac)
    for pair in brojac:
        for poc, kraj in pairIns:
            if pair == poc:
                occurring = brojac[pair]
                noviBrojac[pair] -= occurring
                noviBrojac[pair[0] + kraj] += occurring
                noviBrojac[kraj + pair[1]] += occurring
                break

    return noviBrojac

for i in range(40):
    brojac = zamijeni(brojac)

# broji svaki element
sum = defaultdict(int)
for pair in brojac:
    sum[pair[0]] += brojac[pair]
    sum[pair[1]] += brojac[pair]

sum[polimerTemplate[0]] += 1
sum[polimerTemplate[-1]] += 1

brVal = [c[1] // 2 for c in sum.items()]

p2 = max(brVal) - min(brVal)
print("P2: ", p2)
