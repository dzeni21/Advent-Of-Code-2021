import functools

with open('dan24.txt') as f:
	input = f.read().splitlines()

# podijeliti input na blokove koji počinju sa 'inp w'
blok = []
trenutniBlok = []

for red in input:
	instr = red.split(' ')
	if instr[0] == 'inp':
		assert(instr[1] == 'w')
		blok.append(trenutniBlok)
		trenutniBlok = []
	else:
		trenutniBlok.append(instr)

blok.append(trenutniBlok)
blok = blok[1:]

slova = 'wxyz'
dp = {}

# vrati z vrijednost nakon bloka na 'index', s obzirom na trenutne vrijednosti 'w' i 'z'
def asembler(index, w, z):
	vrijednosti = [w, 0, 0, z]
	# svaka instr je 'op a b;
	for instr in blok[index]:
		index = slova.index(instr[1])
		# pohrani vrijednost b
		if instr[2].lstrip('-').isdigit():
			val = int(instr[2])
		else:
			val = vrijednosti[slova.index(instr[2])]

		if instr[0] == 'mul':
			vrijednosti[index] *= val
		elif instr[0] == 'add':
			vrijednosti[index] += val
		elif instr[0] == 'div':
			vrijednosti[index] = int(vrijednosti[index]/val)
		elif instr[0] == 'mod':
			vrijednosti[index] = vrijednosti[index] % val
		else:
			assert(instr[0] == 'eql')
			vrijednosti[index] = int(vrijednosti[index] == val)

	return vrijednosti[3]

path = []

# vrati True ako je moguće doci do kraja, s obzirom na trenutnu vrijednost 'z' i blok na kojem se nalazimo
@functools.cache
def checkEndP1(index, curZ):
	global path
	if index == len(blok):
		if curZ == 0:
            #P1
			print(''.join([str(i) for i in path]))
			return True
		return False

	# pokušaj sa svim w od 9 => 1 pošto želimo maksimizirati w
	for w in range(9, 0, -1):
		path.append(w)
		if checkEndP1(index + 1, asembler(index, w, curZ)):
			return True
		path = path[:-1]
	return False

checkEndP1(0, 0)

# P2
path = []

@functools.cache
def checkEndP2(index, curZ):
	# nastavi povecavati granicu dok se ne dobije (najmanje) rjesenje
	if curZ >= 1000000:
		return False

	global path
	if index == len(blok):
		if curZ == 0:
			print(''.join([str(p) for p in path]))
			return True
		return False

	# probaj sve w od 1 => 10 (prvo najmanji)
	for w in range(1, 10):
		path.append(w)
		if checkEndP2(index + 1, asembler(index, w, curZ)):
			return True
		path = path[:-1]
	return False

checkEndP2(0, 0)