import time as wait 
import tkinter as tk
import _thread
window = tk.Tk()
window.config(bg="black")
window.title("Project Alpha")
Hello = tk.Label(window, text="Lets raveeeee like a craab", font=("Courier", 15), fg="orangered", bg="black")
Hello.pack(side="top")
stoppressed = "no"
pausedance = "false"

dance1 = """
 C  0 0  C
  \ I I /
  (___)
   ///   \\\\\ """
dance2 = """
  C 0 0  C
  | I I /
  (___)
   ///   \\\\\ """
dance3 = """
  C 0 0 C 
  | I I | 
  (___)
   ///   \\\\\ """
dance4 = """
 C  0 0 C 
  \ I I | 
  (___)
   ///   \\\\\ """
whitespace = """
         
         
         
         """

crab1 =tk.Label(window, text=dance1, font=("Courier", 13), fg="orangered", bg="black")
crab2 =tk.Label(window, text=dance1, font=("Courier", 13), fg="orangered", bg="black")
crab3 =tk.Label(window, text=dance1, font=("Courier", 13), fg="orangered", bg="black")
crab4 =tk.Label(window, text=dance1, font=("Courier", 13), fg="orangered", bg="black")
whitespace1 = tk.Label(window, text=whitespace, font=("Courier", 13), fg="orangered", bg="black")
whitespace2 = tk.Label(window, text=whitespace, font=("Courier", 13), fg="orangered", bg="black")
crab1.pack(side="left")
whitespace1.pack(side="left")
crab2.pack(side="left")
crab3.pack(side="right")
whitespace2.pack(side="right")
crab4.pack(side="right")

def dance(num):
  if stoppressed != "yes":
    button.config(text="Stop", command=stopthread)
  while True:
    crab1.config(text = dance2)
    crab2.config(text = dance2)
    crab3.config(text = dance2)
    crab4.config(text = dance2)
    wait.sleep(0.2)
    crab1.config(text = dance3)
    crab2.config(text = dance3)
    crab3.config(text = dance3)
    crab4.config(text = dance3)
    wait.sleep(0.2)
    crab1.config(text = dance4)
    crab2.config(text = dance4)
    crab3.config(text = dance4)
    crab4.config(text = dance4)
    wait.sleep(0.2)
    crab1.config(text = dance1)
    crab2.config(text = dance1)
    crab3.config(text = dance1)
    crab4.config(text = dance1)
    wait.sleep(0.2)
    if pausedance == "true":
      continue
def stop(num):
  global stoppressed
  stoppressed = "yes"
  global pausedance
  pausedance = "true"
  Hello.config(text="You fool, you can never stop raving")
  button.pack_forget()
  wait.sleep(3)
  pausedance == "false"
def dancethread():
  _thread.start_new_thread(dance, (0,))
def stopthread():
  _thread.start_new_thread(stop, (0,))
button = tk.Button(window, text="Rave!", command=dancethread)
button.pack(side="bottom")
window.mainloop()