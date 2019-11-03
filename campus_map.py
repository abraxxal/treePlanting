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


# section of campus north of the Fence.
def createGraph():
    cmuGraph = Graph()

    # north campus
    cmuGraph.addNode('mudge')
    cmuGraph.addNode('etower')
    cmuGraph.addNode('morewood')
    cmuGraph.addNode('stever')
    cmuGraph.addNode('tepper')
    cmuGraph.addNode('tepper quad')

    # mid campus
    cmuGraph.addNode('hamburg')
    cmuGraph.addNode('cyert')
    cmuGraph.addNode('hillman')
    cmuGraph.addNode('nsh')
    cmuGraph.addNode('gates')
    cmuGraph.addNode('purnell')
    cmuGraph.addNode('aepi')
    cmuGraph.addNode('wts')
    cmuGraph.addNode('uc east')
    cmuGraph.addNode('uc north')
    cmuGraph.addNode('uc west')
    cmuGraph.addNode('uc south')
    cmuGraph.addNode('uc center')
    cmuGraph.addNode('uc sw')
    cmuGraph.addNode('ecg east')
    cmuGraph.addNode('ecg west')
    cmuGraph.addNode('west wing')
    cmuGraph.addNode('resnik')
    cmuGraph.addNode('maggie mo north')

    # south campus
    cmuGraph.addNode('wean')
    cmuGraph.addNode('doherty')
    cmuGraph.addNode('doherty entrance')
    cmuGraph.addNode('scott')
    cmuGraph.addNode('hamerschlag hall')
    cmuGraph.addNode('porter')
    cmuGraph.addNode('scaife')
    cmuGraph.addNode('baker')
    cmuGraph.addNode('baker entrance')
    cmuGraph.addNode('hunt')
    cmuGraph.addNode('cfa')
    cmuGraph.addNode('fence')
    cmuGraph.addNode('donner')
    cmuGraph.addNode('maggie mo south')
    cmuGraph.addNode('schenley')
    cmuGraph.addNode('east mall')
    cmuGraph.addNode('west mall')
    cmuGraph.addNode('scs quad entrance')

    # hilly hilly
    cmuGraph.addNode('scobell')

    # connect north campus
    cmuGraph.addEdge('mudge', ['stever'], [15], [10])
    cmuGraph.addEdge('stever', ['morewood'], [17], [10])
    cmuGraph.addEdge('morewood', ['etower'], [18], [10])
    cmuGraph.addEdge('tepper', ['tepper quad', 'etower'], [4, 28], [10, 10])
    cmuGraph.addEdge('etower', ['tepper', 'aepi', 'cyert', 'wts'], [29, 9, 15, 12], [10, 10, 10, 10])
    cmuGraph.addEdge('tepper quad', ['scs quad entrance'], [5], [10])
    cmuGraph.addEdge('aepi', ['wts'], [14], [10])

    # connect scs quad + walking to the sky
    cmuGraph.addEdge('scs quad entrance', ['hamburg', 'hillman', 'cyert'], [8, 6, 8], [10, 10, 10])
    cmuGraph.addEdge('cyert', ['wts', 'hillman'], [17, 15], [10, 5])
    cmuGraph.addEdge('wts', ['purnell', 'uc west', 'uc north'], [25, 10, 18], [10, 10, 10])
    cmuGraph.addEdge('hillman', ['gates'], [12], [2])
    cmuGraph.addEdge('gates', ['nsh', 'purnell'], [14, 20], [3, 10])
    cmuGraph.addEdge('nsh', ['wean'], [16], [1])
    cmuGraph.addEdge('purnell', ['doherty entrance', 'fence'], [22, 29], [10, 10])

    # connect everything east of the UC
    cmuGraph.addEdge('uc sw', ['uc south', 'doherty entrance', 'purnell', 'fence'], [2, 27, 20, 22])
    cmuGraph.addEdge('uc center', ['uc west', 'uc east', 'uc south'], [4, 9, 4], [1, 1, 1])
    cmuGraph.addEdge('uc north', ['ecg west', 'uc west'], [14, 6], [1, 1])
    cmuGraph.addEdge('uc west', ['uc sw'], [7], [10])
    cmuGraph.addEdge('ecg west', ['ecg east', 'uc east'], [31, 20], [1, 8])
    cmuGraph.addEdge('ecg east', ['resnik'], [30], [10])
    # cmuGraph.addEdge('uc west', ['uc south', 'uc east'], [17, 19], [1, 1])
    cmuGraph.addEdge('uc east', ['maggie mo north'], [15], [1, 1])
    cmuGraph.addEdge('uc south', ['uc sw', 'maggie mo north'], [4, 22], [10, 10])
    cmuGraph.addEdge('west wing', ['resnik'], [14], [3])
    cmuGraph.addEdge('resnik', ['donner', 'scobell', 'ecg east'], [12, 25, 30], [10, 10, 10])
    cmuGraph.addEdge('donner', ['scobell', 'maggie mo south'], [15, 27], [10, 10])
    cmuGraph.addEdge('scobell', ['maggie mo south'], [27], [10])
    cmuGraph.addEdge('maggie mo north', ['maggie mo south', 'west wing'], [22, 10], [1, 10])
    cmuGraph.addEdge('fence', ['maggie mo south', 'cfa'], [23, 16], [10, 10])

    # connect the mall
    cmuGraph.addEdge('wean', ['scott', 'doherty', 'west mall'], [8, 18, 10], [3, 2, 6])
    cmuGraph.addEdge('doherty', ['doherty entrance', 'baker'], [19, 23], [3, 10])
    cmuGraph.addEdge('doherty entrance', ['east mall', 'baker'], [12, 30], [10, 10])
    cmuGraph.addEdge('hamerschlag hall', ['scott', 'west mall'], [10, 10], [2, 8])
    cmuGraph.addEdge('west mall', ['porter', 'east mall'], [11, 36], [10, 10])
    cmuGraph.addEdge('east mall', ['baker entrance'], [10], [10])
    cmuGraph.addEdge('scaife', ['schenley', 'hamerschlag hall'], [18, 13], [10, 2])
    cmuGraph.addEdge('porter', ['schenley', 'baker'], [10, 19], [2, 1])
    cmuGraph.addEdge('baker', ['baker entrance'], [18], [1])
    cmuGraph.addEdge('baker entrance', ['hunt'], [8], [10])
    cmuGraph.addEdge('hunt', ['cfa'], [11], [10])

    # add canvas coordinates for all nodes
    locationsDict = {
        "mudge": (439, 61),
        "stever": (444, 134),
        "morewood": (420, 216),
        "etower": (384, 287),
        "tepper": (240, 245),
        "tepper quad": (252, 291),
        "scs quad entrance": (254, 320),
        "hamburg": (190, 325),
        "nsh": (192, 425),
        "gates": (268, 422),
        "hillman": (285, 377),
        "cyert": (333, 341),
        "wts": (408, 350),
        "purnell": (352, 453),
        "doherty entrance": (334, 553),
        "doherty": (251, 530),
        "wean": (166, 510),
        "scott": (100, 499),
        "hamerschlag hall": (90, 553),
        "west mall": (156, 562),
        "east mall": (320, 605),
        "scaife": (56, 609),
        "schenley": (100, 657),
        "porter": (138, 617),
        "baker": (227, 634),
        "baker entrance": (299, 659),
        "hunt": (346, 657),
        "cfa": (386, 625),
        "fence": (398, 571),
        "donner": (627, 598),
        "scobell": (676, 615),
        "resnik": (647, 541),
        "west wing": (568, 520),
        "uc south": (450, 492),
        "uc west": (447, 402),
        "uc east": (525, 453),
        "uc north": (490, 351),
        "uc center": (470, 430),
        "uc sw": (425, 490),
        "aepi": (427, 288),
        "ecg west": (560, 354),
        "ecg east": (725, 404),
        "maggie mo north": (524, 511),
        "maggie mo south": (516, 611)
    }
    for key, value in locationsDict.items():
        cmuGraph.addCoordinates(key, value[0], value[1])

    return cmuGraph

def testGraph():
    map = createGraph()
    print(map)

testGraph()
