# Nodes of a graph contain a list of adjacent nodes and their weighted distances
class Node(object):
    def __init__(self, name):
        self.name = name
        self.distances = dict()
        self.exposure = dict()
        self.instructions = dict()
        self.x = 0
        self.y = 0

    def addAdjacent(self, adjacentNode, distance, exposure):
        self.distances[adjacentNode] = distance
        self.exposure[adjacentNode] = exposure

    def getConnections(self):
        return self.distances.keys()

    def getDistance(self, other):
        if other in self.distances:
            return self.distances[other]
        print(f"No connection between {self.name} and {other.name}!")
        return None

    # returns distances but weighted by indoors/outdoors
    def getWeatherDistance(self, other):
        if other in self.distances:
            return self.distances[other] * (self.exposure[other] ** 0.5)
        print(f"No connection between {self.name} and {other.name}!")
        return None

    def getInstructions(self, other):
        if other in self.instructions:
            return self.instructions[other]
        else:
            return f"Walk from {self.name} to {other.name}."

    def __eq__(self, other):
        return isinstance(other, Node) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f'Node: {self.name}\n' \
               f'Neighbors: {[node.name for node in self.getConnections()]}\n' \
               f'Weighted Distances: {[self.getWeatherDistance(node) for node in self.getConnections()]}\n'


class Graph(object):
    def __init__(self):
        self.nodes = dict()

    def __iter__(self):
        return iter(self.nodes.values())

    def addNode(self, name):
        self.nodes[name] = Node(name)

    # takes in one node and a list of nodes to connect it to, as well as weights
    def addEdge(self, node1, otherNodes, distances=None, exposure=None):
        if distances is None:
            distances = [1] * len(otherNodes)
        if exposure is None:
            exposure = [1] * len(otherNodes)
        for i, node2 in enumerate(otherNodes):
            self.nodes[node1].addAdjacent(self.nodes[node2], distances[i], exposure[i])
            self.nodes[node2].addAdjacent(self.nodes[node1], distances[i], exposure[i])

    def addCoordinates(self, node, x, y):
        self.nodes[node].x = x
        self.nodes[node].y = y

    def getNode(self, name):
        return self.nodes[name]

    def __repr__(self):
        result = ''
        for node in self.nodes.values():
            result += str(node) + '\n'
        return result


# section of campus north of the The Fence.
def createGraph():
    cmuGraph = Graph()

    # north campus
    cmuGraph.addNode('Mudge House')
    cmuGraph.addNode('Morewood E-Tower')
    cmuGraph.addNode('Morewood Gardens')
    cmuGraph.addNode('Stever House')
    cmuGraph.addNode('Tepper')
    cmuGraph.addNode('Tepper Quadrangle')

    # mid campus
    cmuGraph.addNode('Hamburg Hall')
    cmuGraph.addNode('Cyert Hall')
    cmuGraph.addNode('Hillman Center')
    cmuGraph.addNode('Newell-Simon Center')
    cmuGraph.addNode('Gates Center')
    cmuGraph.addNode('Purnell Center')
    cmuGraph.addNode('AEPi')
    cmuGraph.addNode('Walking to the Sky')
    cmuGraph.addNode('UC East')
    cmuGraph.addNode('UC North')
    cmuGraph.addNode('UC West')
    cmuGraph.addNode('UC South')
    cmuGraph.addNode('UC Center')
    cmuGraph.addNode('UC Southwest')
    cmuGraph.addNode('ECG East')
    cmuGraph.addNode('ECG West')
    cmuGraph.addNode('West Wing')
    cmuGraph.addNode('Resnik Hall')
    cmuGraph.addNode('Margret Morrison North')

    # south campus
    cmuGraph.addNode('wean')
    cmuGraph.addNode('Doherty Hall')
    cmuGraph.addNode('Doherty Hall Entrance')
    cmuGraph.addNode('Scott Hall')
    cmuGraph.addNode('Hamerschlag Hall')
    cmuGraph.addNode('Porter Hall')
    cmuGraph.addNode('Scaife Hall')
    cmuGraph.addNode('Baker Hall')
    cmuGraph.addNode('Baker Hall Entrance')
    cmuGraph.addNode('Hunt Library')
    cmuGraph.addNode('CFA Building')
    cmuGraph.addNode('The Fence')
    cmuGraph.addNode('Donner House')
    cmuGraph.addNode('Margret Morrison South')
    cmuGraph.addNode('Schenley Park')
    cmuGraph.addNode('East Mall')
    cmuGraph.addNode('West Mall')
    cmuGraph.addNode('SCS Quad Entrance')

    # hilly hilly
    cmuGraph.addNode('Scobell, Happiest Place on Earth')

    # connect north campus
    cmuGraph.addEdge('Mudge House', ['Stever House'], [28], [10])
    cmuGraph.addEdge('Stever House', ['Morewood Gardens'], [31], [10])
    cmuGraph.addEdge('Morewood Gardens', ['Morewood E-Tower'], [30], [10])
    cmuGraph.addEdge('Tepper', ['Tepper Quadrangle', 'Morewood E-Tower'], [18, 56], [10, 10])
    cmuGraph.addEdge('Morewood E-Tower', ['AEPi', 'Cyert Hall', 'Walking to the Sky'], [17, 28, 27], [10, 10, 10])
    cmuGraph.addEdge('Tepper Quadrangle', ['Morewood E-Tower', 'SCS Quad Entrance'], [50, 12], [10, 10])
    cmuGraph.addEdge('AEPi', ['Walking to the Sky'], [25], [10])

    # connect SCS Quad + walking to the sky
    cmuGraph.addEdge('SCS Quad Entrance', ['Hamburg Hall', 'Hillman Center', 'Cyert Hall', 'Newell-Simon Center'], [24, 25, 31, 45], [10, 6, 5, 10])
    cmuGraph.addEdge('Cyert Hall', ['Walking to the Sky', 'Hillman Center'], [29, 22], [10, 5])
    cmuGraph.addEdge('Walking to the Sky', ['Purnell Center', 'UC West', 'UC North'], [43, 26, 30], [10, 10, 10])
    cmuGraph.addEdge('Hillman Center', ['Gates Center'], [19], [2])
    cmuGraph.addEdge('Gates Center', ['Newell-Simon Center', 'Purnell Center'], [29, 33], [3, 10])
    cmuGraph.addEdge('Newell-Simon Center', ['wean'], [33], [1])
    cmuGraph.addEdge('Purnell Center', ['Doherty Hall Entrance', 'The Fence', 'UC Southwest'], [39, 49, 31], [10, 10, 10])

    # connect everything east of the UC
    cmuGraph.addEdge('UC Southwest', ['UC South', 'Doherty Hall Entrance', 'The Fence'], [9, 43, 32], [2, 10, 10])
    cmuGraph.addEdge('UC Center', ['UC West', 'UC East', 'UC South', 'UC North'], [8, 23, 24, 31], [1, 1, 1, 1])
    cmuGraph.addEdge('UC North', ['ECG West', 'UC West'], [26, 25], [1, 1])
    cmuGraph.addEdge('UC West', ['UC Southwest'], [35], [10])
    cmuGraph.addEdge('ECG West', ['ECG East', 'UC East'], [61, 39], [1, 8])
    cmuGraph.addEdge('ECG East', ['Resnik Hall'], [59], [10])
    cmuGraph.addEdge('UC East', ['Margret Morrison North'], [21], [1])
    cmuGraph.addEdge('UC South', ['Margret Morrison North'], [29], [10])
    cmuGraph.addEdge('West Wing', ['Resnik Hall'], [31], [3])
    cmuGraph.addEdge('Resnik Hall', ['Donner House', 'Scobell, Happiest Place on Earth'], [22, 30], [10, 10])
    cmuGraph.addEdge('Donner House', ['Scobell, Happiest Place on Earth', 'Margret Morrison South'], [19, 43], [10, 10])
    cmuGraph.addEdge('Scobell, Happiest Place on Earth', ['Margret Morrison South'], [27], [10])
    cmuGraph.addEdge('Margret Morrison North', ['Margret Morrison South', 'West Wing'], [57, 12], [1, 10])
    cmuGraph.addEdge('The Fence', ['Margret Morrison South', 'CFA Building'], [47, 24], [10, 10])

    # connect the mall
    cmuGraph.addEdge('wean', ['Scott Hall', 'Doherty Hall', 'West Mall'], [25, 33, 20], [3, 2, 6])
    cmuGraph.addEdge('Doherty Hall', ['Doherty Hall Entrance', 'Baker Hall'], [34, 40], [2, 10])
    cmuGraph.addEdge('Doherty Hall Entrance', ['East Mall', 'Baker Hall'], [20, 51], [10, 10])
    cmuGraph.addEdge('Hamerschlag Hall', ['Scott Hall', 'West Mall'], [20, 26], [2, 8])
    cmuGraph.addEdge('West Mall', ['Porter Hall', 'East Mall'], [22, 64], [10, 10])
    cmuGraph.addEdge('East Mall', ['Baker Hall Entrance'], [22], [10])
    cmuGraph.addEdge('Scaife Hall', ['Schenley Park', 'Hamerschlag Hall'], [25, 24], [10, 2])
    cmuGraph.addEdge('Porter Hall', ['Schenley Park', 'Baker Hall'], [21, 39], [2, 1])
    cmuGraph.addEdge('Baker Hall', ['Baker Hall Entrance'], [29], [1])
    cmuGraph.addEdge('Baker Hall Entrance', ['Hunt Library'], [18], [10])
    cmuGraph.addEdge('Hunt Library', ['CFA Building'], [19], [10])

    # add canvas coordinates for all nodes
    locationsDict = {
        "Mudge House": (439, 61),
        "Stever House": (444, 134),
        "Morewood Gardens": (420, 216),
        "Morewood E-Tower": (384, 287),
        "Tepper": (240, 245),
        "Tepper Quadrangle": (252, 291),
        "SCS Quad Entrance": (254, 320),
        "Hamburg Hall": (190, 325),
        "Newell-Simon Center": (192, 425),
        "Gates Center": (268, 422),
        "Hillman Center": (285, 377),
        "Cyert Hall": (333, 341),
        "Walking to the Sky": (408, 350),
        "Purnell Center": (352, 453),
        "Doherty Hall Entrance": (334, 553),
        "Doherty Hall": (251, 530),
        "wean": (166, 510),
        "Scott Hall": (100, 499),
        "Hamerschlag Hall": (90, 553),
        "West Mall": (156, 562),
        "East Mall": (320, 605),
        "Scaife Hall": (56, 609),
        "Schenley Park": (100, 657),
        "Porter Hall": (138, 617),
        "Baker Hall": (227, 634),
        "Baker Hall Entrance": (299, 659),
        "Hunt Library": (346, 657),
        "CFA Building": (386, 625),
        "The Fence": (398, 571),
        "Donner House": (627, 598),
        "Scobell, Happiest Place on Earth": (676, 615),
        "Resnik Hall": (647, 541),
        "West Wing": (568, 520),
        "UC South": (450, 492),
        "UC West": (447, 402),
        "UC East": (525, 453),
        "UC North": (490, 351),
        "UC Center": (470, 430),
        "UC Southwest": (425, 490),
        "AEPi": (427, 288),
        "ECG West": (560, 354),
        "ECG East": (725, 404),
        "Margret Morrison North": (524, 511),
        "Margret Morrison South": (516, 611)
    }
    for key, value in locationsDict.items():
        cmuGraph.addCoordinates(key, value[0], value[1])

    return cmuGraph

def testGraph():
    map = createGraph()
    print(map)

