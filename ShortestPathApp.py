from cmu_112_graphics import *
from PIL import Image
from tkinter import *
from campus_map import *
import shortestPath as sp

class ShortestPathApp(App):
    def appStarted(app):
        app.scrollX = 200
        app.scrollY = 300
        app.scaleFactor = 1.5 # Modify this to change the default scaling
        app.getBackground()

        ######################### Defaults for the nodes
        app.defaultNodeColor = "deep sky blue"
        app.pathColor = "red"
        app.pathWidth = 10
        app.r = 8
        app.map = createGraph()
        app.shortestPath = []
        
        app.timerDelay = 20

        #Test drawings
        app.userInputTuple = (app.map.nodes['doherty'], app.map.nodes['mudge'])
        app.shortestPath = app.getShortestPath(app.userInputTuple)

    def userInput(app):
        str1 = app.getUserInput("Please type in your starting location:")
        str2 = app.getUserInput("Please type in your ending location:")
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
        app.image = app.scaleImage(app.image, app.scaleFactor/4)

        app.bgX = app.image.width * 1/2
        app.bgY = app.image.height * 1/2

    # Changes the scrollx and scrolly
    def scroll(app, dx, dy):
        app.scrollX += dx
        app.scrollY += dy
        if(app.scrollX > app.image.width - 800 or
           app.scrollY > app.image.height - 800 or
           app.scrollX < 0 or 
           app.scrollY < 0):
           
            app.scrollX -= dx
            app.scrollY -= dy

    def keyPressed(app, event):
        if(event.key == 'Left'):
            app.scroll(-50, 0)
        elif(event.key == 'Right'):
            app.scroll(50, 0)
        elif(event.key == 'Up'):
            app.scroll(0, -50)
        elif(event.key == 'Down'):
            app.scroll(0, 50)
        # Prompts imput for testing
        elif(event.key == 't'):
            app.userInputTuple = app.userInput()
            app.shortestPath = app.getShortestPath(app.userInputTuple)
        
    
    ########################################
    # Drawing Functions                    #
    ########################################
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

app = ShortestPathApp(width=800, height=800)
