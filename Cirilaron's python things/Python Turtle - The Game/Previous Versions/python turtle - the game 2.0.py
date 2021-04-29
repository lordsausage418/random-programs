#/bin/python3
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")

defaultsettings = turtle.textinput("settings", "wanna use default settings? yes or no, lowercase")
if defaultsettings == "yes":
    
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

    wn.onkey(fwd, "w")
    wn.onkey(tleft, "a")
    wn.onkey(tright, "d")
    wn.onkey(taround, "s")
    wn.onkey(penrise, "r")
    wn.onkey(penfall, "f")
    
    turtle.listen()
    
    turtle.mainloop()

elif defaultsettings == "no":
    
    wndwbgcolor = turtle.textinput("bg color", "what color should background be? lowercase")
    
    trtlpencolor = turtle.textinput("turtle color", "what color is turtle? lowercase")
    trtlfillcolor = turtle.textinput("turtle fill color", "what color will turtle fill with? lowercase")
    trtlpenwidth = turtle.numinput("turtle pen width", "what is width of turtle's pen? number")
    trtlshape = turtle.textinput("turtle shape", "what shape is turtle? arrow, turtle, circle, square or triangle. lowercase, anything else for classic")
    trtlgender = turtle.textinput("turtle gender", "what gender is turtle? male or female, lowercase, anything else for non-binary")

    if trtlgender == "male":
        wn.bgcolor(wndwbgcolor)
        wn.title("Python Turtle - The Game: Now Playing As: david")

        david = turtle.Turtle()
        david.color(trtlpencolor, trtlfillcolor)
        david.pensize(width=trtlpenwidth)
        if trtlshape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
           david.shape(trtlshape)

        else:
            david.shape("classic")
        
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

        wn.onkey(fwd, "w")
        wn.onkey(tleft, "a")
        wn.onkey(tright, "d")
        wn.onkey(taround, "s")
        wn.onkey(penrise, "r")
        wn.onkey(penfall, "f")
    
        turtle.listen()
    
        turtle.mainloop()
    elif trtlgender == "female":
        wn.bgcolor(wndwbgcolor)
        wn.title("Python Turtle - The Game: Now Playing As: jane")

        jane = turtle.Turtle()
        jane.color(trtlpencolor, trtlfillcolor)
        jane.pensize(width=trtlpenwidth)
        if trtlshape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
           jane.shape(trtlshape)

        else:
            jane.shape("classic")
        
        def fwd():
            jane.fd(75)

        def tleft():
            jane.left(45)

        def tright():
            jane.right(45)

        def taround():
            jane.left(180)

        def penrise():
            jane.penup()

        def penfall():
            jane.pendown()

        wn.onkey(fwd, "w")
        wn.onkey(tleft, "a")
        wn.onkey(tright, "d")
        wn.onkey(taround, "s")
        wn.onkey(penrise, "r")
        wn.onkey(penfall, "f")
    
        turtle.listen()
    
        turtle.mainloop()
    else:
        wn.bgcolor(wndwbgcolor)
        wn.title("Python Turtle - The Game: Now Playing As: robin")

        robin = turtle.Turtle()
        robin.color(trtlpencolor, trtlfillcolor)
        robin.pensize(width=trtlpenwidth)
        if trtlshape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
           robin.shape(trtlshape)

        else:
            robin.shape("classic")
        
        def fwd():
            robin.fd(75)

        def tleft():
            robin.left(45)

        def tright():
            robin.right(45)

        def taround():
            robin.left(180)

        def penrise():
            robin.penup()

        def penfall():
            robin.pendown()

        wn.onkey(fwd, "w")
        wn.onkey(tleft, "a")
        wn.onkey(tright, "d")
        wn.onkey(taround, "s")
        wn.onkey(penrise, "r")
        wn.onkey(penfall, "f")
    
        turtle.listen()
    
        turtle.mainloop()
else:
    print("uhh thats not an option, restart and try again")
    wn.bye
    input()
    
