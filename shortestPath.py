import math
import campus_map

cmuMap = campus_map.createGraph()

def Dijkstra(graph, startNode):
    # returns dictionary of key-value pairs node-distance realtive to starting 
    # node
    queue = []
    dist = dict()
    for node in graph:
        dist[node] = math.inf
        queue.append(node)
    dist[startNode] = 0

    while (queue != []):
        # look at distances to each node remaining in queue
        queueDistances = distanceValues(queue, dist)
        shortestDistance = smallestValue(queueDistances)
        tempIndex = queueDistances.index(shortestDistance)
        node = queue[tempIndex]
        queue.remove(node)
        # update distances based on whether nodes become neighbors and whether 
        # they're still in the queue
        for neighbor in node.getConnections():
            if (neighbor in queue):
                alt = dist[node] + node.getWeight(neighbor)
                if (alt < dist[neighbor]):
                    dist[neighbor] = alt
    return dist

def shortestPath(graph, startNode, endNode):
    # finds shortest path recursively by calling Dijkstra's 
    if (startNode == endNode):
        return []
    else:
        path = []
        currentNode = startNode
        nxtNode = None
        # At each step, check shortest distance to every other node using 
        # Dijkstra's
        distances = Dijkstra(graph, currentNode)
        shortestDistance = distances[endNode]
        for neighbor in currentNode.getConnections():
            # calculate distance to next node and distance to end node from 
            # that neighbor using Dijkstra's
            # Pick the next node based on this calculation
            directDistance = currentNode.getWeight(neighbor)
            neighborDistances = Dijkstra(graph, neighbor)
            if (directDistance + neighborDistances[endNode] == distances[endNode]):
                nxtNode = neighbor
                break
        # append the next node to path, and then call shortestPath on the last 
        # node in the path
        path.append(neighbor)
        return path + shortestPath(graph, path[-1], endNode)

def getShortestPath(graph, startNode, endNode):
    # wrapper function for shortestPath
    startPoint = startNode.name
    path = shortestPath(graph, startNode, endNode)
    for i in range(len(path)):
        path[i] = path[i].name
    return [startPoint] + path

def distanceValues(lst, distances):
    # returns list of distances given a list of nodes
    newLst = []
    for value in lst:
        newLst.append(distances[value])
    return newLst

def smallestValue(lst):
    # returns smallest value in a list
    smallest = math.inf
    for value in lst:
        if (value < smallest):
            smallest = value
    return smallest