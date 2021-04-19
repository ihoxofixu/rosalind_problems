def splicer(kmers):
    # this function tkes the list of k-mers and then splits them on (k-1)-mers
    # also it creates key_value and value_key databses that will help working
    # with a graph
    key_value = {}
    value_key = {}
    list_of_splices = set()
    for i in kmers:
        list_of_splices |= set([(i[0][:-1], i[1][:-1]), (i[0][1:], i[1][1:])])
    list_of_splices = list(list_of_splices)
    for i in range(len(list_of_splices)):
        key_value[i] = list_of_splices[i]
        value_key[list_of_splices[i]] = i
    return key_value, value_key


def construct_de_bruijn_graph(kmers):
    # this function makes a graph using the databases from previous function
    # it also makes some constants that will be essiential in finding
    # eurelian path
    edges_to_do = 0
    key_value, value_key = splicer(kmers)
    adj_list = [[] for i in range(len(key_value))]
    # vertex_balancing checks whether all the vertexes are balanced
    vertex_balancing = [0 for i in range(len(key_value))]
    for i in kmers:
        starting_vertex = value_key[(i[0][:-1], i[1][:-1])]
        ending_vertex = value_key[(i[0][1:], i[1][1:])]
        vertex_balancing[starting_vertex] -= 1
        vertex_balancing[ending_vertex] += 1
        adj_list[starting_vertex].append(ending_vertex)
        edges_to_do += 1
    # here we look for unbalanced vertexes
    starting_balancing_vertex = -1
    ending_balancing_vertex = -1
    for i in range(len(vertex_balancing)):
        if vertex_balancing[i] == 1:
            starting_balancing_vertex = i
        elif vertex_balancing[i] == -1:
            ending_balancing_vertex = i
    # and here we look whether we have we have to add a path or no
    # based on that we can say if there is an eurelian cycle
    if_cercular = True
    if starting_balancing_vertex != -1 and ending_balancing_vertex != -1:
        adj_list[starting_balancing_vertex].append(ending_balancing_vertex)
        edges_to_do += 1
        if_cercular = False
    return adj_list, key_value, edges_to_do, ending_balancing_vertex,  \
        if_cercular


def all_vertex_edges_done(vertex_id, adj_list, visited):
    # checks whether there is a free edge from a vertex
    adj_list[vertex_id].sort()
    visited[vertex_id].sort()
    return (adj_list[vertex_id] == visited[vertex_id])


def able_to_move(vertex_start, vertex_end, adj_list, visited):
    # checks whether there is a a free edge beteween two vertexes
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
    # this is the main function that takes the variables from
    # construct_de_bruijn_graph and finds the eurelian path in a graph
    adj_list, key_value, edges_to_do, real_path_begining, if_cercular = \
        construct_de_bruijn_graph(kmers)
    visited_list = []
    for i in range(len(adj_list)):
        visited_list.append([])
    vertex_id = 0
    edges_done = 0
    path = []
    while edges_done != edges_to_do:
        if all_vertex_edges_done(vertex_id, adj_list, visited_list):
            # here we find next vertex with free edges
            new_start = -1
            for i in range(len(path)):
                if not all_vertex_edges_done(path[i], adj_list, visited_list):
                    new_start = i
                    break
            path = path[new_start+1:] + path[:new_start+1]
            vertex_id = path[len(path)-1]
        else:
            # here we just visit free edges
            for i in adj_list[vertex_id]:
                if able_to_move(vertex_id, i, adj_list, visited_list):
                    visited_list[vertex_id].append(i)
                    edges_done += 1
                    path.append(i)
                    vertex_id = i
                    break
    # if the graph is nerly-balanced we have to make sure we have the right
    # starting vertex, and if the graph is balanced we have to add the last
    # because there is an edge between path[0] and path[-1] (if the grapth is
    # nerly-balanced than it will be that edge that we have added and there is
    # no real edge actually)
    if if_cercular:
        path.append(path[0])
    else:
        for i in range(edges_done):
            if path[i] == real_path_begining:
                path = path[i:] + path[:i]
    real_vertex_path = []
    for i in range(len(path)):
        real_vertex_path.append(key_value[path[i]])
    return real_vertex_path


def reconstruct_string(k, d, kmers):
    # makes a string out of ordered (k-1)-mers, called real_vertex_path in the
    # find_eurelian_path function
    path_of_reconstruction = find_eurelian_path(kmers)
    # due to the fact that we have now 2 strings i've decided to make 2 of
    # them and then cut one and join them
    reconstructed_string_begining = path_of_reconstruction[0][0]
    reconstructed_string_ending = path_of_reconstruction[0][1]
    for i in range(1, len(path_of_reconstruction)):
        reconstructed_string_begining += path_of_reconstruction[i][0][-1]
        reconstructed_string_ending += path_of_reconstruction[i][1][-1]
    # joining of two strings is here, we are sure that the second string begins
    # after first's k + d symbols
    reconstructed_string = reconstructed_string_begining[:k+d] + \
        reconstructed_string_ending
    return reconstructed_string
