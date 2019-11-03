# Nodes of a graph contain a list of adjacent nodes and their weighted distances
class Node(object):
    def __init__(self, name):
        self.name = name
        self.distances = dict()
        self.instructions = dict()
        self.x = 0
        self.y = 0

    def addAdjacent(self, adjacentNode, distance):
        self.distances[adjacentNode] = distance

    def getConnections(self):
        return self.distances.keys()

    def getWeight(self, other):
        if other in self.distances:
            return self.distances[other]
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
        return f'Node: {self.name}\nNeighbors: {[x.name for x in self.getConnections()]}\n'


class Graph(object):
    def __init__(self):
        self.nodes = dict()

    def __iter__(self):
        return iter(self.nodes.values())

    def addNode(self, name):
        self.nodes[name] = Node(name)

    # takes in one node and a list of nodes to connect it to, as well as weights
    def addEdge(self, node1, otherNodes, distances=None):
        if distances is None:
            distances = [1] * len(otherNodes)
        for i, node2 in enumerate(otherNodes):
            self.nodes[node1].addAdjacent(self.nodes[node2], distances[i])
            self.nodes[node2].addAdjacent(self.nodes[node1], distances[i])

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

    # hilly hilly
    cmuGraph.addNode('scobell')

    # connect north campus
    cmuGraph.addEdge('mudge', ['stever'], [15])
    cmuGraph.addEdge('stever', ['morewood'], [17])
    cmuGraph.addEdge('morewood', ['etower'], [18])
    cmuGraph.addEdge('etower', ['tepper', 'aepi', 'cyert', 'wts'], [29, 9, 15, 12])
    cmuGraph.addEdge('tepper', ['hamburg', 'hillman'], [14, 20])
    cmuGraph.addEdge('aepi', ['wts'], [14])

    # connect scs quad + walking to the sky
    # cmuGraph.addEdge('hamburg', ['nsh'], [18])
    cmuGraph.addEdge('cyert', ['wts', 'hillman'], [17, 15])
    cmuGraph.addEdge('wts', ['purnell', 'uc east', 'uc north'], [25, 13, 18])
    cmuGraph.addEdge('hillman', ['gates'], [12])
    cmuGraph.addEdge('gates', ['nsh', 'purnell'], [14, 20])
    cmuGraph.addEdge('nsh', ['wean'], )
    cmuGraph.addEdge('purnell', ['doherty entrance', 'fence', 'uc south'])

    # connect everything east of the UC
    cmuGraph.addEdge('uc north', ['uc east', 'ecg east'])
    cmuGraph.addEdge('ecg east', ['ecg west', 'uc west', 'uc east'])
    cmuGraph.addEdge('ecg west', ['resnik'])
    cmuGraph.addEdge('uc east', ['uc south', 'uc west'])
    cmuGraph.addEdge('uc west', ['uc south'])
    cmuGraph.addEdge('uc south', ['doherty entrance', 'fence', 'maggie mo north'])
    cmuGraph.addEdge('west wing', ['resnik'])
    cmuGraph.addEdge('resnik', ['donner', 'scobell', 'ecg west'])
    cmuGraph.addEdge('donner', ['scobell', 'maggie mo south'])  # ***** new connection *****
    cmuGraph.addEdge('scobell', ['maggie mo south'])
    cmuGraph.addEdge('maggie mo north', ['maggie mo south', 'west wing'])
    cmuGraph.addEdge('fence', ['maggie mo south', 'cfa'])

    # connect the mall
    cmuGraph.addEdge('wean', ['scott', 'doherty', 'west mall'])
    cmuGraph.addEdge('doherty', ['doherty entrance', 'baker'])
    cmuGraph.addEdge('doherty entrance', ['baker entrance', 'baker'])
    cmuGraph.addEdge('hamerschlag hall', ['scott', 'west mall'])
    cmuGraph.addEdge('west mall', ['porter', 'east mall'])
    cmuGraph.addEdge('east mall', ['baker entrance'])
    cmuGraph.addEdge('scaife', ['schenley', 'hamerschlag hall'])
    cmuGraph.addEdge('porter', ['schenley', 'baker'])
    cmuGraph.addEdge('baker', ['baker entrance'])
    cmuGraph.addEdge('baker entrance', ['hunt'])
    cmuGraph.addEdge('hunt', ['cfa'])

    # add canvas coordinates for all nodes
    locationsDict = {
        "mudge": (439, 61),
        "stever": (444, 134),
        "morewood": (402, 246),
        "etower": (384, 287),
        "tepper": (252, 291),
        "hamburg": (204, 355),
        "nsh": (192, 425),
        "gates": (268, 422),
        "hillman": (285, 377),
        "cyert": (333, 341),
        "wts": (408, 350),
        "purnell": (352, 453),
        "doherty entrance": (334, 553),
        "doherty": (251, 530),
        "wean": (166, 510),
        "scott": (116, 499),
        "hamerschlag hall": (122, 553),
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
        "uc south": (447, 492),
        "uc west": (447, 402),
        "uc east": (525, 453),
        "uc north": (472, 351),
        "aepi": (427, 288),
        "ecg east": (547, 354),
        "ecg west": (725, 404),
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