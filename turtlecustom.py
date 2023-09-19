def penfill_color(name,color1, color2):
    name.pencolor(color1)
    name.fillcolor(color2)

def circle(name,x,y,r):
    name.begin_fill()
    name.penup()
    name.goto(x,y)
    name.pendown()
    name.circle(r)
    name.end_fill()

def square(name,x,y,l):
    name.begin_fill()
    name.penup()
    name.goto(x,y)
    name.pendown()
    for i in range(4):
        name.forward(l)
        name.left(90)
    name.end_fill()

def rectangle(name,x,y,l,w):
    name.begin_fill()
    name.penup()
    name.goto(x,y)
    name.pendown()
    for i in range(2):
        name.forward(l)
        name.left(90)
        name.forward(w)
        name.left(90)
    name.end_fill()

def triangle(name,x,y,l):
    name.begin_fill()
    name.penup()
    name.goto(x,y)
    name.pendown()
    for i in range(3):
        name.forward(l)
        name.left(120)
    name.end_fill()