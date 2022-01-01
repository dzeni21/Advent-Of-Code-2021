import itertools
import math
from functools import reduce

with open("dan18.txt") as f:
    input = f.read().strip()


def dodajLijevo(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [dodajLijevo(x[0], n), x[1]]


def dodajDesno(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [x[0], dodajDesno(x[1], n)]


def checkEksplozija(x, n = 4):
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, left, a, right = checkEksplozija(a, n - 1)
    if exp:
        return True, left, [a, dodajLijevo(b, right)], None
    exp, left, b, right = checkEksplozija(b, n - 1)
    if exp:
        return True, None, [dodajDesno(a, left), b], right
    return False, None, x, None


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, math.ceil(x / 2)]
        return False, x
    a, b = x
    promjena, a = split(a)
    if promjena:
        return True, [a, b]
    promjena, b = split(b)
    return promjena, [a, b]


def add(a, b):
    x = [a, b]
    while True:
        promjena, _, x, _ = checkEksplozija(x)
        if promjena:
            continue
        promjena, x = split(x)
        if not promjena:
            break
    return x


def magnituda(x):
    if isinstance(x, int):
        return x
    return 3 * magnituda(x[0]) + 2 * magnituda(x[1])


print("P1: ", magnituda(reduce(add, input)))
print("P2: ",  max(magnituda(add(a, b)) for a, b in itertools.permutations(input, 2)),)