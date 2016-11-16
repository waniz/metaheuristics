from data_structures.indirected_graph import IndirectedGraph


def bfs(graph, start, end):
    if start not in graph.vertexes():
        return None
    visited_nodes, queue = set(), [start]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        elif node not in visited_nodes:
            for adjacent in graph.adjacent_nodes(node):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
            visited_nodes.add(node)
    return visited_nodes


def bfs2(graph_to_search, start, end):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex == end:
            return path
        elif vertex not in visited:
            for current_neighbour in graph_to_search.adjacent_nodes(vertex):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
                if current_neighbour == end:
                    return new_path
            visited.add(vertex)


graph = IndirectedGraph()
graph.add_connection('100', '101')
graph.add_connection('200', '303')
graph.add_connection('101', '300')
graph.add_connection('300', '303')

# print(graph.vertex_degree('100'))
# print(graph.adjacent_nodes('100'))

print('')

# print(bfs(graph=graph, start='a0', end='e4'))
print(bfs2(graph_to_search=graph, start='100', end='200'))

