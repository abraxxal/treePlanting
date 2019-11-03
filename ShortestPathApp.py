from cmu_112_graphics import *
from PIL import Image
from tkinter import *
from campus_map import *
import shortestPath as sp


class ShortestPathApp(App):
    def appStarted(app):
        app.scrollX = 200
        app.scrollY = 300
        app.scaleFactor = 2  # Modify this to change the default scaling
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

########################################
# Drawing Functions                    #
########################################

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
                app.start = None
                app.end = None
        elif 40 < x < 300 and 180 < y < 210:
            if app.start is not None and app.end is not None:
                app.shortestPath = sp.getShortestPath(app.map, app.start, app.end)
                app.start = None
                app.end = None

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

    def drawRoutingScreen(app, canvas):
        canvas.create_rectangle(20, 20, 320, 230, fill="SteelBlue1")
        canvas.create_text(32, 60, text="From:", font="Helvetica 16 bold", anchor="w")

        canvas.create_rectangle(100, 45, 300, 75, fill="powder blue")
        startText = "Click to set start!"
        color = "SlateGray3"
        if app.start is not None:
            startText = app.start.name
            color = "SlateGray4"
        elif app.selectingStart:
            startText = "Click on a location!"
        canvas.create_text(110, 60, text=startText, font="Helvetica 13", anchor="w", fill=color)

        canvas.create_text(35, 100, text="    To:", font="Helvetica 16 bold", anchor="w")
        canvas.create_rectangle(100, 85, 300, 115, fill="powder blue")
        endText = "Click to set destination!"
        color = "SlateGray3"
        if app.end is not None:
            endText = app.end.name
            color = "SlateGray4"
        elif app.selectingEnd:
            endText = "Click on a location!"
        canvas.create_text(110, 100, text=endText, font="Helvetica 13", anchor="w", fill=color)

        canvas.create_rectangle(40, 140, 300, 170, fill="LightGoldenrod1")
        canvas.create_text(170, 155, text="Route for shortest distance", font="Helvetica 14 ")
        canvas.create_rectangle(40, 180, 300, 210, fill="LightGoldenrod1")
        canvas.create_text(170, 195, text="Route for least time outside", font="Helvetica 14 ")

    def redrawAll(app, canvas):
        app.drawBG(canvas)
        app.drawNodes(canvas)
        app.drawPath(canvas)
        app.drawRoutingScreen(canvas)


app = ShortestPathApp(width=800, height=800)
