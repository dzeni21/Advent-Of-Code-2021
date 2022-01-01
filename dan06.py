with open("dan06.txt") as f:
    input = f.read().strip().split(",")

x = [0] * 10
br = list(map(int, input().split(",")))

for i in br:
    x[i] += 1

for j in range(256):
    pom = [0] * 10
    for i in range(10):
        if i:
            pom[i - 1] += x[i]
        else:
            pom[6] += x[0]
            pom[8] += x[0]
    x = pom
    if j == 79: 
        print("P1: ", sum(x))
print("P2:", sum(x))