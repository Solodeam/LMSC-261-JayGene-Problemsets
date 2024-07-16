# Phase 5

def setup():
    size(400, 400)
    noStroke()
    frameRate(60) # added framrate
# Turn shape into function
def drawObject(x, y, s, r):
    push()  # save
    translate(x + 40 * s, y + 40 * s)  # Move origin to the center of the object
    scale(s)
    rotate(r)#added rotation parameter
    
    # Head
    fill(0)
    rect(-40, -40, 80, 80)
    # Eyes
    fill(222, 122, 250)
    rect(-40, 0, 30, 10)
    rect(10, 0, 30, 10)
    # Pupils
    fill(200, 0, 250)
    rect(-30, 0, 10, 10)
    rect(20, 0, 10, 10)

    pop()  # restore

# Painting
def draw():
    background(sin(frameCount * 0.01)* 255)  # clear the background
    cols = 4  # number of columns, can be changed
    col_width = 400 / cols  # calculate cell width
    for X in range(cols):  # loop to control x start point
        for Y in range(cols):  # loop to control y start point
            x = X * col_width
            y = Y * col_width
            angle_range = 10  # max bank angle
            r = radians(angle_range * sin(frameCount * 0.03))  #controls the speed of rotation

            # Calculate dynamic scaling within a limited range
            base_scale = col_width / 80.0
            scale_range = 0.05  # Maximum scale variation
            s = base_scale - scale_range * sin(frameCount * 0.01)  #controls the speed of scaling
            
            drawObject(x, y, s, r)
