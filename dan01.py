with open("dan01.txt") as f:
    input = [int(i) for i in f.read().strip().split("\n")]

rez = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        rez += 1
print("P1: ", rez)

rez = 0
for i in range(3, len(input)):
    if input[i] > input[i-3]:
        rez += 1
print("P2: ", rez)