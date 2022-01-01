with open("dan12.txt") as f:
    input = f.read().strip()

assert len(input.argv) == 2
rubovi = list(map(lambda arg: arg.split('-'), open(input.argv[1]).read().splitlines()))

def countPath(graph, checkDoublePath, node = 'start', seen = ['start']):
    if node == 'end':
        return 1
    count = 0
    for susjed in graph[node]:
        if susjed != 'start':
            if susjed[0].isupper() or susjed not in seen:
                count += countPath(graph, checkDoublePath, susjed, seen + [susjed])
            elif not checkDoublePath:
                count += countPath(graph, True, susjed, seen)
    return count

graph = dict()
for cave1, cave2 in rubovi:
        if cave1 not in graph:
            graph[cave1] = set()
        if cave2 not in graph:
            graph[cave2] = set()
        graph[cave1].add(cave2)
        graph[cave2].add(cave1)

print("P1: ", countPath(graph, True))
print("P2: ", countPath(graph, False))