with open("dan06.txt") as f:
    input = f.read().strip().split(",")
    podaci = [int(i) for i in input]

dani = 80

for _ in range(days):
    n = len(podaci)
    for i in range(n):
        if podaci[i] == 0:
            podaci[i] = 6
            podaci.append(8)
        else:
            podaci[i] -= 1

p1 = len(podaci)
print(p1)
