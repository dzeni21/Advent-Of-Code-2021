with open("dan07.txt") as f:
    input = f.read().strip().split(",")

br = sorted(map(int, input().split(",")))

# P2
def fuel(i):
    return sum(map(lambda arg: (abs(arg - i) * (abs(arg - i) + 1)) // 2, br))
# P1
medijan = br[len(br) // 2]

print("P1: ", sum(map(lambda arg: abs(arg - medijan), br)))
print("P2: ", fuel(sum(br) // len(br)))