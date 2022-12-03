def calculate_betweenness(graph, edges):
    """ Calculate the betweenness of each edge """
    for root in graph:
        visited = set()
        _bfs({root: [1, []]}, graph, edges, visited)


def _bfs(curr_level, graph, edge_betweenness, visited):
    """ Perform BFS to calculate the betweenness """
    if not curr_level:
        return {}

    next_level = _find_all_children(curr_level, graph, visited)
    edge_sum = _bfs(next_level, graph, edge_betweenness, visited)
    curr_level_weights = _calculate_weights(curr_level, edge_sum)
    return _calculate_parent_sum(curr_level, curr_level_weights, edge_betweenness)


def _find_all_children(curr_level, graph, visited):
    """ Find all the valid neighbors on the next level """
    next_level = {}
    for curr_node in curr_level:
        visited.add(curr_node)
        num_of_shortest_paths = curr_level[curr_node][0]
        for neighbor in graph[curr_node]:
            # only consider the node when it hasn't been explored
            if neighbor not in visited and neighbor not in curr_level:
                if neighbor not in next_level:
                    next_level[neighbor] = [0, []]
                next_level[neighbor][0] += num_of_shortest_paths
                next_level[neighbor][1].append([curr_node, num_of_shortest_paths])

    return next_level


def _calculate_weights(curr_level, edge_sum):
    """ Calculate the weights for each node """
    curr_level_weights = {n: 1 for n in curr_level}
    for curr_node in edge_sum:
        curr_level_weights[curr_node] += edge_sum[curr_node]
    return curr_level_weights


def _calculate_parent_sum(curr_level, curr_level_weights, edge_betweenness):
    """ Calculate the value of each edge """
    parent_edge_sum = {}
    for curr_node in curr_level_weights:
        for parent, weight in curr_level[curr_node][1]:
            edge_weight = curr_level_weights[curr_node] * weight / curr_level[curr_node][0]
            parent_edge_sum[parent] = parent_edge_sum.get(parent, 0) + edge_weight

            edge = tuple(sorted([curr_node, parent]))
            edge_betweenness[edge] += edge_weight / 2.0

    return parent_edge_sum


def find_communities(graph):
    """ Find different clusters of communities """
    visited = set()
    communities = []
    for node in graph:
        if node not in visited:
            community = _find_community(node, graph, visited)
            communities.append(community)

    return communities


def _find_community(root, graph, visited):
    """ Explore all nodes in the graph using BFS """
    community = [root]
    visited.add(root)
    next_queue = [root]
    while next_queue:
        node = next_queue.pop(0)
        for child in graph[node]:
            if child not in visited:
                next_queue.append(child)
                community.append(child)
                visited.add(child)

    return community


def calculate_modularity(modules, degree_table, edges, num_of_edges):
    """ Calculate modularity of the partitions """
    modularity = 0.0
    for module in modules:
        modularity += calculate_q(module, degree_table, edges, num_of_edges)

    return modularity / (2.0 * num_of_edges)


def calculate_q(module, degree_table, edges, num_of_edges):
    """ Calculate Q value for each module """
    res = 0.0
    for node_1 in module:
        for node_2 in module:
            pair = tuple(sorted([node_1, node_2]))
            a_i_j = 1.0 if pair in edges else 0.0
            res += (a_i_j - ((degree_table[node_1] * degree_table[node_2]) / (2.0 * num_of_edges)))

    return res