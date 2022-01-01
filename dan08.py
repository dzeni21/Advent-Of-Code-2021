with open("dan08.txt") as f:
    input = f.read().strip().split("\n")

lijevo = []
desno = []
skup = [2, 4, 3, 7]

# Parse
for red in range(1, len(input)):
    red = red.strip().split(" | ")
    lijevo.append(red[0].split())
    desno.append(red[1].split())
    # P1
    print("P1: ", sum(map(lambda arg: len(list(filter(lambda p: len(p) in skup, arg))), desno)))

# P2
for i in range(len(desno)):
    map = dict()
    for j in lijevo[i]:
        if len(j) == 2:
            jedan = str().join(sorted(j))
            map[jedan] = '1'
        elif len(j) == 3:
            sedam = str().join(sorted(j))
            map[sedam] = '7'
        elif len(j) == 4:
            cetiri = str().join(sorted(j))
            map[cetiri] = '4'
        elif len(j) == 7:
            osam = str().join(sorted(j))
            map[osam] = '8'

    for j in lijevo[i]:
        if len(j) == 6:
            if set(cetiri).issubset(set(j)):
                devet = str().join(sorted(j))
                map[devet] = '9'
            elif set(jedan).issubset(set(j)):
                nula = str().join(sorted(j))
                map[nula] = '0'
            else:
                sest = str().join(sorted(j))
                map[sest] = '6'

    for j in lijevo[i]:
        if len(j) == 5:
            if not (set(nula) - set(sest)).issubset(set(j)):
                map[str().join(sorted(j))] = '5'
            elif set(jedan).issubset(set(j)):
                map[str().join(sorted(j))] = '3'
            else:
                map[str().join(sorted(j))] = '2'
    
    desno[i] = int(str().join(list(map(lambda arg: map[str().join(sorted(arg))], desno[i]))))
print("P2: ", sum(desno))