import turtle
import tkinter as tk

root = tk.Tk()
root.configure(bg="black")
root.geometry("650x570")
root.title("Project Sigma")

frame = tk.Frame(root, bg="black")
frame.pack()

bottomframe = tk.Frame(root, bg="black")
bottomframe.pack(side="bottom")

labelone = tk.Label(
    frame,
    bg="black",
    fg="green",
    text=
    "Hi, i'm a program made by Cirilaron.\n My name is Sigma.\n I will have most of his programs later."
)
labelone.pack(side="top")
labelone.config(font=("Courier", 15))

labeltwo = tk.Label(
    bottomframe,
    bg="black",
    fg="green",
    text="Press the button to open the program menu")
labeltwo.config(font=("Courier", 15))
labeltwo.pack(side="top")

canvasboi = tk.Canvas(frame, bg="black", width=400, height=400, relief="flat")
screenboi = turtle.TurtleScreen(canvasboi)
screenboi.bgcolor("black")

david = turtle.RawTurtle(screenboi)


def darkmodesquare():
    trianglerun.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(command=programsmenu, text="Back")
    prgrmsbutton.pack(side="bottom")
    dmsbutton.pack_forget()
    labelone.config(text="Here, have a square.")
    labeltwo.config(text="drawing...")
    david.color("white", "gray")
    david.pensize(10)
    canvasboi.pack(side="bottom")
    david.fd(150)
    david.left(90)
    david.fd(150)
    david.left(90)
    david.fd(150)
    david.left(90)
    david.fd(150)
    david.left(90)
    labeltwo.config(text="like it? yeah you do.")


dmsbutton = tk.Button(
    bottomframe, text="Dark Mode Square", command=darkmodesquare)


def triangle():
    trianglestring = """    /\ 
    /  \ 
    /    \ 
    /      \ 
    /        \ 
    /          \ 
    /            \ 
    /              \ 
    /                \ 
    /                  \ 
    /                    \ 
    /                      \ 
    /________________________\ 
    triangle go brr"""
    labelone.config(text=trianglestring)
    labeltwo.config(text="Press back to return to program menu")
    trianglerun.pack_forget()
    dmsbutton.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(command=programsmenu)
    prgrmsbutton.pack(side="bottom")


trianglerun = tk.Button(bottomframe, text="Triangle", command=triangle)


def programsmenu():
    labelone.config(
        text=
        "Program List:\nTriangle: draws a triangle with ASCII\nDark Mode Square: draws a white square using turtle\nPress Back to go to the main menu"
    )
    labeltwo.config(text="Run a program:")
    canvasboi.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(text="Back", command=mainmenu)
    prgrmsbutton.pack(side="left")
    trianglerun.pack(side="right")
    dmsbutton.pack(side="bottom")
    david.clear()


def mainmenu():
    labelone.config(
        text=
        "Hi, i'm a program made by Cirilaron.\n My name is Sigma.\n I will have most of his programs later."
    )
    labeltwo.config(text="Press the button to open the command menu")
    trianglerun.pack_forget()
    dmsbutton.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(text="Programs", command=programsmenu)
    prgrmsbutton.pack(side="bottom")


prgrmsbutton = tk.Button(bottomframe, text="Programs", command=programsmenu)
prgrmsbutton.pack(side="bottom")
root.mainloop()
