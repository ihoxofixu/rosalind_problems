def splicer(reads):
    ans = set()
    for i in reads:
        ans |= set([i[1:], i[:-1]])
    return list(ans)


def construct_de_brujn(kmers):
    comp = splicer(kmers)
    adj_matrix = [[0 for j in range(len(comp))] for i in range(len(comp))]
    for i in kmers:
        starting_node = comp.index(i[:-1])
        ending_node = comp.index(i[1:])
        adj_matrix[starting_node][ending_node] += 1
    return adj_matrix, comp


list_of_kmers = []
tmp = input()
while tmp != '':
    list_of_kmers.append(tmp)
    tmp = input()
adjacency_matrix, composition = construct_de_brujn(list_of_kmers)
for i in range(len(adjacency_matrix)):
    starting_node = composition[i]
    nodes = []
    for j in range(len(adjacency_matrix)):
        if adjacency_matrix[i][j] != 0:
            for it in range(adjacency_matrix[i][j]):
                nodes.append(composition[j])
    if len(nodes) != 0:
        print(starting_node, '->', ','.join(nodes))
