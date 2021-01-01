import turtle

wn = turtle.Screen()
wn.bgcolor("black")

defaultsettings = turtle.textinput("settings", "wanna use default settings? yes or no, lowercase")
if defaultsettings == "yes":

    wn.bgcolor("black")
    wn.title("Python Turtle - The Game: Now Playing As: david")

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

    trtlamount = turtle.numinput("player amount", "how much players? 1-3", minval=1, maxval=3)
    trtlpencolor = turtle.textinput("turtle color", "what color is turtle? lowercase")
    trtlfillcolor = turtle.textinput("turtle fill color", "what color will turtle fill with? lowercase")
    trtlpenwidth = turtle.numinput("turtle pen width", "what is width of turtle's pen? number")
    trtlshape = turtle.textinput("turtle shape", "what shape is turtle? arrow, turtle, circle, square or triangle. lowercase, anything else for classic")
    trtlgender = turtle.textinput("turtle gender", "what gender is turtle? male or female, lowercase, anything else for non-binary")
    if trtlamount == 1:
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

    elif trtlamount == 2:
         trtl2pencolor = turtle.textinput("turtle color", "what color is turtle 2? lowercase")
         trtl2fillcolor = turtle.textinput("turtle fill color", "what color will turtle 2 fill with? lowercase")
         trtl2penwidth = turtle.numinput("turtle pen width", "what is width of turtle 2's pen? number")
         trtl2shape = turtle.textinput("turtle shape", "what shape is turtle 2? arrow, turtle, circle, square or triangle. lowercase, anything else for classic")
         trtl2gender = turtle.textinput("turtle gender", "what gender is turtle 2? male or female, lowercase, anything else for non-binary")

         if trtlgender == "male":

            wn.bgcolor(wndwbgcolor)

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

            if trtl2gender == "male":
                wn.title("Python Turtle - The Game: Now Playing As: david And daniel")
                
                daniel = turtle.Turtle()
                daniel.color(trtl2pencolor, trtl2fillcolor)
                david.pensize(width=trtl2penwidth)
                if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                    daniel.shape(trtlshape)
  
                else:
                    daniel.shape("classic")
        
                def fwd2():
                    daniel.fd(75)

                def tleft2():
                    daniel.left(45)

                def tright2():
                    daniel.right(45)

                def taround2():
                    daniel.left(180)

                def penrise2():
                    daniel.penup()

                def penfall2():
                    daniel.pendown()

                wn.onkey(fwd2, "i")
                wn.onkey(tleft2, "j")
                wn.onkey(tright2, "l")
                wn.onkey(taround2, "k")
                wn.onkey(penrise2, "o")
                wn.onkey(penfall2, "p")

                turtle.listen()

                turtle.mainloop()

            elif trtl2gender == "female":

                 wn.title("Python Turtle - The Game: Now Playing As: david And jane")
                
                 jane = turtle.Turtle()
                 jane.color(trtl2pencolor, trtl2fillcolor)
                 jane.pensize(width=trtl2penwidth)
                 if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                     jane.shape(trtlshape)
  
                 else:
                     jane.shape("classic")
         
                 def fwd2():
                     jane.fd(75)

                 def tleft2():
                     jane.left(45)

                 def tright2():
                     jane.right(45)

                 def taround2():
                     jane.left(180)

                 def penrise2():
                     jane.penup()

                 def penfall2():
                     jane.pendown()

                 wn.onkey(fwd2, "i")
                 wn.onkey(tleft2, "j")
                 wn.onkey(tright2, "l")
                 wn.onkey(taround2, "k")
                 wn.onkey(penrise2, "o")
                 wn.onkey(penfall2, "p")

                 turtle.listen()

                 turtle.mainloop()

            else:
                wn.title("Python Turtle - The Game: Now Playing As: david And robin")
                
                robin = turtle.Turtle()
                robin.color(trtl2pencolor, trtl2fillcolor)
                robin.pensize(width=trtl2penwidth)
                if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                   robin.shape(trtlshape)
  
                else:
                    robin.shape("classic")
        
                def fwd2():
                    robin.fd(75)

                def tleft2():
                    robin.left(45)

                def tright2():
                    robin.right(45)

                def taround2():
                    robin.left(180)

                def penrise2():
                    robin.penup()

                def penfall2():
                    robin.pendown()

                wn.onkey(fwd2, "i")
                wn.onkey(tleft2, "j")
                wn.onkey(tright2, "l")
                wn.onkey(taround2, "k")
                wn.onkey(penrise2, "o")
                wn.onkey(penfall2, "p")

                turtle.listen()

                turtle.mainloop()

         if trtlgender == "female":

            wn.bgcolor(wndwbgcolor)

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

            if trtl2gender == "male":
                wn.title("Python Turtle - The Game: Now Playing As: jane And david")
                
                david = turtle.Turtle()
                david.color(trtl2pencolor, trtl2fillcolor)
                david.pensize(width=trtl2penwidth)
                if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                   david.shape(trtlshape)
  
                else:
                    david.shape("classic")
        
                def fwd2():
                    david.fd(75)

                def tleft2():
                    david.left(45)

                def tright2():
                    david.right(45)

                def taround2():
                    david.left(180)

                def penrise2():
                    daniel.penup()

                def penfall2():
                    david.pendown()

                wn.onkey(fwd2, "i")
                wn.onkey(tleft2, "j")
                wn.onkey(tright2, "l")
                wn.onkey(taround2, "k")
                wn.onkey(penrise2, "o")
                wn.onkey(penfall2, "p")

                turtle.listen()

                turtle.mainloop()

            elif trtl2gender == "female":

                 wn.title("Python Turtle - The Game: Now Playing As: jane And jill")
                
                 jill = turtle.Turtle()
                 jill.color(trtl2pencolor, trtl2fillcolor)
                 jill.pensize(width=trtl2penwidth)
                 if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                     jill.shape(trtlshape)
  
                 else:
                     jill.shape("classic")
         
                 def fwd2():
                     jill.fd(75)

                 def tleft2():
                     jill.left(45)

                 def tright2():
                     jill.right(45)

                 def taround2():
                     jill.left(180)

                 def penrise2():
                     jill.penup()

                 def penfall2():
                     jill.pendown()

                 wn.onkey(fwd2, "i")
                 wn.onkey(tleft2, "j")
                 wn.onkey(tright2, "l")
                 wn.onkey(taround2, "k")
                 wn.onkey(penrise2, "o")
                 wn.onkey(penfall2, "p")

                 turtle.listen()

                 turtle.mainloop()

            else:
                wn.title("Python Turtle - The Game: Now Playing As: jill And robin")
                
                robin = turtle.Turtle()
                robin.color(trtl2pencolor, trtl2fillcolor)
                robin.pensize(width=trtl2penwidth)
                if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                   robin.shape(trtlshape)
  
                else:
                    robin.shape("classic")
        
                def fwd2():
                    robin.fd(75)

                def tleft2():
                    robin.left(45)

                def tright2():
                    robin.right(45)

                def taround2():
                    robin.left(180)

                def penrise2():
                    robin.penup()

                def penfall2():
                    robin.pendown()

                wn.onkey(fwd2, "i")
                wn.onkey(tleft2, "j")
                wn.onkey(tright2, "l")
                wn.onkey(taround2, "k")
                wn.onkey(penrise2, "o")
                wn.onkey(penfall2, "p")

                turtle.listen()

                turtle.mainloop()

         else:

            wn.bgcolor(wndwbgcolor)

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

            if trtl2gender == "male":
                wn.title("Python Turtle - The Game: Now Playing As: robin And david")
                
                david = turtle.Turtle()
                david.color(trtl2pencolor, trtl2fillcolor)
                david.pensize(width=trtl2penwidth)
                if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                   david.shape(trtlshape)
  
                else:
                    david.shape("classic")
        
                def fwd2():
                    david.fd(75)

                def tleft2():
                    david.left(45)

                def tright2():
                    david.right(45)

                def taround2():
                    david.left(180)

                def penrise2():
                    daniel.penup()

                def penfall2():
                    david.pendown()

                wn.onkey(fwd2, "i")
                wn.onkey(tleft2, "j")
                wn.onkey(tright2, "l")
                wn.onkey(taround2, "k")
                wn.onkey(penrise2, "o")
                wn.onkey(penfall2, "p")

                turtle.listen()

                turtle.mainloop()

            elif trtl2gender == "female":

                 wn.title("Python Turtle - The Game: Now Playing As: robin And jill")
                
                 jill = turtle.Turtle()
                 jill.color(trtl2pencolor, trtl2fillcolor)
                 jill.pensize(width=trtl2penwidth)
                 if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                     jill.shape(trtlshape)
  
                 else:
                     jill.shape("classic")
         
                 def fwd2():
                     jill.fd(75)

                 def tleft2():
                     jill.left(45)

                 def tright2():
                     jill.right(45)

                 def taround2():
                     jill.left(180)

                 def penrise2():
                     jill.penup()

                 def penfall2():
                     jill.pendown()

                 wn.onkey(fwd2, "i")
                 wn.onkey(tleft2, "j")
                 wn.onkey(tright2, "l")
                 wn.onkey(taround2, "k")
                 wn.onkey(penrise2, "o")
                 wn.onkey(penfall2, "p")

                 turtle.listen()

                 turtle.mainloop()

            else:
                wn.title("Python Turtle - The Game: Now Playing As: robin And rowan")
                
                rowan = turtle.Turtle()
                rowan.color(trtl2pencolor, trtl2fillcolor)
                rowan.pensize(width=trtl2penwidth)
                if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":
            
                   rowan.shape(trtlshape)
  
                else:
                    rowan.shape("classic")
        
                def fwd2():
                    rowan.fd(75)

                def tleft2():
                    rowan.left(45)

                def tright2():
                    rowan.right(45)

                def taround2():
                    rowan.left(180)

                def penrise2():
                    rowan.penup()

                def penfall2():
                    rowan.pendown()

                wn.onkey(fwd2, "i")
                wn.onkey(tleft2, "j")
                wn.onkey(tright2, "l")
                wn.onkey(taround2, "k")
                wn.onkey(penrise2, "o")
                wn.onkey(penfall2, "p")

                turtle.listen()

                turtle.mainloop()

    elif trtlamount == 3:
        print("Sorry, but that feature isn't complete yet. Please restart the program and choose either 1 or 2.")
        input()

else:
    print("uhh thats not an option, restart and try again")
    wn.bye
    input()