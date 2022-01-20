with open("dan13.txt") as f:
    tacke = set()
    while True:
        linija = f.readline().strip()
        if linija == "":
            break
        tacke.add(tuple([int(i) for i in linija.split(",")]))

    savijanje = []
    while True:
        linija = f.readline().strip()

         # VAŽNO: provjeri da li se ulazni fajl zavrsava sa novim redom
        if linija == "":
            break

        fold = linija[len("fold along "):]
        if fold[0] == "y":
            savijanje.append((0, int(fold[2:])))
        else:
            savijanje.append((int(fold[2:]), 0))


def refleksija(tacka, linija):
    if linija[0] != 0:
        return (2*linija[0] - tacka[0], tacka[1])
    return (tacka[0], 2*linija[1] - tacka[1])


# prvo savijanje
new_tacke = set()
fold = savijanje[0]

for dot in tacke:
    if fold[0] != 0:
        # vertikalno
        if dot[0] > fold[0]:
            new_tacke.add(refleksija(dot, fold))
        else:
            new_tacke.add(dot)

    else:
        # horizontalno
        if dot[1] > fold[1]:
            new_tacke.add(refleksija(dot, fold))
        else:
            new_tacke.add(dot)


p1 = len(new_tacke)
print("P1: ", p1)

for y in range(6):
    for x in range(50):
        if (x, y) in new_tacke:
            print("##", end = "")
        else:
            print("..", end = "")
    print()

