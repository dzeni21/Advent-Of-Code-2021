with open("dan03.txt") as f:
    input = f.read().strip().split("\n")

brojBin = len(input[0])  

gama = [None] * brojBin
epsilon = [None] * brojBin
for i in range(brojBin):
    nule = sum([input[j][i] == "0" for j in range(len(input))])
    jedinice = sum([input[j][i] == "1" for j in range(len(input))])
    if nule > jedinice:
        epsilon[i] = "1"
        gama[i] = "0"
    else:
        epsilon[i] = "0"
        gama[i] = "1"

# P1
p1 = int("".join(gama), 2) * int("".join(epsilon), 2)
print("P1: ",p1)


# Odredi broj bita
N = len(input[0])
input = [int(i, 2) for i in input]

# kisik
kisik = input.copy()
poz = N - 1
while poz >= 0 and len(kisik) > 1:
    # najcesci bit
    jedinice = sum([((x & (1 << poz)) >> poz) for x in kisik])
    nule = len(kisik) - jedinice

    if nule > jedinice:
        kisik = list(filter(lambda arg: not (arg & (1 << poz)), kisik))
    else:
        kisik = list(filter(lambda arg: (arg & (1 << poz)), kisik))
    poz -= 1

# CO2
co2 = input.copy()
poz = N - 1
while poz >= 0 and len(co2) > 1:
    # najcesci bit
    jedinice = sum([((x & (1 << poz)) >> poz) for x in co2])
    nule = len(co2) - jedinice
    if nule > jedinice:
        co2 = list(filter(lambda x: (x & (1 << poz)), co2))
    else:
        co2 = list(filter(lambda x: not (x & (1 << poz)), co2))
    poz -= 1


p2 = kisik[0] * co2[0]
print("P2: ",p2)
