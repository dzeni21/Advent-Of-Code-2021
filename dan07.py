with open("dan07.txt") as f:
    input = f.read().strip().split(",")

podaci = [int(i) for i in input]

p1 = 1 << 60
maxPoz = max(podaci)

for poz in range(maxPoz):
    r = 0
    for i in podaci:
        r += abs(poz - i)
    p1 = min(p1, r)
print("P1", p1)


p2 = 1 << 60

for pos in range(maxPoz):
    r = 0
    for i in podaci:
        udaljenost = abs(i - poz)
        cijena = udaljenost * (udaljenost + 1) // 2
        r += cijena
    p2 = min(p2, r)

print("P2", p2)
