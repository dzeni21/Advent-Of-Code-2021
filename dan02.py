with open("dan02.txt") as f:
    input = f.read().strip().split("\n")

x = 0
y1 = 0
y2 = 0

for red in range(1, len(input)):
    dir, num = red.split()
    num = int(num)
    if dir == "forward":
        x += num
        y2 += y1 * num
    elif dir == "up":
        y1 -= num
    else:
        y1 += num

p1 = x * y1
p2 = x * y2

print("P1: ", p1)
print("P2: ", p2)