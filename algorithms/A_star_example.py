# A* Shortest Path Algorithm
# http://en.wikipedia.org/wiki/A*
# FB - 201012256
from heapq import heappush, heappop  # for priority queue
import math
import time
import random


class Node:
    # current position
    xPos = 0
    yPos = 0
    # total distance already travelled to reach the node
    distance = 0
    # priority = distance + remaining distance estimate
    priority = 0  # smaller: higher priority

    def __init__(self, xPos, yPos, distance, priority):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority

    def __lt__(self, other):  # for priority queue
        return self.priority < other.priority

    def updatePriority(self, xDest, yDest):
        self.priority = self.distance + self.estimate(xDest, yDest) * 10  # A*

    # give better priority to going straight instead of diagonally
    def nextdistance(self, i):  # i: direction
        if i % 2 == 0:
            self.distance += 10
        else:
            self.distance += 14

    # Estimation function for the remaining distance to the goal.
    def estimate(self, xDest, yDest):
        xd = xDest - self.xPos
        yd = yDest - self.yPos
        # Euclidian Distance
        d = math.sqrt(xd * xd + yd * yd)
        # Manhattan distance
        # d = abs(xd) + abs(yd)
        # Chebyshev distance
        # d = max(abs(xd), abs(yd))
        return (d)


# A-star algorithm.
# Path returned will be a string of digits of directions.
def pathFind(the_map, directions, dx, dy, xStart, yStart, xFinish, yFinish):
    closed_nodes_map = []  # map of closed (tried-out) nodes
    open_nodes_map = []  # map of open (not-yet-tried) nodes
    dir_map = []  # map of directions
    row = [0] * n
    for i in range(m):  # create 2d arrays
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

    pq = [[], []]  # priority queues of open (not-yet-tried) nodes
    pqi = 0  # priority queue index
    # create the start node and push into list of open nodes
    n0 = Node(xStart, yStart, 0, 0)
    n0.updatePriority(xFinish, yFinish)
    heappush(pq[pqi], n0)
    open_nodes_map[int(yStart)][int(xStart)] = n0.priority  # mark it on the open nodes map

    # A* search
    while len(pq[pqi]) > 0:
        # get the current node w/ the highest priority
        # from the list of open nodes
        n1 = pq[pqi][0]  # top node
        n0 = Node(n1.xPos, n1.yPos, n1.distance, n1.priority)
        x = n0.xPos
        y = n0.yPos
        heappop(pq[pqi])  # remove the node from the open list
        open_nodes_map[int(y)][int(x)] = 0
        # mark it on the closed nodes map
        closed_nodes_map[int(y)][int(x)] = 1

        # quit searching when the goal state is reached
        # if n0.estimate(xFinish, yFinish) == 0:
        if x == xFinish and y == yFinish:
            # generate the path from finish to start
            # by following the directions
            path = ''
            while not (x == xStart and y == yStart):
                j = int(dir_map[y][x])
                c = str((j + directions / 2) % directions)
                path = c + path
                x += dx[j]
                y += dy[j]
            return path

        # generate moves (child nodes) in all possible directions
        for i in range(directions):
            xdx = x + dx[i]
            ydy = y + dy[i]
            if not (xdx < 0 or xdx > n - 1 or ydy < 0 or ydy > m - 1
                    or the_map[int(ydy)][int(xdx)] == 1 or closed_nodes_map[int(ydy)][int(xdx)] == 1):
                # generate a child node
                m0 = Node(xdx, ydy, n0.distance, n0.priority)
                m0.nextdistance(i)
                m0.updatePriority(xFinish, yFinish)
                # if it is not in the open list then add into that
                if open_nodes_map[int(ydy)][int(xdx)] == 0:
                    open_nodes_map[int(ydy)][int(xdx)] = m0.priority
                    heappush(pq[pqi], m0)
                    # mark its parent node direction
                    dir_map[int(ydy)][int(xdx)] = (i + directions / 2) % directions
                elif open_nodes_map[int(ydy)][int(xdx)] > m0.priority:
                    # update the priority info
                    open_nodes_map[ydy][xdx] = m0.priority
                    # update the parent direction info
                    dir_map[ydy][xdx] = (i + directions / 2) % directions
                    # replace the node
                    # by emptying one pq to the other one
                    # except the node to be replaced will be ignored
                    # and the new node will be pushed in instead
                    while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    heappop(pq[pqi])  # remove the wanted node
                    # empty the larger size pq to the smaller one
                    if len(pq[pqi]) > len(pq[1 - pqi]):
                        pqi = 1 - pqi
                    while len(pq[pqi]) > 0:
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    pqi = 1 - pqi
                    heappush(pq[pqi], m0)  # add the better node instead
    return ''  # no route found


# MAIN
directions = 8  # number of possible directions to move on the map
if directions == 4:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
elif directions == 8:
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

# map matrix
n = 30  # horizontal size
m = 30  # vertical size
the_map = []
row = [0] * n
for i in range(m):
    the_map.append(list(row))

# fillout the map matrix with a '+' pattern
for x in range(n // 8, n * 7 // 8):
    the_map[m // 2][x] = 1
for y in range(m // 8, m * 7 // 8):
    the_map[y][n // 2] = 1

# randomly select start and finish locations from a list
sf = []
sf.append((0, 0, n - 1, m - 1))
sf.append((0, m - 1, n - 1, 0))
sf.append((n / 2 - 1, m / 2 - 1, n / 2 + 1, m / 2 + 1))
sf.append((n / 2 - 1, m / 2 + 1, n / 2 + 1, m / 2 - 1))
sf.append((n / 2 - 1, 0, n / 2 + 1, m - 1))
sf.append((n / 2 + 1, m - 1, n / 2 - 1, 0))
sf.append((0, m / 2 - 1, n - 1, m / 2 + 1))
sf.append((n - 1, m / 2 + 1, 0, m / 2 - 1))
(xA, yA, xB, yB) = random.choice(sf)

print('Map Size (X,Y): ', n, m)
print('Start: ', xA, yA)
print('Finish: ', xB, yB)
t = time.time()
route = pathFind(the_map, directions, dx, dy, xA, yA, xB, yB)
print('Time to generate the route (s): ', time.time() - t)
print('Route:')
print(route)

# mark the route on the map
if len(route) > 0:
    x = xA
    y = yA
    the_map[y][x] = 2
    for i in range(len(route)):
        j = int(route[int(i)])
        x += dx[j]
        y += dy[j]
        the_map[y][x] = 3
    the_map[y][x] = 4

# display the map with the route
print('Map:')
for y in range(m):
    for x in range(n):
        xy = the_map[y][x]
        if xy == 0:
            print('.')  # space
        elif xy == 1:
            print('O')  # obstacle
        elif xy == 2:
            print('S')  # start
        elif xy == 3:
            print('R')  # route
        elif xy == 4:
            print('F')  # finish
    print('')
