'''
import tkinter
import pyfirmata
import time
from config import *
'file contain methods for using servo'
board = pyfirmata.Arduino(port2)
left = board.get_pin('d:8:s')
right = board.get_pin('d:6:s')


def left():
    board = pyfirmata.Arduino(port2)
    left = board.get_pin('d:8:s')
    time.sleep(1)
    left.write(180)
    time.sleep(2)
    left.write(0)
def right():
    board = pyfirmata.Arduino(port2)
    right = board.get_pin('d:6:s')
    time.sleep(1)
    right.write(0)
    time.sleep(2)
    right.write(180)



parent_widget = tkinter.Tk()
lab = tkinter.Label(parent_widget,text='angle')
lab.pack(side = 'top')
entry_widget = tkinter.Entry(parent_widget)

servo_1  = tkinter.Button(parent_widget,text = '1servo',command = left)
servo_1.pack()

servo_2 = tkinter.Button(parent_widget,text = '2servo',command = right)
servo_2.pack()


tkinter.mainloop()










class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Get", command=self.on_button)
        self.button.pack()
        self.entry.pack()

    def on_button(self):
        print(self.entry.get())

w = SampleApp()
w.mainloop()

'''

from pygame import mixer

file = '/home/qbc/Downloads/vdad.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()