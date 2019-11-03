from cmu_112_graphics import *
from PIL import Image
from tkinter import *

class Node(object):
    # Name is the display name
    # nodes is the connections, dist are the distances
    # to the connections
    def __init__(self, name, nodes=[], dist=[], x=0, y=0):
        self.name = name
        self.nodes = nodes
        self.dist = dist
        self.x = x
        self.y = y

    def addNodes(self, nodes):
        for node in nodes:
            self.nodes.append(node)

    def addDists(self, dists):
        for dist in dists:
            self.dist.append(dist)
    
class GraphCreator(object):

    @staticmethod
    def createGraph():
        morewood = Node("Morewood E Tower", 300, 50)
        gates = Node("Gates Center", 300, 100)
        newellSimon = Node("Newell Simon Hall", 200, 130)
        wean = Node("Wean Hall", 200, 300)
        doherty = Node("Doherty Hall", 300, 300)

        morewood.addNodes([gates])
        morewood.addDists([2])
        gates.addNodes([newellSimon, morewood])
        gates.addDists([1, 2])
        newellSimon.addNodes([gates, wean])
        newellSimon.addDists([1, 1])
        wean.addNodes([newellSimon, doherty])
        wean.addDists([1, 2])
        doherty.addNodes([wean, gates])
        doherty.addDists([2, 4])

        graph = {}
        graph['morewood'] = morewood
        graph['gates'] = gates
        graph['newellSimon'] = newellSimon
        graph['wean'] = wean
        graph['doherty'] = doherty
        
        return graph

'''class drawing
    def draw(list of names)
    find the correctsponding node objects
    draw each object according to x and y'''

class Dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10
        self.color = "red"

class ShortestPathApp(App):
    def appStarted(app):
        #app.graph = GraphCreator.createGraph()
        app.getBackground()
        app.scrollX = 0
        app.scrollY = 0
        app.scrollLocation = (0, 0)
        app.timerDelay = 20
        app.dotList = []
        app.coordList = []
        
        app.locationsDict = {
            "mudge": (439, 61),
            "stever":(444, 134),
            "morewood":(402, 246),
            "etower":(384, 287),
            "tepper": (252, 291),
            "hamburg":(204, 355),
            "nsh": (192, 425),
            "gates": (268, 422),
            "hillman": (285, 377),
            "cyert": (333, 341),
            "wts": (408, 350),
            "purnell": (352, 453),
            "doherty entrance": (334, 553),
            "doherty": (251, 530),
            "wean": (166, 510),
            "scott hall": (116, 499),
            "hamerschlag": (122, 553),
            "west mall": (156, 562),
            "east mall": (320, 605),
            "scaife": (56, 609),
            "schenley": (100, 657),
            "porter": (138, 617),
            "baker": (227, 634),
            "baker entrance": (299, 659),
            "hunt": (346, 657),
            "cfa": (386, 625),
            "fence" : (398, 571),
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

        }

    def getBackground(app):
        url = "https://i.imgur.com/Js6Yr8T.png"
        app.image = app.loadImage(url)
        app.image = app.image.resize((866, 800))

        app.bgX = app.width / 2 + 30
        app.bgY = app.width / 2

    def mousePressed(app, event):
        app.scrollLocation = (event.x, event.y)
        
        #print(event.x, event.y)
        
        app.dotList.append(Dot(event.x, event.y))
        app.coordList.append((event.x, event.y))

    '''def trackDrag(app, event):
        x1, y1 = app.scrollLocation
        x2, y2 = event.x, event.y
        app.scrollX -= (x2 - x1)
        app.scrollY -= (y2 - y1)'''

    #def mouseDragged(app, event):
    #    app.trackDrag(event)
    
    #def mouseReleased(app, event):
    #    app.trackDrag(event)

    def keyPressed(app, event):
        if(event.key == "f" and len(app.dotList) > 0):
            app.dotList.pop()
            app.coordList.pop()
        elif(event.key == "r"):
            print(app.coordList)

    def redrawAll(app, canvas):
        canvas.create_image(app.bgX - app.scrollX,
                            app.bgY - app.scrollY,
                            image = ImageTk.PhotoImage(app.image))

        for dot in app.dotList:
            canvas.create_oval(dot.x - dot.r, dot.y - dot.r,
                            dot.x + dot.r, dot.y + dot.r,
                            fill = dot.color)

        app.drawDict(canvas)

    def drawDict(app, canvas):
        for key in app.locationsDict:
            x, y = app.locationsDict[key]

            if(key == "uc south"):
                color = "blue"
            else:
                color = "green2"
            canvas.create_oval(x - 10, y - 10,
                            x + 10, y + 10,
                            fill = color)

app = ShortestPathApp(width=800, height=800)
