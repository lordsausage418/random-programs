#/bin/python3
import turtle
import tkinter as tk

ispog = "waiting"
question = tk.Tk()
question.geometry("250x100")
question.title("ADHP")
lbl = tk.Label(question, text="is david the turtle pog?")
lbl.grid(column=5, row=0)


def pogyes():
    global ispog
    ispog = "yes"
    question.destroy()


def pogno():
    global ispog
    ispog = "no"
    question.destroy()


btnyes = tk.Button(question, text="yes", command=pogyes)
btnyes.grid(column=4, row=1)
btnno = tk.Button(question, text="no", command=pogno)
btnno.grid(column=6, row=1)
question.mainloop()

if ispog == "yes":

    defaultsettings = "waiting"
    question = tk.Tk()
    question.geometry("250x100")
    question.title("default settings")
    lbl = tk.Label(question, text="do you wanna use default settings?")
    lbl.grid(column=5, row=0)

    def defaultyes():
        global defaultsettings
        defaultsettings = "yes"
        question.destroy()

    def defaultno():
        global defaultsettings
        defaultsettings = "no"
        question.destroy()

    btnyes = tk.Button(question, text="yes", command=defaultyes)
    btnyes.grid(column=4, row=1)
    btnno = tk.Button(question, text="no", command=defaultno)
    btnno.grid(column=6, row=1)
    question.mainloop()

    if defaultsettings == "yes":

        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Python Turtle - The Game: Now Playing As: david")
        trtl1 = turtle.Turtle()
        trtl1.color("white", "gray")
        trtl1.pensize(width=10)
        trtl1.shape("turtle")

        def fwd():
            trtl1.fd(75)

        def tleft():
            trtl1.left(45)

        def tright():
            trtl1.right(45)

        def taround():
            trtl1.left(180)

        def penrise():
            trtl1.penup()

        def penfall():
            trtl1.pendown()

        wn.onkey(fwd, "w")
        wn.onkey(tleft, "a")
        wn.onkey(tright, "d")
        wn.onkey(taround, "s")
        wn.onkey(penrise, "r")
        wn.onkey(penfall, "f")

        turtle.listen()

        turtle.mainloop()

    elif defaultsettings == "no":

        wndwbgcolor = turtle.textinput("bg color",
                                       "what color should background be?")

        trtlamount = turtle.numinput(
            "player amount", "how much players? 1-3", minval=1, maxval=3)
        trtlpencolor = turtle.textinput("turtle color",
                                        "what color is turtle? lowercase")
        trtlfillcolor = turtle.textinput(
            "turtle fill color", "what color will turtle fill with? lowercase")
        trtlpenwidth = turtle.numinput(
            "turtle pen width", "what is width of turtle's pen? number")
        trtlshape = turtle.textinput(
            "turtle shape",
            "what shape is turtle? arrow, turtle, circle, square or triangle. lowercase, anything else for classic"
        )
        trtlgender = turtle.textinput(
            "turtle gender",
            "what gender is turtle? male or female, lowercase, anything else for non-binary"
        )

        if trtlamount == 1:
            wn = turtle.Screen()
            wn.bgcolor(wndwbgcolor)

            trtl1 = turtle.Turtle()
            trtl1.color(trtlpencolor, trtlfillcolor)
            trtl1.pensize(width=trtlpenwidth)
            if trtlshape == "arrow" or "turtle" or "circle" or "triangle" or "square":

                trtl1.shape(trtlshape)

            else:
                trtl1.shape("classic")

            def fwd():
                trtl1.fd(75)

            def tleft():
                trtl1.left(45)

            def tright():
                trtl1.right(45)

            def taround():
                trtl1.left(180)

            def penrise():
                trtl1.penup()

            def penfall():
                trtl1.pendown()

            wn.onkey(fwd, "w")
            wn.onkey(tleft, "a")
            wn.onkey(tright, "d")
            wn.onkey(taround, "s")
            wn.onkey(penrise, "r")
            wn.onkey(penfall, "f")

            if trtlgender == "male":
                wn.title("Python Turtle - The Game: Now Playing As: david")

            elif trtlgender == "female":
                wn.title("Python Turtle - The Game: Now Playing As: jane")

            else:
                wn.title("Python Turtle - The Game: Now Playing As: robin")
            turtle.listen()
            turtle.mainloop()

        elif trtlamount == 2:
            trtl2pencolor = turtle.textinput(
                "turtle color", "what color is turtle 2? lowercase")
            trtl2fillcolor = turtle.textinput(
                "turtle fill color",
                "what color will turtle 2 fill with? lowercase")
            trtl2penwidth = turtle.numinput(
                "turtle pen width", "what is width of turtle 2's pen? number")
            trtl2shape = turtle.textinput(
                "turtle shape",
                "what shape is turtle 2? arrow, turtle, circle, square or triangle. lowercase, anything else for classic"
            )
            trtl2gender = turtle.textinput(
                "turtle gender",
                "what gender is turtle 2? male or female, lowercase, anything else for non-binary"
            )
            wn = turtle.Screen()
            wn.bgcolor(wndwbgcolor)

            trtl1 = turtle.Turtle()
            trtl1.color(trtlpencolor, trtlfillcolor)
            trtl1.pensize(width=trtlpenwidth)
            if trtlshape == "arrow" or "turtle" or "circle" or "triangle" or "square":

                trtl1.shape(trtlshape)

            else:
                trtl1.shape("classic")

            def fwd():
                trtl1.fd(75)

            def tleft():
                trtl1.left(45)

            def tright():
                trtl1.right(45)

            def taround():
                trtl1.left(180)

            def penrise():
                trtl1.penup()

            def penfall():
                trtl1.pendown()

            wn.onkey(fwd, "w")
            wn.onkey(tleft, "a")
            wn.onkey(tright, "d")
            wn.onkey(taround, "s")
            wn.onkey(penrise, "r")
            wn.onkey(penfall, "f")

            trtl2 = turtle.Turtle()
            trtl2.color(trtl2pencolor, trtl2fillcolor)
            trtl2.pensize(width=trtlpenwidth)
            if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":

                trtl2.shape(trtlshape)

            else:
                trtl2.shape("classic")

            def fwd2():
                trtl2.fd(75)

            def tleft2():
                trtl2.left(45)

            def tright2():
                trtl2.right(45)

            def taround2():
                trtl2.left(180)

            def penrise2():
                trtl2.penup()

            def penfall2():
                trtl2.pendown()

            wn.onkey(fwd, "i")
            wn.onkey(tleft, "j")
            wn.onkey(tright, "l")
            wn.onkey(taround, "k")
            wn.onkey(penrise, "o")
            wn.onkey(penfall, "p")

            if trtlgender == "male":
                if trtl2gender == "male":
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: david And daniel"
                    )
                elif trtl2gender == "female":
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: david And jane"
                    )
                else:
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: david And robin"
                    )

            elif trtlgender == "female":
                if trtl2gender == "male":
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: jane And david"
                    )
                elif trtl2gender == "female":
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: jane And jill"
                    )
                else:
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: jane And robin"
                    )

            else:
                if trtl2gender == "male":
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: robin And david"
                    )
                elif trtl2gender == "female":
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: robin And jane"
                    )
                else:
                    wn.title(
                        "Python Turtle - The Game: Now Playing As: robin And rowan"
                    )
            turtle.listen()
            turtle.mainloop()

        elif trtlamount == 3:
            trtl2pencolor = turtle.textinput(
                "turtle color", "what color is turtle 2? lowercase")
            trtl2fillcolor = turtle.textinput(
                "turtle fill color",
                "what color will turtle 2 fill with? lowercase")
            trtl2penwidth = turtle.numinput(
                "turtle pen width", "what is width of turtle 2's pen? number")
            trtl2shape = turtle.textinput(
                "turtle shape",
                "what shape is turtle 2? arrow, turtle, circle, square or triangle. lowercase, anything else for classic"
            )
            trtl2gender = turtle.textinput(
                "turtle gender",
                "what gender is turtle 2? male or female, lowercase, anything else for non-binary"
            )
            trtl3pencolor = turtle.textinput(
                "turtle color", "what color is turtle 3? lowercase")
            trtl3fillcolor = turtle.textinput(
                "turtle fill color",
                "what color will turtle 2 fill with? lowercase")
            trtl3penwidth = turtle.numinput(
                "turtle pen width", "what is width of turtle 3's pen? number")
            trtl3shape = turtle.textinput(
                "turtle shape",
                "what shape is turtle 3? arrow, turtle, circle, square or triangle. lowercase, anything else for classic"
            )
            trtl3gender = turtle.textinput(
                "turtle gender",
                "what gender is turtle 3? male or female, lowercase, anything else for non-binary"
            )
            wn = turtle.Screen()
            wn.bgcolor(wndwbgcolor)

            trtl1 = turtle.Turtle()
            trtl1.color(trtlpencolor, trtlfillcolor)
            trtl1.pensize(width=trtlpenwidth)
            if trtlshape == "arrow" or "turtle" or "circle" or "triangle" or "square":

                trtl1.shape(trtlshape)

            else:
                trtl1.shape("classic")

            def fwd():
                trtl1.fd(75)

            def tleft():
                trtl1.left(45)

            def tright():
                trtl1.right(45)

            def taround():
                trtl1.left(180)

            def penrise():
                trtl1.penup()

            def penfall():
                trtl1.pendown()

            wn.onkey(fwd, "w")
            wn.onkey(tleft, "a")
            wn.onkey(tright, "d")
            wn.onkey(taround, "s")
            wn.onkey(penrise, "r")
            wn.onkey(penfall, "f")

            trtl2 = turtle.Turtle()
            trtl2.color(trtl2pencolor, trtl2fillcolor)
            trtl2.pensize(width=trtlpenwidth)
            if trtl2shape == "arrow" or "turtle" or "circle" or "triangle" or "square":

                trtl2.shape(trtlshape)

            else:
                trtl2.shape("classic")

            def fwd2():
                trtl2.fd(75)

            def tleft2():
                trtl2.left(45)

            def tright2():
                trtl2.right(45)

            def taround2():
                trtl2.left(180)

            def penrise2():
                trtl2.penup()

            def penfall2():
                trtl2.pendown()

            wn.onkey(fwd, "i")
            wn.onkey(tleft, "j")
            wn.onkey(tright, "l")
            wn.onkey(taround, "k")
            wn.onkey(penrise, "o")
            wn.onkey(penfall, "p")

            trtl3 = turtle.Turtle()
            trtl3.color(trtl2pencolor, trtl2fillcolor)
            trtl3.pensize(width=trtlpenwidth)
            if trtl3shape == "arrow" or "turtle" or "circle" or "triangle" or "square":

                trtl3.shape(trtlshape)

            else:
                trtl3.shape("classic")

            def fwd3():
                trtl3.fd(75)

            def tleft3():
                trtl3.left(45)

            def tright3():
                trtl2.right(45)

            def taround3():
                trtl3.left(180)

            def penrise3():
                trtl3.penup()

            def penfall3():
                trtl3.pendown()

            wn.onkey(fwd, "g")
            wn.onkey(tleft, "c")
            wn.onkey(tright, "v")
            wn.onkey(taround, "b")
            wn.onkey(penrise, "n")
            wn.onkey(penfall, "m")

            if trtlgender == "male":
                if trtl2gender == "male":
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As david, daniel And damien"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As: david, daniel And jane"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As david, daniel And robin"
                        )
                elif trtl2gender == "female":
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As david, jane And daniel"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As david, jane And jill"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As david, jane And robin"
                        )
                else:
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As david, robin And daniel"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game : Now Playing As: david, robin And jane"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As david, robin And rowan"
                        )
            elif trtlgender == "female":
                if trtl2gender == "male":
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As jane, david And daniel"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As: jane, david And jill"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As jane, david And robin"
                        )
                elif trtl2gender == "female":
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As jane, jill And david"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As jane, jill And jade"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As jane, jill And robin"
                        )
                else:
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As jane, robin And david"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game : Now Playing As: jane, robin And jill"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As jane, robin  And rowan"
                        )
            else:
                if trtl2gender == "male":
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As robin, david And daniel"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As: robin, david And jane"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As robin, david And rowan"
                        )
                elif trtl2gender == "female":
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As robin, jane And david"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As robin, jane And jill"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As robin, jane And rowan"
                        )
                else:
                    if trtl3gender == "male":
                        wn.title(
                            "Python Turtle - The Game: Now Playing As robin, rowan And david"
                        )
                    elif trtl3gender == "female":
                        wn.title(
                            "Python Turtle - The Game : Now Playing As: robin, rowan And jane"
                        )
                    else:
                        wn.title(
                            "Python Turtle - The Game: Now Playing As robin, rowan And riley"
                        )
            turtle.listen()
            turtle.mainloop()

elif ispog == "no":
    print("leave. now.")
