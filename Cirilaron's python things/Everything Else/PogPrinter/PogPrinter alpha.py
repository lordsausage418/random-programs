import tkinter as tk
window = tk.Tk()
window.title("PogPrinter proto")
window.geometry("350x200")
lbl = tk.Label(window, text="Press button to print pog into console")
lbl.grid(column=5, row=0)
def clicked():
    print("pog")
def clicked2():
    print("poggers")
btn = tk.Button(window, text="Button of Pog", command=clicked)
btn.grid(column=5, row=1)
lbl2 = tk.Label(window, text="Customization Buttons")
lbl2.grid(column=5, row=2)
def justpogclick():
    btn.configure(text="Button of Pog", command=clicked)
btnjustpog = tk.Button(window, text="Just Pog", command=justpogclick)
btnjustpog.grid(column=4, row=2)
def gersclick():
    btn.configure(text="Button of Poggers", command=clicked2)
btngers = tk.Button(window, text="-gers", command=gersclick)
btngers.grid(column=6, row=2)
window.mainloop()
