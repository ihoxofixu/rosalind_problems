def splicer(reads):
    ans = set()
    for i in reads:
        ans |= set([i[1:], i[:-1]])
    return list(ans)


kmers = []
tmp = input()
while tmp != '':
    kmers.append(tmp)
    tmp = input()
composition = splicer(kmers)
adjacency_matrix = [[0 for j in range(len(composition))]
                    for i in range(len(composition))]
for i in kmers:
    starting_node = composition.index(i[:-1])
    ending_node = composition.index(i[1:])
    adjacency_matrix[starting_node][ending_node] += 1
for i in range(len(adjacency_matrix)):
    starting_node = composition[i]
    nodes = []
    for j in range(len(adjacency_matrix)):
        if adjacency_matrix[i][j] != 0:
            for it in range(adjacency_matrix[i][j]):
                nodes.append(composition[j])
    if len(nodes) != 0:
        print(starting_node, '->', ','.join(nodes))
