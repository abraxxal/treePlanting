
# Nodes of a graph contain a list of adjacent nodes and their weighted distances
class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacent = dict()

    def addAdjacent(self, adjacentNode, distance):
        self.adjacent[adjacentNode] = distance

    def getConnections(self):
        return self.adjacent.keys()

    def getWeight(self, other):
        if other in self.adjacent:
            return self.adjacent[other]
        return None

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
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
    cmuGraph.addEdge('mudge', ['stever'])
    cmuGraph.addEdge('stever', ['morewood'])
    cmuGraph.addEdge('morewood', ['etower'])
    cmuGraph.addEdge('etower', ['tepper', 'aepi', 'cyert', 'wts'])
    cmuGraph.addEdge('tepper', ['hamburg', 'hillman'])
    cmuGraph.addEdge('aepi', ['wts'])

    # connect scs quad + walking to the sky
    cmuGraph.addEdge('hamburg', ['nsh'])
    cmuGraph.addEdge('cyert', ['wts', 'hillman'])
    cmuGraph.addEdge('wts', ['purnell', 'uc east', 'uc north'])
    cmuGraph.addEdge('hillman', ['gates'])
    cmuGraph.addEdge('gates', ['nsh', 'purnell'])
    cmuGraph.addEdge('nsh', ['wean'])
    cmuGraph.addEdge('purnell', ['doherty entrance', 'fence', 'uc south'])

    # connect everything east of the UC
    cmuGraph.addEdge('uc north', ['uc east', 'ecg east'])
    cmuGraph.addEdge('ecg east', ['ecg west', 'uc west', 'uc east'])
    cmuGraph.addEdge('ecg west', ['resnik'])
    cmuGraph.addEdge('uc east', ['uc south', 'uc west'])
    cmuGraph.addEdge('uc west', ['uc south'])
    cmuGraph.addEdge('uc south', ['doherty entrance', 'fence', 'maggie mo north'])
    cmuGraph.addEdge('west wing', ['resnik'])
    cmuGraph.addEdge('resnik', ['donner', 'scobell'])
    cmuGraph.addEdge('donner', ['scobell', 'maggie mo south'])  # ***** new connection *****
    cmuGraph.addEdge('scobell', ['maggie mo south'])
    cmuGraph.addEdge('maggie mo north', ['maggie mo south', 'west wing'])

    # connect the mall
    cmuGraph.addEdge('wean', ['scott', 'doherty', 'west mall'])
    cmuGraph.addEdge('doherty', ['doherty entrance', 'baker'])
    cmuGraph.addEdge('doherty entrance', ['baker entrance'])
    cmuGraph.addEdge('hamerschlag hall', ['scott', 'west mall'])
    cmuGraph.addEdge('west mall', ['porter', 'east mall'])
    cmuGraph.addEdge('east mall', ['baker entrance'])
    cmuGraph.addEdge('scaife', ['schenley'])
    cmuGraph.addEdge('porter', ['schenley', 'baker'])
    cmuGraph.addEdge('baker', ['baker entrance'])
    cmuGraph.addEdge('baker entrance', ['hunt'])
    cmuGraph.addEdge('hunt', ['cfa'])

    return cmuGraph

map = createGraph()
print(map)


