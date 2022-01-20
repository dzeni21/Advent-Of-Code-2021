with open("dan17.txt") as f:
    input = f.read().strip()

podaci = input[len("target area: x="):]
podaci = podaci.split(", y=")
xRange = (
    int(podaci[0][:podaci[0].index("..")]),
    int(podaci[0][podaci[0].index("..")+2:])
)
yRange = (
    int(podaci[1][:podaci[1].index("..")]),
    int(podaci[1][podaci[1].index("..")+2:])
)

cilj = (xRange, yRange)


def iteracija(poz, brzina):
 # vrati novu poziciju i brzinu
    new_poz = [0, 0]
    new_brzina = [0, 0]

    new_poz[0] = poz[0] + brzina[0]
    new_poz[1] = poz[1] + brzina[1]

    new_brzina[1] = brzina[1] - 1
    if brzina[0] > 0:
        new_brzina[0] = brzina[0] - 1
    if brzina[0] < 0:
        new_brzina[0] = brzina[0] + 1

    return new_poz, new_brzina


def within(poz, cilj):
    return (cilj[0][0] <= poz[0] <= cilj[0][1]) \
        and (cilj[1][0] <= poz[1] <= cilj[1][1])


def jeProslost(poz, brzina, cilj):
    if brzina[0] > 0 and poz[0] > cilj[0][1]:
        return True
    if brzina[0] < 0 and poz[0] < cilj[0][0]:
        return True
    if brzina[1] < 0 and poz[1] < cilj[1][0]:
        return True
    return False


def hit(brzina, cilj):
   
    # cilj = [xRange, yRange]

    poz = (0, 0)
    maxY = 0
    while not jeProslost(poz, brzina, cilj):
        maxY = max(maxY, poz[1])
        if within(poz, cilj):
            return True, maxY
        poz, brzina = iteracija(poz, brzina)

    return False, None


# limit y brzine
maxYv = abs(cilj[1][0])

yv = maxYv
while yv >= cilj[1][0]:
    done = False
    for xv in range(-100, 101):
        works, maxY = hit((xv, yv), cilj)
        if works:
            done = True
            break

    if done:
        break

    print(yv)

    yv -= 1


odg = 0
yv = maxYv
while yv >= cilj[1][0]:
    done = False
    for xv in range(-100, 101):
        works = hit((xv, yv), cilj)
        if works:
            odg += 1
            done = True

    yv -= 1

print(odg)
