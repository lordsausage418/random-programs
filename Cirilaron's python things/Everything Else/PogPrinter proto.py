import tkinter as tk
window = tk.Tk()
window.title("PogPrinter proto")
window.geometry("350x200")
lbl = tk.Label(window, text="Press button to print pog into console")
lbl.grid(column=5, row=0)
def clicked():
    print("pog")
btn = tk.Button(window, text="Button of Pog", command=clicked)
btn.grid(column=5, row=1)
window.mainloop()
