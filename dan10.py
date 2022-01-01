
with open("dan10.txt") as f:
    input = f.read().strip()

#definiramo simbole
openBrackets = '([{<'
closeBrackets = ')]}>'

p1Points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

corrupted = dict() # prati oštećene simbole
potrebnoZaIspravljanje = [] # prati šta nam je potrebno da ispravimo liniju

for red in input:
    ocekivano = []
    otvoreno = []

    for i, ch in enumerate(red):
        otvoreno.append(ch)

        # ako smo otvorili 'chunk', ovo prati odgovarajući closerBracket za chunk   
        if ch in openBrackets:
            ocekivano.append(closeBrackets[openBrackets.index(ch)])
        else:
            # chunk je ok
            if closeBrackets.index(ch) == openBrackets.index(opened[-2]): 
                opened = opened[:-2] 
                ocekivano.pop() 
            
            # chunk nije ok
            else:
                if ch in corrupted: # prati koliko simbola su osteceni
                    corrupted[ch] += 1
                else:
                    corrupted[ch] = 1
                
                ocekivano.clear()
                break

    if ocekivano:
        ocekivano.reverse()
        potrebnoZaIspravljanje.append(ocekivano)


allPoints = 0    
for i,j in corrupted.items():
    allPoints += p1Points[i] * j

print("P1: ", allPoints)

p2Points = []
for i in potrebnoZaIspravljanje:
    score = 0
    for ch in i:
        score = score * 5 + closeBrackets.index(ch) + 1 
    p2Points.append(score)

p2Points.sort()
ret = p2Points[len(p2Points)//2]

print("P2: ", ret)   