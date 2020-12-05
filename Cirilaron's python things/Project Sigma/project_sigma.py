import turtle
import tkinter as tk

root = tk.Tk()
root.configure(bg="black")
root.geometry("450x500")
root.title("Project Sigma")

frame = tk.Frame(root, bg="black")
frame.pack()

bottomframe = tk.Frame(root, bg="black")
bottomframe.pack(side="bottom")

labelone = tk.Label(frame, bg="black", fg="green", text="Hi, i'm a program made by Cirilaron.\n My name is Sigma.\n I will have most of his programs later.")
labelone.pack(side="top")
labelone.config(font=("Courier", 15))

labeltwo = tk.Label(bottomframe, bg="black", fg="green", text="Press the button to open the program menu")
labeltwo.config(font=("Courier", 15))
labeltwo.pack(side="top")

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
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(command=programsmenu)
    prgrmsbutton.pack(side="bottom")
    
trianglerun = tk.Button(bottomframe, text="Triangle", command=triangle)

def programsmenu():
    labelone.config(text="Program List:\nTriangle: draws a triangle with ASCII\nPress Back to go to the main menu")
    labeltwo.config(text="Run a program:")
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(text="Back", command=mainmenu)
    prgrmsbutton.pack(side="left")
    trianglerun.pack(side="right")

def mainmenu():
    labelone.config(text="Hi, i'm a program made by Cirilaron.\n My name is Sigma.\n I will have most of his programs later.")
    labeltwo.config(text="Press the button to open the command menu")
    trianglerun.pack_forget()
    prgrmsbutton.pack_forget()
    prgrmsbutton.config(text="Programs", command=programsmenu)
    prgrmsbutton.pack(side="bottom")
    
prgrmsbutton = tk.Button(bottomframe, text="Programs", command=programsmenu)
prgrmsbutton.pack(side="bottom")
root.mainloop()