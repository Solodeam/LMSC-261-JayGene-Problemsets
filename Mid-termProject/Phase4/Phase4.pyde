#Phase4
def setup():
    size(400, 400)
    noStroke()

#Turn shape into function:
def drawObject(x, y, s,):
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
    cols = 10  #number of columns, can be changed
    col_width = 400 / cols  #Calculate cell width
    for X in range(cols): #loop to control x start point
        for Y in range(cols): #loop to control y start point
            x = X * col_width
            y = Y * col_width
            drawObject(x, y, col_width / 80.0)#calculate size to fill the canvas
    
    
