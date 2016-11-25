"""
http://gabrielgambetta.com/path2.html
"""

import random


class IndirectedGraph:

    def __init__(self):
        self.__adjacent = {}
        self.__vertex_count = 0
        self.__edges_count = 0

    def add_connection(self, source, destination):
        if source in self.__adjacent:
            self.__adjacent[source].append(destination)
        else:
            self.__adjacent[source] = [destination]
            self.__vertex_count += 1

        if destination in self.__adjacent:
            self.__adjacent[destination].append(source)
        else:
            self.__adjacent[destination] = [source]
            self.__vertex_count += 1
        self.__edges_count += 1

    def adjacent_nodes(self, source):
        return set(self.__adjacent[source])

    def vertex_count(self):
        return self.__vertex_count

    def edges_count(self):
        return self.__edges_count

    def vertex_degree(self, source):
        if source in self.__adjacent:
            return len(self.__adjacent[source])
        else:
            return None

    def vertexes(self):
        return self.__adjacent.keys()


class AStar:
    open_set = []
    closed_set = []
    visited = []
    start_node = None
    goal_node = None
    data_graph = None
    parent = {}
    cost = {}

    FIXED_COST = 1

    def __init__(self, start, end, data):
        self.open_set = [start]
        self.closed_set = []
        self.visited = []
        self.start_node = start
        self.goal_node = end
        self.data_graph = data
        self.cost[start] = 0

        for node in data.vertexes():
            self.cost[node] = float('inf')

    def search(self):
        while self.open_set:
            node = self.__choose_node()

            if node == self.goal_node:
                return self.__build_path(self.goal_node)[::-1]

            self.open_set.remove(node)
            self.visited.append(node)

            new_open_set = self.data_graph.adjacent_nodes(node)
            for neighbor in new_open_set:
                if neighbor in self.visited:
                    continue
                if self.cost[node] + self.FIXED_COST < self.cost[neighbor]:

                # p1
                if neighbor not in self.open_set:
                    self.parent[neighbor] = node
                    self.open_set.append(neighbor)
        return None

    def __choose_node(self):
        return random.choice(self.open_set)

    def __build_path(self, to_node):
        path = []
        while to_node:
            path.append(to_node)
            if to_node == self.start_node:
                return path
            to_node = self.parent[to_node]

        return path

# main
graph = IndirectedGraph()

graph.add_connection('A', 'B')
graph.add_connection('B', 'C')
graph.add_connection('A', 'F')
graph.add_connection('F', 'K')
graph.add_connection('K', 'L')
graph.add_connection('L', 'Q')
graph.add_connection('Q', 'V')
graph.add_connection('V', 'W')
graph.add_connection('W', 'X')
graph.add_connection('X', 'Y')
graph.add_connection('L', 'M')
graph.add_connection('M', 'N')
graph.add_connection('N', 'O')
graph.add_connection('O', 'T')
graph.add_connection('T', 'Y')
graph.add_connection('O', 'J')
graph.add_connection('J', 'E')

a_star = AStar('A', 'T', graph)
print(a_star.search())

