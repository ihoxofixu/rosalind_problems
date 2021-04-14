edges_to_do = 0
id_data = {}
adjacency_list = []
tmp = input()
while tmp != '':
    start, trash, ends = tmp.split()
    start, ends = int(start), list(map(int, ends.split(',')))
    id_data[len(adjacency_list)] = start
    adjacency_list.append(ends)
    edges_to_do += len(ends)
    tmp = input()


def adj_list_remake(key_value=id_data, adj_list=adjacency_list):
    value_key = {}
    for i in key_value:
        value_key[key_value[i]] = i
    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            adj_list[i][j] = value_key[adj_list[i][j]]
    return adj_list


adjacency_list = adj_list_remake()
visited_list = []
for i in range(len(adjacency_list)):
    visited_list.append([])


def all_vertex_edges_done(vertex_id, adj_list=adjacency_list,
                          visited=visited_list):
    for j in range(len(adj_list[vertex_id])):
        if adj_list[vertex_id][j] not in visited[vertex_id]:
            return False
    return True


vertex_id = 0
path = []
edges_done = 0
while edges_done != edges_to_do:
    if all_vertex_edges_done(vertex_id):
        new_start = -1
        for i in range(len(path)):
            if not all_vertex_edges_done(path[i]):
                new_start = i
                break
        path = path[new_start+1:] + path[:new_start+1]
        vertex_id = path[len(path)-1]
    else:
        for i in adjacency_list[vertex_id]:
            if i not in visited_list[vertex_id]:
                visited_list[vertex_id].append(i)
                edges_done += 1
                path.append(i)
                vertex_id = i
                break
for i in range(edges_done):
    print(id_data[path[i]], end='->')
print(id_data[path[0]])
