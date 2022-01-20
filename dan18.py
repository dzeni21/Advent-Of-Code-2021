with open("dan18.txt") as f:
    input = f.read().strip().split("\n")
podaci = [eval(line) for line in input]

# Prikazujemo podatke kao stablo
class Cvor:
    def __init__(s, val=None):
        s.val = val
        s.left = None
        s.right = None
        s.par = None

    def __str__(s):
        if isinstance(s.val, int):
            return str(s.val)
        return f"[{str(s.left)},{str(s.right)}]"


def parse(brFish):
    korijen = Cvor()
    if isinstance(brFish, int):
        korijen.val = brFish
        return korijen

    korijen.left = parse(brFish[0])
    korijen.right = parse(brFish[1])
    korijen.left.par = korijen
    korijen.right.par = korijen

    smanji(korijen)

    return korijen


def dodaj(a, b):
# dodaj dva stabla
    korijen = Cvor()
    korijen.left = a
    korijen.right = b
    korijen.left.par = korijen
    korijen.right.par = korijen
    smanji(korijen)
    return korijen


def magnituda(korijen):
    if isinstance(korijen.val, int):
        return korijen.val

    return 3 * magnituda(korijen.left) + 2 * magnituda(korijen.right)


def smanji(korijen):
    checkDone = True

    stek = [(korijen, 0)]

    while len(stek) > 0: 
        Cvor, dubina = stek.pop()

        if Cvor == None:
            continue

        stanje = (Cvor.left == None and Cvor.right == None) or (
            Cvor.left.val != None and Cvor.right.val != None)

        if dubina >= 4 and Cvor.val == None and stanje:
            # Idi uz stek i pronađi lijevi cvor
            prev_Cvor = Cvor.left
            cur_Cvor = Cvor
            while cur_Cvor != None and (cur_Cvor.left == prev_Cvor or cur_Cvor.left == None):
                prev_Cvor = cur_Cvor
                cur_Cvor = cur_Cvor.par

            # Lijevi cvor mora da postoji
            if cur_Cvor != None:

                cur_Cvor = cur_Cvor.left
                while cur_Cvor.val == None:
                    if cur_Cvor.right != None:
                        cur_Cvor = cur_Cvor.right
                    else:
                        cur_Cvor = cur_Cvor.left

                # azuriraj vrijednosti
                cur_Cvor.val += Cvor.left.val

            # Idi uz stek i pronađi desni cvor
            prev_Cvor = Cvor.right
            cur_Cvor = Cvor
            while cur_Cvor != None and (cur_Cvor.right == prev_Cvor or cur_Cvor.right == None):
                prev_Cvor = cur_Cvor
                cur_Cvor = cur_Cvor.par

            # desni cvor mora da postoji
            if cur_Cvor != None:

                cur_Cvor = cur_Cvor.right
                while cur_Cvor.val == None:
                    if cur_Cvor.left != None:
                        cur_Cvor = cur_Cvor.left
                    else:
                        cur_Cvor = cur_Cvor.right

                # azuriraj vrijednosti
                cur_Cvor.val += Cvor.right.val

            Cvor.val = 0
            Cvor.left = None
            Cvor.right = None

            checkDone = False
            break

        stek.append((Cvor.right, dubina + 1))
        stek.append((Cvor.left, dubina + 1))

    if not checkDone:
        smanji(korijen)
        return

    stek = [korijen]
    while len(stek) > 0:
        Cvor = stek.pop()
        if Cvor == None:
            continue

        if Cvor.val != None:
            # split
            assert Cvor.left == None and Cvor.right == None
            if Cvor.val >= 10:
                Cvor.left = Cvor(Cvor.val//2)
                Cvor.right = Cvor(Cvor.val - (Cvor.val//2))
                Cvor.left.par = Cvor
                Cvor.right.par = Cvor
                Cvor.val = None

                checkDone = False
                break

        stek.append(Cvor.right)
        stek.append(Cvor.left)

    # ako nije checkDone, nastavi
    if not checkDone:
        smanji(korijen)

korijen = parse(podaci[0])

i = 1
while i < len(podaci):
    korijen = dodaj(korijen, parse(podaci[i]))
    i += 1

p1 = magnituda(korijen)
print("P1: ", p1)

def dajMag(a, b):
    return magnituda(dodaj(a, b))

p2 = 0
for i in range(len(podaci)):
    for j in range(len(podaci)):
        if i == j:
            continue

        a, b = parse(podaci[i]), parse(podaci[j])

        if dajMag(a, b) > ans:
            ans = dajMag(a, b)

print("P2: ", p2)
