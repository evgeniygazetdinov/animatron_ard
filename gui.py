import tkinter
from tkinter import *

def one(event):
	print('2')
def two(event):
    print('3')
def three(event):
    print('1')

root = Tk()
btn = Button(root,
             text="first",
             width=30,height=5,
             bg="white",fg="black")
btn.bind("<Button-1>", one)
btn.pack()
btn2 = Button(root,
             text="second",
             width=30,height=5,
             bg="white",fg="black")
btn2.bind("<Button-1>", two)
btn2.pack()
btn3 = Button(root,
             text="third",
             width=30,height=5,
             bg="white",fg="black")
btn3.bind("<Button-1>", three)
btn3.pack()
root.mainloop()


