from cmu_112_graphics import *
from PIL import Image
from tkinter import *

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
        app.pathColor = "red2"
        app.pathWidth = 10
        
        app.setPathKey()
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
            "ecg west": (725, 404)
            }

    #app.nodes
    #node in app.nodes
    #node.x
    #node.y

    ##############################################
    #             Change the keys here           #
    ##############################################
    def setPathKey(app, keys = ["morewood", "etower", "wts", "purnell"]):
        app.pathKeys = keys

    def getBackground(app):
        url = "https://i.imgur.com/Js6Yr8T.png"
        app.image = app.loadImage(url)
        app.image = app.image.resize((866, 800))

        app.bgX = app.width / 2 + 30
        app.bgY = app.width / 2

    def mousePressed(app, event):
        app.scrollLocation = (event.x, event.y)
        
        app.dotList.append(Dot(event.x, event.y))
        app.coordList.append((event.x, event.y))

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
        
        for i in range(len(app.pathKeys) - 1):
            app.drawPath(canvas, app.pathKeys[i], app.pathKeys[i+1])

        app.drawNodes(canvas)
    
    def drawPath(app, canvas, node1, node2):
        x1, y1 = app.locationsDict[node1]
        x2, y2 = app.locationsDict[node2]
        canvas.create_line(x1, y1, x2, y2,
                           fill = app.pathColor,
                           width = app.pathWidth)
    
    def drawNodes(app, canvas):
        for key in app.locationsDict:
            x, y = app.locationsDict[key]
            canvas.create_oval(x - 8, y - 8,
                               x + 8, y + 8,
                               fill = app.pathColor,
                               width = 0)

app = ShortestPathApp(width=800, height=800)
