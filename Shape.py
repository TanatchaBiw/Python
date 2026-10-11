import turtle
turtle.speed(5)
turtle.shape("turtle")
def square():
    for b in range(4):
        turtle.forward(100)
        turtle.left(90)

def triangle():
    for b in range(3):
        turtle.forward(100)
        turtle.left(120)

def polygon():
    for b in range(5):
        turtle.forward(100)
        turtle.left(72)
def star():
     for b in range(9):
        turtle.forward(100)
        turtle.left(160)
    
turtle.color("blue")
turtle.begin_fill()
square()
turtle.end_fill()
turtle.goto(-100,0)

turtle.color("red")
turtle.begin_fill()
triangle()
turtle.end_fill()
turtle.goto(-100,-100)

turtle.color("yellow")
turtle.begin_fill()
square()
turtle.end_fill()
turtle.goto(0,-100)

turtle.color("pink")
turtle.begin_fill()
polygon()
turtle.end_fill()

turtle.color("green")
turtle.begin_fill()
star()
turtle.end_fill()

