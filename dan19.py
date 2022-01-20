from functools import lru_cache
from itertools import combinations
from collections import defaultdict

with open("dan19.txt") as f:
    input = f.read().strip()
    input = input.split("\n")

# Parse
scanner = []
i = 0
while i < len(input):
    beacon = []
    while i < len(input) and len(input[i]) > 0:
        if "--- scanner" in input[i]:
            i += 1
            continue
        beacon.append(tuple([int(i)
                       for i in input[i].split(",")]))
        i += 1
    scanner.append(tuple(sorted(beacon)))
    i += 1

@lru_cache(None)
def inv(rot):
    a = rotacije((1, 2, 3))[rot]
    for inv_rot in range(24):
        if rotacije(a)[inv_rot] == (1, 2, 3):
            return inv_rot


@lru_cache(None)
def compose(rot1, rot2):
    a = rotacije(rotacije((1, 2, 3))[rot1])[rot2]
    for comp_rot in range(24):
        if rotacije((1, 2, 3))[comp_rot] == a:
            return comp_rot

def sub(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2])

def add(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])

def neg(x):
    return (-x[0], -x[1], -x[2])

def manhattanDist(x, y):
    return sum([abs(x[i] - y[i]) for i in range(3)])

@lru_cache(None)
def rotacije(tacka):
    x, y, z = tacka
    return [
        (x, y, z), (x, z, -y), (x, -y, -z), (x, -z, y),
        (-x, -y, z), (-x, z, y), (-x, y, -z), (-x, -z, -y),
        (y, z, x), (y, x, -z), (y, -z, -x), (y, -x, z),
        (-y, -z, x), (-y, x, z), (-y, z, -x), (-y, -x, -z),
        (z, x, y), (z, y, -x), (z, -x, -y), (z, -y, x),
        (-z, -x, y), (-z, y, x), (-z, x, -y), (-z, -y, -x)
    ]

def hash(a):
    return tuple(sorted([abs(i) for i in a]))


def offset_set(beacon):
    rez = set()
    for x, y in combinations(beacon, r=2):
        rez.add(sub(x, y))
    return rez


@lru_cache(None)
def udaljenost_set(beacon):
    return set([hash(x) for x in offset_set(beacon)])


def checkOverlap(a, b):
    if len(set.intersection(udaljenost_set(a), udaljenost_set(b))) >= 66:
        return True
    return False


def orientacija(a, b, base_index, rots):
    a_set = set(a)

    for rot in rots:
        drugiBeacon = tuple([rotacije(beacon)[rot] for beacon in b])
        for drugiBase in drugiBeacon:
            translacija = sub(a[base_index], drugiBase)
            drugiBeacon_translated = set(
                [add(beacon, translacija) for beacon in drugiBeacon])

            if len(set.intersection(a_set, drugiBeacon_translated)) >= 12:
                return translacija, rot

    return None

def overlap(a, b):
    if not checkOverlap(a, b):
        return False

    for i, j in combinations(range(len(a)), r=2):
        for k, m in combinations(range(len(b)), r=2):
            da = sub(a[i], a[j])
            db = sub(b[k], b[m])
            if not hash(da) == hash(db):
                continue

            rot = []

            rot_db = rotacije(db)
            for i in range(24):
                if rot_db[i] == da:
                    rot.append(i)
                    break
            db = neg(db)
            rot_db = rotacije(db)
            for i in range(24):
                if rot_db[i] == da:
                    rot.append(i)
                    break

            if len(rot) == 0:
                continue

            return orientacija(a, b, i, rot)

    return False


adj = defaultdict(list)
for i in range(len(scanner)):
    for j in range(i + 1, len(scanner)):
        x = overlap(scanner[i], scanner[j])
        if x:
            adj[i].append((j, x[0], x[1]))
            adj[j].append((i, rotacije(neg(x[0]))[inv(x[1])], inv(x[1])))


beacon = set()

scannersPairs = {}
stek = [(0, (0, 0, 0), 0)]
posjeta = set()
while len(stek) > 0:
    cvor, trans, rot = stek.pop()

    if cvor in posjeta:
        continue
    posjeta.add(cvor)

    scannersPairs[cvor] = trans

    trenutni_beacon = [add(rotacije(beacon)[rot], trans)
                   for beacon in scanner[cvor]]

    for b in trenutni_beacon:
        beacon.add(b)

    for nbr in adj[cvor]:
        if nbr[0] in posjeta:
            continue
        nTrans = add(trans, rotacije(nbr[1])[rot])
        nRot = compose(nbr[2], rot)
        stek.append((nbr[0], nTrans, nRot))

print("P1: ", len(beacon))


maxDist = 0
for a, b in combinations(scannersPairs.values(), r=2):
    maxDist = max(maxDist, manhattanDist(a, b))

print("P2: ", maxDist)
