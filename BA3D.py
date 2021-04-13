def splitter(string, length):
    ans = []
    for i in range(len(string) - length + 1):
        ans.append(string[i:i+length])
    return ans


def glue_rows(matrix, l1, l2):
    for i in range(len(matrix[l1])):
        matrix[l1][i] += matrix[l2][i]
    matrix = matrix[:l2] + matrix[l2+1:]
    return matrix


def glue_columns(matrix, c1, c2):
    for i in range(len(matrix)):
        matrix[i][c1] += matrix[i][c2]
        matrix[i] = matrix[i][:c2] + matrix[i][c2+1:]
    return matrix


def glue(matrix, dict):
    i = 0
    while i < len(matrix):
        j = i + 1
        while j < len(matrix):
            if dict[i] == dict[j]:
                matrix = glue_rows(matrix, i, j)
                matrix = glue_columns(matrix, i, j)
                dict = dict[:j] + dict[j+1:]
            j += 1
        i += 1
    return matrix, dict


k = int(input())
dna = input()
composition = splitter(dna, k-1)
adjacency_matrix = [[int(i == j - 1) for j in range(len(composition))]
                    for i in range(len(composition))]
adjacency_matrix, composition = glue(adjacency_matrix, composition)
for i in range(len(adjacency_matrix)):
    starting_node = composition[i]
    nodes = []
    for j in range(len(adjacency_matrix)):
        if adjacency_matrix[i][j] != 0:
            for it in range(adjacency_matrix[i][j]):
                nodes.append(composition[j])
    if len(nodes) != 0:
        print(starting_node, '->', ','.join(nodes))
