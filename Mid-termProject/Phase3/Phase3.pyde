#Phase3
def setup():
    size(400, 400) #5x canvas modified
    noStroke()

#Turn shape into function:
def drawObject(x, y, s):
    push()#save
    translate(x, y)
    scale(s)

    # Head
    fill(0)
    rect(0, 0, 80, 80)
    # Eyes
    fill(222, 122, 250)
    rect(0, 40, 30, 10)
    rect(50, 40, 30, 10)
    # Pupils
    fill(200, 0, 250)
    rect(10, 40, 10, 10)
    rect(60, 40, 10, 10)

    pop()#restore

#painting
def draw():
    # use drawObject function twice
    drawObject(150, 150, 1.5)
    drawObject(300, 100, 0.75)
