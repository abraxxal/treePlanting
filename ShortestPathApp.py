from cmu_112_graphics import *
from PIL import Image
from tkinter import *
from campus_map import *
import shortestPath as sp

class ShortestPathApp(App):
    def appStarted(app):
        app.getBackground()
        app.scrollX = 800
        app.scrollY = 800
        #app.scrollLocation = (0, 0)
        app.scaleFactor = 4.0

        app.timerDelay = 20
        app.defaultNodeColor = "deep sky blue"
        app.pathColor = "red"
        app.pathWidth = 10
        app.map = createGraph()
        app.shortestPath = []
        app.r = 8

        #Test drawings
        app.userInputTuple = (app.map.nodes['doherty'], app.map.nodes['mudge'])
        app.shortestPath = app.getShortestPath(app.userInputTuple)

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
        nodes = sp.getShortestPath(app.map, inputs[0], inputs[1])
        for node in nodes:
            print(node.name, node.x, node.y)
        return sp.getShortestPath(app.map, inputs[0], inputs[1])

    def getBackground(app):
        url = "https://i.imgur.com/WapEwR6.jpg"
        app.image = app.loadImage(url)
        #app.image = app.scaleImage(app.image, 4/4)

        app.bgX = 1600 #app.width / 2
        app.bgY = 1600 #app.width / 2

    def keyPressed(app, event):
        if(event.key == 'Left'):
            app.scrollX -= 50
        elif(event.key == 'Right'):
            app.scrollX += 50
        elif(event.key == 'Up'):
            app.scrollY -= 50
        elif(event.key == 'Down'):
            app.scrollY += 50
        #elif(event.key == 'r'):
        #    app.scaleFactor -= 0.5
        elif(event.key == 't'):
            app.userInputTuple = app.userInput()
            app.shortestPath = app.getShortestPath(app.userInputTuple)

    def drawBG(app, canvas):
        canvas.create_image(app.bgX - app.scrollX,
                            app.bgY - app.scrollY,
                            image = ImageTk.PhotoImage(app.image))

    def drawPath(app, canvas):
        for i in range(len(app.shortestPath) - 1):
            app.drawSegment(canvas, app.shortestPath[i], app.shortestPath[i+1])
        for j in range(len(app.shortestPath)):
            app.drawSingleNode(canvas, app.shortestPath[j], app.pathColor)

    def drawSegment(app, canvas, node1, node2):
        x1 = node1.x * app.scaleFactor - app.scrollX
        y1 = node1.y * app.scaleFactor - app.scrollY
        x2 = node2.x * app.scaleFactor - app.scrollX
        y2 = node2.y * app.scaleFactor - app.scrollY
        canvas.create_line(x1, y1, x2, y2,
                           fill = app.pathColor,
                           width = app.pathWidth)
    
    def drawNodes(app, canvas):
        for key in app.map.nodes:
            app.drawSingleNode(canvas, app.map.nodes[key], app.defaultNodeColor)

    def drawSingleNode(app, canvas, node, color):
            x = node.x * app.scaleFactor - app.scrollX 
            y = node.y * app.scaleFactor - app.scrollY
            canvas.create_oval(x - app.r, y - app.r,
                               x + app.r, y + app.r,
                               fill = color,
                               width = 0)

    def redrawAll(app, canvas):
        app.drawBG(canvas)
        app.drawNodes(canvas)
        app.drawPath(canvas)
        #canvas.create_rectangle(400,400,250,300, fill = "black")

app = ShortestPathApp(width=800, height=800)
