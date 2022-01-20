import heapq
from collections import defaultdict

with open("dan15.txt") as f:
    input = f.read().strip()
podaci = [[int(i) for i in linija] for linija in input.split("\n")]

n = len(podaci)
m = len(podaci[0])

cijena = defaultdict(int)

pq = [(0, 0, 0)]
heapq.heapify(pq)
posjeta = set()

while len(pq) > 0:
    c, red, kol = heapq.heappop(pq)

    if (red, kol) in posjeta:
        continue
    posjeta.add((red, kol))

    cijena[(red, kol)] = c

    if red == n - 1 and kol == m - 1:
        break

    for dr, dk in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr = red + dr
        nk = kol + dk
        if not (0 <= nr < n and 0 <= nk < m):
            continue

        heapq.heappush(pq, (c + podaci[nr][nk], nr, nk))


print("P1: ",cijena[(n - 1, m - 1)])


redovi = n * 5
kolone = m * 5


def get(r, k):
    x = (podaci[r % n][k % m] +
         (r // n) + (k // m))
    return (x - 1) % 9 + 1


pq = [(0, 0, 0)]
heapq.heapify(pq)
posjeta = set()

while len(pq) > 0:
    c, red, kol = heapq.heappop(pq)

    if (red, kol) in posjeta:
        continue
    posjeta.add((red, kol))

    cijena[(red, kol)] = c

    if red == redovi - 1 and kol == kolone - 1:
        break

    for dr, dk in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr = red + dr
        nc = kol + dk
        if not (0 <= nr < redovi and 0 <= nk < kolone):
            continue

        heapq.heappush(pq, (c + get(nr, nk), nr, nk))


print("P2: ",cijena[(redovi - 1, kolone - 1)])
