def splicer(kmers):
    key_value = {}
    value_key = {}
    list_of_splices = set()
    for i in kmers:
        list_of_splices |= set([i[1:], i[:-1]])
    list_of_splices = list(list_of_splices)
    for i in range(len(list_of_splices)):
        key_value[i] = list_of_splices[i]
        value_key[list_of_splices[i]] = i
    return key_value, value_key


def construct_de_bruijn_graph(kmers):
    edges_to_do = 0
    key_value, value_key = splicer(kmers)
    adj_list = [[] for i in range(len(key_value))]
    vertex_balancing = [0 for i in range(len(key_value))]
    for i in kmers:
        starting_vertex = value_key[i[:-1]]
        ending_vertex = value_key[i[1:]]
        vertex_balancing[starting_vertex] -= 1
        vertex_balancing[ending_vertex] += 1
        adj_list[starting_vertex].append(ending_vertex)
        edges_to_do += 1
    starting_balancing_vertex = 0
    ending_balancing_vertex = 0
    for i in range(len(vertex_balancing)):
        if vertex_balancing[i] == 1:
            starting_balancing_vertex = i
        elif vertex_balancing[i] == -1:
            ending_balancing_vertex = i
    adj_list[starting_balancing_vertex].append(ending_balancing_vertex)
    edges_to_do += 1
    return adj_list, key_value, edges_to_do, ending_balancing_vertex


def all_vertex_edges_done(vertex_id, adj_list, visited):
    adj_list[vertex_id].sort()
    visited[vertex_id].sort()
    return (adj_list[vertex_id] == visited[vertex_id])


def able_to_move(vertex_start, vertex_end, adj_list, visited):
    visited_end_count = 0
    adj_list_end_count = 0
    for i in visited[vertex_start]:
        if i == vertex_end:
            visited_end_count += 1
    for i in adj_list[vertex_start]:
        if i == vertex_end:
            adj_list_end_count += 1
    return adj_list_end_count > visited_end_count


def find_eurelian_path(kmers):
    adj_list, key_value, edges_to_do, real_path_begining = \
        construct_de_bruijn_graph(kmers)
    visited_list = []
    for i in range(len(adj_list)):
        visited_list.append([])
    vertex_id = 0
    edges_done = 0
    path = []
    while edges_done != edges_to_do:
        if all_vertex_edges_done(vertex_id, adj_list, visited_list):
            new_start = -1
            for i in range(len(path)):
                if not all_vertex_edges_done(path[i], adj_list, visited_list):
                    new_start = i
                    break
            path = path[new_start+1:] + path[:new_start+1]
            vertex_id = path[len(path)-1]
        else:
            for i in adj_list[vertex_id]:
                if able_to_move(vertex_id, i, adj_list, visited_list):
                    visited_list[vertex_id].append(i)
                    edges_done += 1
                    path.append(i)
                    vertex_id = i
                    break
    for i in range(edges_done):
        if path[i] == real_path_begining:
            path = path[i:] + path[:i]
    real_vertex_path = []
    for i in range(len(path)):
        real_vertex_path.append(key_value[path[i]])
    return real_vertex_path


def reconstruct_string(kmers):
    path_of_reconstruction = find_eurelian_path(kmers)
    reconstructed_string = path_of_reconstruction[0]
    for i in range(1, len(path_of_reconstruction)):
        reconstructed_string += path_of_reconstruction[i][-1]
    return reconstructed_string
