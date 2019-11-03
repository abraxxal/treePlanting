from cmu_112_graphics import *
from PIL import Image
from tkinter import *
from campus_map import *
import shortestPath as sp

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
        app.shortestPath = []

    def userInput(app):
        str1 = input("Please type in your starting location:")
        str2 = input("Please type in your ending location:")
        node1 = app.map.nodes[str1]
        node2 = app.map.nodes[str2]
        return (node1, node2)

    ###################################
    #    Calls Jennifer's Function    #
    ###################################
    def getShortestPath(app, inputs):
        print(sp.getShortestPath(app.map, inputs[0], inputs[1]))
        return sp.getShortestPath(app.map, inputs[0], inputs[1])

    def getBackground(app):
        url = "https://i.imgur.com/Js6Yr8T.png"
        app.image = app.loadImage(url)
        app.image = app.image.resize((866, 800))

        app.bgX = app.width / 2 + 30
        app.bgY = app.width / 2

    def keyPressed(app, event):
        if(event.key == "f" and len(app.dotList) > 0):
            app.dotList.pop()
            app.coordList.pop()
        elif(event.key == "r"):
            print(app.coordList)
        elif(event.key == "e"):
            app.userInputTuple = app.userInput()
            app.shortestPath = app.getShortestPath(app.userInputTuple)

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
