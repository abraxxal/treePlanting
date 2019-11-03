from cmu_112_graphics import *
from PIL import Image
from tkinter import *
from campus_map import *

class ShortestPathApp(App):
    def appStarted(app):
        app.getBackground()
        #app.scrollX = 0
        #app.scrollY = 0
        #app.scrollLocation = (0, 0) code used once for scrolling
        app.timerDelay = 20
        app.defaultNodeColor = "deep sky blue"
        app.pathColor = "red"
        app.pathWidth = 10
        app.map = createGraph()
        
        #ShortestPath stores a list of node objects
        app.shortestPath = app.getPath()

    ##############################################
    #             Change the keys here           #
    ##############################################
    def getPath(app):
        # This is a sample list of locations
        return [app.map.nodes['scobell'],
                app.map.nodes['resnik'],
                app.map.nodes['west wing'],
                app.map.nodes['uc south'],
                app.map.nodes['doherty entrance'],
                app.map.nodes['doherty'],
                app.map.nodes['wean'],
                app.map.nodes['nsh'],
                app.map.nodes['hamburg'],
                app.map.nodes['tepper'],
                app.map.nodes['hillman'],
                app.map.nodes['gates'],
                app.map.nodes['ecg west'],
                app.map.nodes['aepi'],
                ]
        #app.shortestPathKeys = Jennifer's algorithm(input)

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

    def drawBG(app, canvas):
        canvas.create_image(app.bgX,
                            app.bgY,
                            image = ImageTk.PhotoImage(app.image))

    def drawPath(app, canvas):
        for i in range(len(app.shortestPath) - 1):
            app.drawSegment(canvas, app.shortestPath[i], app.shortestPath[i+1])
        for j in range(len(app.shortestPath)):
            app.drawSingleNode(canvas, app.shortestPath[j], app.pathColor)

    def drawSegment(app, canvas, node1, node2):
        x1, y1 = node1.x, node1.y
        x2, y2 = node2.x, node2.y
        canvas.create_line(x1, y1, x2, y2,
                           fill = app.pathColor,
                           width = app.pathWidth)
    
    def drawNodes(app, canvas):
        for key in app.map.nodes:
            app.drawSingleNode(canvas, app.map.nodes[key], app.defaultNodeColor)

    def drawSingleNode(app, canvas, node, color):
            x = node.x 
            y = node.y
            canvas.create_oval(x - 8, y - 8,
                               x + 8, y + 8,
                               fill = color,
                               width = 0)

    def redrawAll(app, canvas):
        app.drawBG(canvas)
        app.drawNodes(canvas)
        app.drawPath(canvas)

app = ShortestPathApp(width=800, height=800)
