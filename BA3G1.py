edges_to_do = 0
id_data = {}
adjacency_list = []
tmp = input()
all_starting_vertexes = set()
while tmp != '':
    start, trash, ends = tmp.split()
    start, ends = int(start), list(map(int, ends.split(',')))
    id_data[len(adjacency_list)] = start
    adjacency_list.append(ends)
    edges_to_do += len(ends)
    all_starting_vertexes |= set([start])
    tmp = input()
for i in range(len(adjacency_list)):
    for j in range(len(adjacency_list[i])):
        if adjacency_list[i][j] not in all_starting_vertexes:
            all_starting_vertexes |= set([adjacency_list[i][j]])
            id_data[len(adjacency_list)] = adjacency_list[i][j]
            adjacency_list.append([])


def adj_list_remake(key_value=id_data, adj_list=adjacency_list,
                    edges_count=edges_to_do):
    value_key = {}
    for i in key_value:
        value_key[key_value[i]] = i
    vertex_balancing = [0 for i in range(len(adj_list))]
    for i in range(len(adj_list)):
        vertex_balancing[i] -= len(adj_list[i])
        for j in range(len(adj_list[i])):
            vertex_balancing[value_key[adj_list[i][j]]] += 1
    new_path_beginig = 0
    new_path_ending = 0
    for i in range(len(vertex_balancing)):
        if vertex_balancing[i] == 1:
            new_path_beginig = i
        elif vertex_balancing[i] == -1:
            new_path_ending = i
    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            adj_list[i][j] = value_key[adj_list[i][j]]
    if new_path_beginig != new_path_ending:
        if new_path_beginig < len(adj_list):
            adj_list[new_path_beginig].append(new_path_ending)
        else:
            adj_list.append([new_path_ending])
        edges_count += 1
    return adj_list, edges_count, new_path_ending


adjacency_list, edges_to_do, real_path_begining = adj_list_remake()
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
    if path[i] == real_path_begining:
        path = path[i:] + path[:i]
for i in range(edges_done):
    print(id_data[path[i]], end='->')
print()
