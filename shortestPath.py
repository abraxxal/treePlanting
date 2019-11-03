import math
import campus_map

cmuMap = campus_map.createGraph()

def Dijkstra(graph, startNode, indoors):
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
                if (indoors):
                    alt = dist[node] + node.getDistanceIndoors(neighbor)
                else:
                    alt = dist[node] + node.getDistance(neighbor)
                if (alt < dist[neighbor]):
                    dist[neighbor] = alt
    return dist

def shortestPath(graph, startNode, endNode, indoors):
    # finds shortest path recursively by calling Dijkstra's 
    if (startNode == endNode):
        return []
    else:
        path = []
        currentNode = startNode
        nxtNode = None
        # At each step, check shortest distance to every other node using 
        # Dijkstra's
        distances = Dijkstra(graph, currentNode, indoors)
        shortestDistance = distances[endNode]
        for neighbor in currentNode.getConnections():
            # calculate distance to next node and distance to end node from 
            # that neighbor using Dijkstra's
            # Pick the next node based on this calculation
            directDistance = currentNode.getDistance(neighbor)
            neighborDistances = Dijkstra(graph, neighbor, indoors)
            if (directDistance + neighborDistances[endNode] == distances[endNode]):
                nxtNode = neighbor
                break
        # append the next node to path, and then call shortestPath on the last 
        # node in the path
        path.append(neighbor)
        return path + shortestPath(graph, path[-1], endNode, indoors)

def getShortestPath(graph, startNode, endNode):
    # wrapper function for shortestPath
    return [startNode] + shortestPath(graph, startNode, endNode, False)

def getShortestPathIndoors(graph, startNode, endNode):
    # wrapper function for shortestPathIndoors
    return [startNode] + shortestPath(graph, startNode, endNode, True)

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