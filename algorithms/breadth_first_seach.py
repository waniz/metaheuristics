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


graph = IndirectedGraph()
graph.add_connection('1', '3')
graph.add_connection('1', '2')
graph.add_connection('1', '4')
graph.add_connection('2', '5')
graph.add_connection('2', '6')
graph.add_connection('5', '9')
graph.add_connection('5', '10')
graph.add_connection('4', '7')
graph.add_connection('4', '8')
graph.add_connection('7', '11')
graph.add_connection('7', '12')
print(bfs(graph=graph, start='1', end='11'))
