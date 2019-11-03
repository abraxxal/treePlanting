def distance(app, x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def mouseMoved(app, event):
    for node in app.map:
        if app.distance(event.x, event.y, node.x, node.y) < app.r:
            app.drawInfoBox(app, canvas, node)
            app.drawBuildingName(app, canvas, node)
            app.drawBuildingImage(app, canvas, node)

def drawInfoBox(app, canvas, node):
    (x, y) = legalQuadrant(app, canvas, node)
    if ((x, y) == (-, -)):
        canvas.create_rectangle(node.x-150, node.y-100, node.x, node.y,
                                fill="white", width=0)
    elif ((x, y) == (+, -)):
        canvas.create_rectangle(node.x, node.y-100, node.x+150, node.y,
                                fill="white", width=0)
    elif ((x, y) == (-, +)):
        canvas.create_rectangle(node.x-150, node.y, node.x, node.y+150,
                                fill="white", width=0)
    elif ((x, y) == (+, +)):
        canvas.create_rectangle(node.x, node.y, node.x+150, node.y+100,
                                fill="white", width=0)

def drawBuildingName(app, canvas, node, nodeX, nodeY):
    (x, y) = legalQuadrant(app, canvas, node)
    font = "Helvetica 12"
    if ((x, y) == (-, -)):
        canvas.create_text(node.x-75, node.y-80, text=f"{node.name}",
                           fill="black", font=font)
    elif((x, y) == (+, -)):
        canvas.create_text(node.x+75, node.y-80, text=f"{node.name}",
                           fill="black", font=font)
    elif ((x, y) == (-, +)):
        canvas.create_text(node.x-75, node.y+20, text=f"{node.name}",
                           fill="black", font=font)
    elif ((x, y) == (+, +)):
        canvas.create_text(node.x+75, node.y+20, text=f"{node.name}",
                           fill="black", font=font)

def legalQuadrant(app, canvas, node):
    if ((node.x+150) > app.width):
        if ((node.y+100) > app.height):
            return (-, -)
        elif ((node.y-100) < 0):
            return (-, +)
        else:
            return (-, -)
    elif ((node.x-150) < 0):
        if ((node.y+100) > app.height):
            return (+, -)
        elif ((node.y-100) < 0):
            return (+, +)
        else:
            return (+, -)
    else:
        if ((node.y+100) > app.height):
            return (+, -)
        elif ((node.y-100) < 0):
            return (+, +)
        else:
            return (+, -)

