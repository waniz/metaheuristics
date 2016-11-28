"""
http://gabrielgambetta.com/path2.html
"""

import math
import matplotlib.pyplot as plt
import time

plt.style.use('ggplot')


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
        self.open_set = [start]          # reachable
        self.closed_set = []
        self.visited = []                # explored
        self.start_node = start
        self.goal_node = end
        self.data_graph = data

        for node in data.vertexes():
            self.cost[node] = float('inf')
        self.cost[start] = 0

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
                    self.parent[neighbor] = node
                    self.cost[neighbor] = self.cost[node] + self.FIXED_COST
                if neighbor not in self.open_set:
                    self.open_set.append(neighbor)
        return None

    def __choose_node(self):
        min_cost = float('inf')
        best_node = None
        for node in self.open_set:
            cost_start_to_node = self.cost[node]
            cost_node_to_goal = self.__estimate_distance(node)
            total_cost = cost_start_to_node + cost_node_to_goal

            if min_cost > total_cost:
                min_cost = total_cost
                best_node = node
        return best_node

    def __estimate_distance(self, node, distance_method='manhattan'):
        node_y, node_x = node.split('_')
        goal_y, goal_x = self.goal_node.split('_')
        node_x, node_y, goal_x, goal_y = int(node_x), int(node_y), int(goal_x), int(goal_y)

        distance = float('inf')
        if distance_method == 'manhattan':
            distance = abs(node_x - goal_x) + abs(node_y - goal_y)
        elif distance_method == 'sqrt':
            distance = math.sqrt((node_x - goal_x) ** 2 + (node_y - goal_y) ** 2)
        return distance

    def __build_path(self, to_node):
        path = []
        while to_node:
            path.append(to_node)
            if to_node == self.start_node:
                return path
            to_node = self.parent[to_node]
        return path


# main
def obstacle_in_node(node):
    obstacles = [[10, 10], [15, 15], [20, 20], [20, 25]]
    if node in obstacles:
        return True
    return False


map_size = 400
step = 1

start_graph = time.time()
graph = IndirectedGraph()
for y_line in range(0, map_size, step):
    for x_line in range(0, map_size - step, step):
        if not obstacle_in_node([y_line, x_line + step]):
            node_1 = '%s_%s' % ((y_line + step // 2), x_line + step // 2)
            node_2 = '%s_%s' % ((y_line + step // 2), x_line + step // 2 + step)
            graph.add_connection(node_1, node_2)

print('   1L: %s' % round((time.time() - start_graph), 5))

for y_line in range(0, map_size - step, step):
    for x_line in range(0, map_size, step):
        if not obstacle_in_node([y_line + step, x_line]):
            node_1 = '%s_%s' % ((y_line + step // 2), x_line + step // 2)
            node_2 = '%s_%s' % ((y_line + step // 2 + step), x_line + step // 2 + step)
            graph.add_connection(node_1, node_2)

print('   2L: %s' % round((time.time() - start_graph), 5))

for y_line in range(0, map_size - step, step):
    for x_line in range(0, map_size - step, step):
        if not obstacle_in_node([y_line + step, x_line + step]):
            node_1 = '%s_%s' % ((y_line + step // 2), x_line + step // 2)
            node_2 = '%s_%s' % ((y_line + step // 2 + step), x_line + step // 2 + step)
            graph.add_connection(node_1, node_2)

print('   3L: %s' % round((time.time() - start_graph), 5))

for y_line in range(0, map_size - step, step):
    for x_line in range(step, map_size, step):
        if not obstacle_in_node([y_line - step, x_line - step]):
            node_1 = '%s_%s' % ((y_line + step // 2), x_line + step // 2)
            node_2 = '%s_%s' % ((y_line + step // 2 - step), x_line + step // 2 - step)
            graph.add_connection(node_1, node_2)

print('   4L: %s' % round((time.time() - start_graph), 5))

print('Graph: %s' % round((time.time() - start_graph), 5))

start_a = time.time()
a_star = AStar('5_5', '55_75', graph)
path = a_star.search()

print('A*   : %s' % round((time.time() - start_a), 5))
print(path)


