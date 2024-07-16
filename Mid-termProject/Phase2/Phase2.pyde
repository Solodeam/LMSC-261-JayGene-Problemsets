#Phase 2, this will print out the shape I drawed, 1 grid = 10 pixels
#1. setup the canvas
def setup():
    size(80, 80)
    noStroke()
    
#2. drawing
def draw():
    #Head:
    fill(0)
    rect(0, 0, 80, 80)
    #Eye
    fill(222, 122, 250)
    rect(0, 40, 30,10)
    rect(50, 40, 30,10)
    #pupil
    fill(200, 0, 250)
    rect(10, 40, 10, 10)
    rect(60, 40, 10, 10)
