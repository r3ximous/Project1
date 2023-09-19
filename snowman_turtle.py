import turtle
from turtlecustom import penfill_color, circle
#circle(name,y,x,r)
#penfill_color(name,pen color,fill color2)

#step 0; create the board/window
window = turtle.Screen() #create a window
window.title("First Board") #set the title of the window
window.bgcolor("skyblue") #set the background color of the window

#step 1: create a turtle
turta = turtle.Turtle() 
turta.shape("turtle") 
penfill_color(turta,"lightgrey","white")
turta.pensize(5) 
turta.speed(50) 

#step 2: move the turtle

#make snowman body
circle(turta, 0, 200, 50)
circle(turta, 0, 0, 100)
circle(turta, 0, -260, 130)

#make eyes
penfill_color(turta,"black","black")
#make right eye
circle(turta, 25, 250,10)
#make left eye
circle(turta, -25, 250,10)

#make nose
penfill_color(turta,"orange","orange")
turta.begin_fill()
turta.penup()
turta.goto(0,225)
turta.pendown()
turta.left(90)
for i in range(3):
    turta.forward(20)
    turta.right(120)
turta.end_fill()
turta.penup()
turta.goto(0,0)

#step 3: close the window
window.exitonclick() #wait for the user to close the window






