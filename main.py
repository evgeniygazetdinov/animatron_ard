import  tkinter as Tkinter
from tkinter import ttk
import tkinter as tk

import pygame
from tinytag import TinyTag
import time



class Demo1:






    def __init__(self, master):
        ##########
        self.position = 0
        self.playing = False
        self.paused = False
        self.port1 = '/Users/evgeshakrasava/PycharmProjects/c.mp3'
        self.port2 = '/home/qbc/Downloads/c.mp3'

        ##########
        self.pr_time = 0
        self.fin_time = 0
        self.min = 0
        self.sec = 0
        self.value =1
        ##########

        self.master = master
        self.master.geometry('640x480')
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'servo_config', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
        self.scale = Tkinter.Scale(orient='horizontal', from_=0.9, to=180.5, command=self.print_value)
        self.scale.pack()

        self.p_bar = ttk.Progressbar(self.frame, orient='horizontal', length=200)
        self.p_bar.config(mode='determinate', maximum=self.fin_time, value=1)
        self.p_bar.pack()

        self.b = Tkinter.Button(self.frame, text="play", command=self.play_music)
        self.b.pack()

        self.pause = Tkinter.Button(self.frame, text='pause/unpause', command=self.pause)
        self.pause.pack()


        self.m_time = ttk.Label(self.frame,text =self.min)
        self.m_time.pack()
        self.m_time.configure(text="%2.2d:%2.2d" % (self.min,self.sec))





    def play_music(self):
            self.conventer_durability()
            self.p_bar.start(1000)
            pygame.init()
            pygame.mixer.music.load(self.port2)
            pygame.mixer.music.play()



    def pause(self):
        pygame.init()
        self.playing = False
        self.p_bar.stop()
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.paused = True
            pygame.mixer.music.pause()


    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)




    def conventer_durability(self):
        tag = TinyTag.get(self.port2)
        self.fin_time = tag.duration
        self.fin_time = int(self.fin_time)
        minutes = self.fin_time / 60
        sec = self.fin_time % 60
        self.minutes = minutes
        self.sec = sec



    def print_value(self):
        print(self.value)







class Demo2:
    def __init__(self, master):
        self.master = master
        self.master.geometry('640x480')
        self.frame = tk.Frame(self.master)
        self.frame.config(height=5000 ,width=1200)
        self.servo1 =100
        self.servo2 = 50
        self.servo3 = 700
        self.servo4 = 30




        self.servo_box2 = ttk.Combobox(self.master, textvariable=self.servo1)
        self.servo_box2.grid(row = 0,column = 2)

        self.servo_box3 = ttk.Combobox(self.master,textvariable =self.servo2)
        self.servo_box3.grid(row = 1,column = 2)

        self.servo_box4 = ttk.Combobox(self.master, textvariable=self.servo3)
        self.servo_box4.grid(row = 5,column = 3)

        self.servo_box5 = ttk.Combobox(self.master, textvariable=self.servo4)
        self.servo_box5.grid(row = 2,column = 3)

        self.labelframe = ttk.LabelFrame(self.frame, text="This is a LabelFrame")
        self.labelframe.grid(row = 2,column = 3)

        self.left = ttk.Label(self.labelframe, text="Inside the LabelFrame")
        self.left.grid(row = 8,column = 5)




    def close_windows(self):
        self.master.destroy()
    def take(self):
        x=self.servo_box3.get()
        print(x)
def main():
    root = tk.Tk()
    root.title("SERVO_M")
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
