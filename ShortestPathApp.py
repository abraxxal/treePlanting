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
        app.hovering = False
        app.currentNode = None

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
    
    def distance(app, x1, y1, x2, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**0.5

    def mouseMoved(app, event):
        '''
        print(event.x, event.y)
        for node in app.map.nodes.values():
            x = node.x * app.scaleFactor - app.scrollX 
            y = node.y * app.scaleFactor - app.scrollY
            if app.distance(event.x, event.y, x, y) < 2*app.r:
                app.currentNode = node
                app.hovering = True
            else:
                app.hovering = False
        '''
        '''
        node = app.map.getNode("aepi")
        x = node.x * app.scaleFactor - app.scrollX
        y = node.y * app.scaleFactor - app.scrollY
        if app.distance(event.x, event.y, x, y) < app.r:
            app.currentNode = node
            app.hovering = True
        else:
            app.hovering = False
        '''
        for node in app.map.nodes.values():
            if (app.distance(event.x, event.y, 
                node.x*app.scaleFactor-app.scrollX, 
                node.y*app.scaleFactor-app.scrollY) < 20):
                print("akljdhfs")
                app.currentNode = node
                app.hovering = True
                break
            else:
                app.hovering = False
                print(":(")

    def drawInfoBox(app, canvas):
        canvas.create_rectangle(app.width-150, 0, app.width, 100, fill="white")
    
    def drawBuildingName(app, canvas):
        canvas.create_text(app.width-75, 15, text=f"{app.currentNode.name}", 
                           fill="black")
    

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
        app.drawInfoBox(canvas)
        if (app.hovering):
            print("REEEEE")
            app.drawBuildingName(canvas)
        #canvas.create_rectangle(400,400,250,300, fill = "black")

app = ShortestPathApp(width=800, height=800)
