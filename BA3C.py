class vertex():
    def __init__(self, string=''):
        self.suffix = string[1:]
        self.prefix = string[:-1]
        self.read = string


reads = []
tmp = input()
while tmp != '':
    reads.append(vertex(tmp))
    tmp = input()
reads.sort(key=lambda x: x.read)
adjacency_matrix = [[] for i in range(len(reads))]
for i in range(len(reads)):
    for j in range(i, len(reads)):
        if i != j:
            if reads[i].suffix == reads[j].prefix:
                adjacency_matrix[i].append(j)
            elif reads[j].suffix == reads[i].prefix:
                adjacency_matrix[j].append(i)
for i in range(len(adjacency_matrix)):
    for j in adjacency_matrix[i]:
        print(reads[i].read, '->', reads[j].read)
