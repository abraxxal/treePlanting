from cmu_112_graphics import *
from PIL import Image
from tkinter import *
from campus_map import *
import shortestPath as sp


class ShortestPathApp(App):
    def appStarted(app):
        app.scrollX = 0
        app.scrollY = 0
        app.scaleFactor = 1  # Modify this to change the default scaling
        app.getBackground()
        app.timerDelay = 20
        app.getBackground()

        # Defaults for the nodes
        app.defaultNodeColor = "deep sky blue"
        app.pathColor = "red"
        app.pathWidth = 10
        app.map = createGraph()
        app.shortestPath = []
        app.r = 8

        # Defaults for the interface
        app.selectingStart = False
        app.selectingEnd = False
        app.start = None
        app.end = None

        # Test drawings
        app.userInputTuple = (app.map.nodes['doherty'], app.map.nodes['mudge'])
        app.shortestPath = app.getShortestPath(app.userInputTuple)

        # mouse hovering
        app.currentNode = None
        app.hovering = False

    ###################################
    #    Calls Jennifer's Function    #
    ###################################
    def getShortestPath(app, inputs):
        nodes = sp.getShortestPath(app.map, inputs[0], inputs[1])
        # for node in nodes:
        #     print(node.name, node.x, node.y)
        return sp.getShortestPath(app.map, inputs[0], inputs[1])

    def getBackground(app):
        url = "https://i.imgur.com/WapEwR6.jpg"
        app.image = app.loadImage(url)
        app.image = app.scaleImage(app.image, app.scaleFactor / 4)

        app.bgX = app.image.width * 1 / 2
        app.bgY = app.image.height * 1 / 2

    # Changes the scrollx and scrolly
    def scroll(app, dx, dy):
        app.scrollX += dx
        app.scrollY += dy
        if (app.scrollX > app.image.width - 800 or
                app.scrollY > app.image.height - 800 or
                app.scrollX < 0 or
                app.scrollY < 0):
            app.scrollX -= dx
            app.scrollY -= dy

    def keyPressed(app, event):
        if (event.key == 'Left'):
            app.scroll(-50, 0)
        elif (event.key == 'Right'):
            app.scroll(50, 0)
        elif (event.key == 'Up'):
            app.scroll(0, -50)
        elif (event.key == 'Down'):
            app.scroll(0, 50)
            # Prompts imput for testing
        elif (event.key == 't'):
            app.userInputTuple = app.userInput()
            app.shortestPath = app.getShortestPath(app.userInputTuple)
    
    def distance(app, x1, y1, x2, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**0.5

########################################
# Drawing Functions                    #
########################################
    
    def drawInfoBox(app, canvas):
        canvas.create_rectangle(app.width//2-200, app.height-75, app.width//2+200, 
                                app.height-25, fill="red3", width=0)
    
    def drawBuildingName(app, canvas):
        canvas.create_text(app.width//2, app.height-50, text=f"{app.currentNode.name.upper()}", 
                           font="Helvetica 20", fill="white")

    def drawBG(app, canvas):
        canvas.create_image(app.bgX - app.scrollX,
                            app.bgY - app.scrollY,
                            image=ImageTk.PhotoImage(app.image))

    def drawPath(app, canvas):
        for i in range(len(app.shortestPath) - 1):
            app.drawSegment(canvas, app.shortestPath[i], app.shortestPath[i + 1])
        for j in range(len(app.shortestPath)):
            app.drawSingleNode(canvas, app.shortestPath[j], app.pathColor)

    def drawSegment(app, canvas, node1, node2):
        x1 = node1.x * app.scaleFactor - app.scrollX
        y1 = node1.y * app.scaleFactor - app.scrollY
        x2 = node2.x * app.scaleFactor - app.scrollX
        y2 = node2.y * app.scaleFactor - app.scrollY
        canvas.create_line(x1, y1, x2, y2,
                           fill=app.pathColor,
                           width=app.pathWidth)

    def drawNodes(app, canvas):
        for key in app.map.nodes:
            app.drawSingleNode(canvas, app.map.nodes[key], app.defaultNodeColor)

    def drawSingleNode(app, canvas, node, color):
        x = node.x * app.scaleFactor - app.scrollX
        y = node.y * app.scaleFactor - app.scrollY
        canvas.create_oval(x - app.r, y - app.r,
                           x + app.r, y + app.r,
                           fill=color,
                           width=0)

    def mousePressed(app, event):
        x, y = event.x, event.y
        if 100 < x < 300 and 45 < y < 75:
            app.selectingStart = True
            app.selectingEnd = False
        elif 100 < x < 300 and 85 < y < 115:
            app.selectingStart = False
            app.selectingEnd = True
        elif 40 < x < 300 and 140 < y < 170:
            if app.start is not None and app.end is not None:
                app.shortestPath = sp.getShortestPath(app.map, app.start, app.end)
                #app.start = None
                #app.end = None
        elif 40 < x < 300 and 180 < y < 210:
            if app.start is not None and app.end is not None:
                app.shortestPath = sp.getShortestPath(app.map, app.start, app.end)
                #app.start = None
                #app.end = None

        for node in app.map.nodes.values():
            targetX = node.x
            targetY = node.y
            if abs(x - targetX) <= app.r and abs(y - targetY) <= app.r:
                if app.selectingStart:
                    app.start = node
                    app.selectingStart = False
                elif app.selectingEnd:
                    app.end = node
                    app.selectingEnd = False
        
    def mouseMoved(app, event):
        for node in app.map.nodes.values():
            if (app.distance(event.x, event.y, 
                node.x*app.scaleFactor-app.scrollX, 
                node.y*app.scaleFactor-app.scrollY) < 20):
                app.currentNode = node
                app.hovering = True
                break
            else:
                app.hovering = False

    def drawRoutingScreen(app, canvas):
        canvas.create_rectangle(20, 20, 320, 215, fill="red3", width = 0)
        canvas.create_text(32, 60, text="From:", font="Helvetica 16 bold", anchor="w", fill = "white")

        canvas.create_rectangle(100, 45, 300, 75, fill="gray27", width = 0)
        startText = "Click to set start!"
        color = "cyan2"
        if app.start is not None:
            startText = app.start.name
            color = "white"
        elif app.selectingStart:
            startText = "Click on a location!"
        canvas.create_text(110, 60, text=startText, font="Helvetica 13", anchor="w", fill=color)

        canvas.create_text(35, 100, text="    To:", font="Helvetica 16 bold", anchor="w", fill="white")
        canvas.create_rectangle(100, 85, 300, 115, fill="gray27", width=0)
        endText = "Click to set destination!"
        color = "cyan2"
        if app.end is not None:
            endText = app.end.name
            color = "white"
        elif app.selectingEnd:
            endText = "Click on a location!"
        canvas.create_text(110, 100, text=endText, font="Helvetica 13", anchor="w", fill=color)

        canvas.create_rectangle(40, 130, 300, 160, fill="cyan4", width=0)
        canvas.create_text(170, 145, text="Route for shortest distance", font="Helvetica 13 bold", fill="white")
        canvas.create_rectangle(40, 170, 300, 200, fill="cyan4", width=0)
        canvas.create_text(170, 185, text="Route for least time outside", font="Helvetica 13 bold", fill="white")

    def redrawAll(app, canvas):
        app.drawBG(canvas)
        app.drawNodes(canvas)
        app.drawPath(canvas)
        app.drawRoutingScreen(canvas)
        if (app.hovering):
            app.drawInfoBox(canvas)
            app.drawBuildingName(canvas)


app = ShortestPathApp(width=800, height=800)