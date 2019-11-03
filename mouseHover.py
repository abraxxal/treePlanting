def distance(app, x1, y1, x2, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**0.5

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

    def drawInfoBox(app, canvas):
        canvas.create_rectangle(app.width-150, 0, app.width, 100, fill="white")
    
    def drawBuildingName(app, canvas):
        canvas.create_text(app.width-75, 15, text=f"{app.currentNode.name}", 
                           fill="black")