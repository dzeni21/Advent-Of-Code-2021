with open("dan03.txt") as f:
    input = f.read().strip().split("\n")

def binToDec(broj):
    ret = 0
    for i in broj:
        ret *= 2
        ret += int(i)
    return ret

bits1 = []
pom = []

for red in range(1, len(input)):
    bits1.append(red.strip())

# P1
for red in bits1:
    if not pom:
        pom = list(map(int, red))
    else:
        for i in range(len(red)):
            pom[i] += int(red[i])

n = len(bits1)
gamma = str().join(list(map(lambda arg: str(int(arg > n/2)), pom)))
epsilon = str().join(list(map(lambda arg: str(int(arg < n/2)), pom)))
x1 = binToDec(gamma)
x2 = binToDec(epsilon)

print("P1:", x1 * x2)

# P2
b = len(bits1[0])
bits2 = bits1.copy()
for i in range(b):
    if len(bits1) == 1:
        break
    # oxygen i co2 rating
    brojac = [0, 0]
    for bit in bits1:
        brojac[int(bit[i])] += 1
    if brojac[0] > brojac[1]:
        bits1 = list(filter(lambda arg: arg[i] == "0", bits1))
    else:
        bits1 = list(filter(lambda arg: arg[i] == "1", bits1))

for i in range(b):
    if len(bits2) == 1:
        break
    brojac = [0, 0]
    for bit in bits2:
        brojac[int(bit[i])] += 1
    if brojac[0] > brojac[1]:
        bits2 = list(filter(lambda arg: arg[i] == "1", bits2))
    else:
        bits2 = list(filter(lambda arg: arg[i] == "0", bits2))

print("P2: ", binToDec(bits1[0]) * binToDec(bits2[0]))