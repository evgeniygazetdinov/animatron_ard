import tkinter
from tkinter import *
from servo import *

root = Tk()
btn = Button(root,
             text="first",
             width=30,height=5,
             bg="white",fg="black")
btn.bind("<Button-1>", leftw)
btn.pack()
btn2 = Button(root,
             text="second",
             width=30,height=5,
             bg="white",fg="black")
btn2.bind("<Button-1>", rightw)
btn2.pack()

root.mainloop()


