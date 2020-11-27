import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")

david = turtle.Turtle()
david.color("white", "gray")
david.pensize(width=10)
david.shape("turtle")

def fwd():
    david.fd(75)

def tleft():
    david.left(45)

def tright():
    david.right(45)

def taround():
    david.left(180)

def penrise():
    david.penup()

def penfall():
    david.pendown()

turtle.listen()

wn.onkey(fwd, "w")
wn.onkey(tleft, "a")
wn.onkey(tright, "d")
wn.onkey(taround, "s")
wn.onkey(penrise, "r")
wn.onkey(penfall, "f")

turtle.mainloop()
