from collections import defaultdict
from pprint import pprint
import heapq


with open("dan23.txt") as f:
    input = f.read().strip().split("\n")

hodnik = input[1][1:12]
red1 = input[2][3:10:2]
red2 = input[3][3:10:2]

#Stanje amfipoda može se predstaviti sa tuple:
#     (lokacija, prostorija, dubina)
# Pretpostavimo da su se svi amfipodi potpuno pomjerili
# Soba je jedna od (2, 4, 6, 8)


def printAmphipod(amphi):
    grid = """
#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  ######### """.strip()
    grid = [list(red) for red in grid.split("\n")]
    for i, stanje in enumerate(amphi):
        loc, soba, dubina = stanje
        ch = "ABCD"[i//2]
        if loc != -1:
            grid[1][loc + 1] = ch
        else:
            grid[dubina + 1][soba + 1] = ch


def checkBlokada(amphi, index, dest):
    # Provjeri ima li amfipoda između pods[index] i destSoba
    assert len(amphi) == 8

    locHodnik, soba, _ = amphi[index]
    assert locHodnik == -1 or soba == -1
    loc = max(locHodnik, soba)

    for i in range(8):
        if i == index or amphi[i][0] == -1:
            continue

        nLoc = amphi[i][0]
        assert loc != nLoc

        if (dest <= nLoc <= loc) or (loc <= nLoc <= dest):
            return True

    return False


def getSoba(amphi, ciljSoba):
    # Vrati listu amfipoda u datoj sobi
    assert ciljSoba in [2, 4, 6, 8]
    ret = [-1] * 2

    for i, apod in enumerate(amphi):
        tip = i // 2
        loc, soba, dubina = apod
        if soba != -1:
            assert loc == -1 and dubina != -1
            if soba != ciljSoba:
                continue
            ret[2 - dubina] = tip

    # Provjeri da je popunjena odozdo prema gore
    pos = 0
    while pos < 2 and ret[pos] != -1:
        pos += 1
    while pos < 2:
        assert ret[pos] == -1
        pos += 1

    return ret


def nextState(stanje):
    # Izracunaj sva sljedeca stanja iz datog stanja
    energy, amphi = stanje
    assert len(amphi) == 8

    for i, amphipod in enumerate(amphi):
        tip = i // 2
        loc, soba, dubina = amphipod

        assert not loc in [2, 4, 6, 8]

        # Je li ovaj amfipod smjesten?
        if loc == -1:
            assert soba != -1
            if soba == (tip + 1) * 2:
                if dubina == 2:
                    continue

                partners = amphi[tip*2 + (1 - i % 2)]
                if (partners[2], dubina) in [(1, 2), (2, 1)]:
                    # Svi su se smjestili
                    continue

        if True:
            bezEnergy = 0 if soba == -1 else dubina
            practLoc = max(loc, soba)

            destSoba = (tip + 1) * 2

            # Ako je u sobi i zeli da izadje, prvo proveri da li zaista moze da izadje
            good = True
            if soba != -1 and dubina == 2:
                assert loc == -1
                checkBlock = False
                for j in range(8):
                    if j == i:
                        continue
                    if amphi[j][1] == soba and amphi[j][2] == 1:
                        checkBlock = True
                        break

                good = not checkBlock

            if good:
                # Ima li stranaca u ovoj sobi?
                stranci = False
                for j in range(8):
                    if j == i or j == tip*2 + (1 - i % 2) or amphi[j][1] == -1:
                        # Je li sam, ili je partner, ili nije u svojoj sobi
                        continue

                    if amphi[j][1] == destSoba:
                        stranci = True
                        break

                if not stranci:
                    partners = amphi[tip*2 + (1 - i % 2)]

                    if partners[1] == (tip + 1) * 2:
                        if partners[2] != 1:
                            assert partners[2] == 2

                            # partners zauzima na dubini 2 
                            if not checkBlokada(amphi, i, destSoba):
                                moveEnergija = pow(10, tip) * (abs(practLoc - destSoba) + 1 + bezEnergy)
                                amphiCopy = list(amphi)
                                amphiCopy[i] = (-1, destSoba, 1)
                                yield energy + moveEnergija, tuple(amphiCopy)

                    else:
                        # Mozda ima i drugih u ovoj sobi
                        if not any([amphi[j][1] == destSoba for j in range(8) if j != i]):

                            if not checkBlokada(amphi, i, destSoba):

                                # Ako je prazno, moze se preseliti ovamo
                                moveEnergija = pow(10, tip) * (abs(practLoc - destSoba) + 2 + bezEnergy)
                                amphiCopy = list(amphi)
                                amphiCopy[i] = (-1, destSoba, 2)
                                yield energy + moveEnergija, tuple(amphiCopy)

        # U sobi
        if soba == -1:
            assert loc != -1
            continue

        assert soba != -1 and dubina != -1 and loc == -1

        # Provjeri ima li neko da blokira u sobi
        if dubina == 2:
            checkBlock = False
            for j in range(8):
                if j == i:
                    continue

                if amphi[j][1] == soba and amphi[j][2] == 1:
                    checkBlock = True
                    break
            if checkBlock:
                continue

        # Idi u hodnik?
        for destLoc in [0, 1, 3, 5, 7, 9, 10]:
            moveEnergija = pow(10, tip) * (abs(soba - destLoc) + (dubina))

            if checkBlokada(amphi, i, destLoc):
                continue

            amphiCopy = list(amphi)
            amphiCopy[i] = (destLoc, -1, -1)
            yield energy + moveEnergija, tuple(amphiCopy)

        # Done :)


def checkEnd(amphi):
    for i in range(8):
        amphipod = amphi[i]
        loc, soba, dubina = amphipod
        if loc != -1:
            assert soba == -1
            return False

        if soba != (i//2)*2 + 2:
            return False

    return True


pocAmphi = [None] * 8
tipBrojac = [0, 0, 0, 0]

# "Parse" hodnik
for loc in range(11):
    if hodnik[loc] == ".":
        continue
    tip = "ABCD".index(hodnik[loc])
    pocAmphi[tip*2 + tipBrojac[tip]] = (loc, -1, -1)
    tipBrojac[tip] += 1

# "Parse" sobe
for red, dubina in [(red1, 1), (red2, 2)]:
    for i in range(4):
        if red[i] == ".":
            continue
        tip = "ABCD".index(red[i])
        pocAmphi[tip*2 + tipBrojac[tip]] = (-1, (i*2)+2, dubina)
        tipBrojac[tip] += 1


pocStanje = 0, tuple(pocAmphi)
org = defaultdict(tuple)

checkPosjeta = set()
energy = defaultdict(int)

endAmphi = None
p1 = None

# Dijkstrin algoritam
ps = [pocStanje]
while len(ps) > 0:
    trenutnaEnergija, trenutniAmphi = heapq.heappop(ps)

    if trenutniAmphi in checkPosjeta:
        continue
    checkPosjeta.add(trenutniAmphi)

    energy[trenutniAmphi] = trenutnaEnergija
    if checkEnd(trenutniAmphi):
        ans = trenutnaEnergija
        endAmphi = trenutniAmphi
        break

    for nextStanje in nextState((trenutnaEnergija, trenutniAmphi)):
        if nextStanje[1] in checkPosjeta:
            continue

        org[nextStanje[1]] = trenutniAmphi
        heapq.heappush(ps, nextStanje)


trenutniAmphi = endAmphi
while org[trenutniAmphi] != tuple():
    print(energy[trenutniAmphi])
    printAmphipod(trenutniAmphi)
    trenutniAmphi = org[trenutniAmphi]

print("P1: ", p1)



