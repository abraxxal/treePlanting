import math

graph = [i for i in range(1, 10)]
neighbors = {1: [2, 3, 4], 2: [1, 4, 5], 3: [1, 4, 6], 4: [1, 2, 3, 5, 6, 7], 
             5: [2, 4, 7, 8], 6: [3, 4, 7, 9], 7: [4, 5, 6, 8, 9], 8: [5, 7, 9],
             9: [6, 7, 8]}
lengths = {(1, 2): 3, (1, 3): 5, (1, 4): 7, (2, 4): 1, (2, 5): 7, (3, 4): 3, 
           (3, 6): 2, (4, 5): 2, (4, 6): 3, (4, 7): 1, (5, 7): 2, (5, 8): 1,
           (6, 7): 3, (6, 9): 4, (7, 8): 3, (7, 9): 2, (8, 9): 5}

def Dijkstra(graph, neighbors, start):
    queue = []
    dist = dict()
    for vertex in graph:
        dist[vertex] = math.inf
        queue.append(vertex)
    dist[start] = 0

    while (queue != []):
        queueDistances = distanceValues(queue, dist)
        shortestDistance = smallestValue(queueDistances)
        tempIndex = queueDistances.index(shortestDistance)
        node = queue[tempIndex]
        queue.remove(node)
        for neighbor in neighbors[node]:
            if neighbor in queue:
                alt = dist[node] + length(node, neighbor)
                if (alt < dist[neighbor]):
                    dist[neighbor] = alt
    return dist

def shortestPath(graph, neighbors, start, end):
    if (start == end):
        return []
    else:
        path = []
        node = start
        nxtNode = None
        distances = Dijkstra(graph, neighbors, start)
        shortestDistance = distances[end]
        for neighbor in neighbors[node]:
            directDistance = length(node, neighbor)
            pathDistances = Dijkstra(graph, neighbors, neighbor)
            if (directDistance + pathDistances[end] == distances[end]):
                nxtNode = neighbor
                break
        path.append(neighbor)
        return path + shortestPath(graph, neighbors, path[-1], end)

def getShortestPath(graph, neighbors, start, end):
    return [start] + shortestPath(graph, neighbors, start, end)
    
def distanceValues(lst, distances):
    newLst = []
    for value in lst:
        newLst.append(distances[value])
    return newLst

def smallestValue(lst):
    smallest = math.inf
    for value in lst:
        if (value < smallest):
            smallest = value
    return smallest

def length(u, v):
    if (u < v):
        return lengths[(u, v)]
    else:
        return lengths[(v, u)]


