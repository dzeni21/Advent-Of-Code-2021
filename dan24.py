from itertools import product

with open("dan24.txt") as f:
    input = f.read().strip().split("\n\n")[4:5]

koraci = [6, 12, 8, None, 7, 12, 2, None, 4, None, None, None, None, None]
potrebno = [None, None, None, 11, None, None, None, 7, None, 6, 10, 15, 9, 0]

inputSpace = product(range(9, 0, -1), repeat = 7)

def radi(cifre):
    z = 0
    odg1 = [0] * 14

    cifreIdx = 0

    for i in range(14):
        incr, modReq = koraci[i], potrebno[i]

        if incr == None:
            assert modReq != None
            odg1[i] = ((z % 26) - modReq)
            z //= 26
            if not (1 <= odg1[i] <= 9):
                return False

        else:
            assert incr != None
            z = z * 26 + cifre[cifreIdx] + incr
            odg1[i] = cifre[cifreIdx]
            cifreIdx += 1

    return odg1


for cifre in inputSpace:
    odg1 = radi(cifre)
    if odg1:
        print("".join([str(i) for i in odg1]))
        break

inputSpace = product(range(1, 10), repeat = 7)

for digits in inputSpace:
    odg2 = radi(cifre)
    if odg2:
        print("".join([str(i) for i in odg2]))
        break
