import turtle
turtle.bgcolor("black")
turtle.pensize(2)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("pink", "white")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(3)
t.color('white')
style = ('times new roman',20,'bold')
t.write('APRILIYANDA',font=style,align='left',move=True)
t.hideturtle()
turtle.bgcolor("black")
turtle.pensize(2)
