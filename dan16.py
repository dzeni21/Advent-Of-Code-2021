with open("dan16.txt") as f:
    input = f.read().strip()

data = bin(int(input, base=16))[2:]
data = data.zfill(-(-len(data)//4) * 4)


def parse(packet, brojac=-1):

    if packet == "" or int(packet) == 0:
        return 0

    if brojac == 0:
        return parse(packet, brojac=-1)

    verzija = int(packet[0:3], base=2)
    tId = int(packet[3:6], base=2)

    # Literal value
    if tId == 4:
        i = 6
        brStr = ""
        kraj = False
        while not kraj:
            if packet[i] == "0":
                # Posljednji paket
                kraj = True

            brStr += packet[i+1:i+5]
            i += 5

        val = int(brStr, base=2)
        return verzija + parse(packet[i:], brojac-1)

    # u suprotnom je operator
    lenID = packet[6]
    if lenID == "0":
        # 15 bita koji reprezentuju ukupni duzinu u bitima 
        nbits = int(packet[7:22], base = 2)
        return verzija + parse(packet[22:22 + nbits], -1) + parse(packet[22+nbits:], brojac-1)

    else:
        # 11 bita koji reprezentuju ukupan broj sub-packets 
        npacks = int(packet[7:18], base=2)
        return verzija + parse(packet[18:], brojac = npacks)

p1 = parse(data)
print("P1: ", p1)

# P2

def operator(tId, val):
    if tId == 0:
        return sum(val)

    if tId == 1:
        p = 1
        for v in val:
            p *= v
        return p

    if tId == 2:
        return min(val)

    if tId == 3:
        return max(val)

    if tId == 5:
        assert len(val) == 2
        return int(val[0] > val[1])

    if tId == 6:
        assert len(val) == 2
        return int(val[0] < val[1])

    if tId == 7:
        assert len(val) == 2
        return int(val[0] == val[1])


def parseP2(x, y=-1):
    if x == y:
        return None, None

    if x > len(data) - 4:
        return None, None

    ver = int(data[x:x+3], base=2)
    tId = int(data[x+3:x+6], base=2)

    # Literal value
    if tId == 4:
        x += 6
        brStr = ""
        kraj = False
        while not kraj:
            if data[x] == "0":
                # Posljednji paket
                end = True

            brStr += data[x+1:x+5]
            x+= 5

        val = int(brStr, base = 2)
        return val, x

    # Operator packet
    subPacks = []
    nxtStart = None  

    lenID = data[x+6]
    if lenID == "0":
        # 15 bita koji reprezentuju ukupni duzinu u bitima 
        num_bits = int(data[x+7:x+22], base=2)
        kraj = x+ 22 + num_bits
        index = x+ 22
        prethodniIndex = None
        while index != None:
            prethodniIndex = index
            x, index = parse(index, j=kraj)
            subPacks.append(x)
        subPacks = subPacks[:-1]  # Ukloni posljednji
        nxtStart = prethodniIndex

    else:
        # 11 bita koji reprezentuju ukupan broj sub-packets 
        remSubPacks = int(data[x+7:x+18], base=2)
        index = x + 18
        while remSubPacks > 0:
            x, index = parse(index)
            remSubPacks -= 1
            subPacks.append(x)
        nxtStart = index

    # Procesiraj operacije
    return operator(tId, subPacks), nxtStart

p2 = parseP2(0)[0]
print("P2: ", p2)