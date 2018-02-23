
from tkinter import *
import tkinter as tk
from tkinter import ttk

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
        self.volume = 0.1
        self.info = ''
        ##########

        self.master = master
        self.master.geometry('300x200')

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.button1 = tk.Button(self.frame, text = 'servo_config', width = 25, command = self.new_window)
        self.button1.pack()


        self.scale = ttk.Scale(orient='horizontal', from_=0.01, to=100,)
        self.scale.pack()


        self.p_bar = ttk.Progressbar(self.frame, orient='horizontal', length=200)
        self.p_bar.pack()


        self.b = ttk.Button(self.frame, text="play/replay", command=self.play_music)
        self.b.pack()

        self.pause = ttk.Button(self.frame, text='pause/unpause', command=self.pause)
        self.pause.pack()


        self.m_time = ttk.Label(self.frame,text =self.min)
        self.m_time.pack()

    def play_music(self):
        self.playing = True
        self.conventer_durability()

        pygame.init()
        pygame.mixer.music.load(self.port1)
        pygame.mixer.music.play()


        if self.playing == True:
            self.p_bar.config(mode='determinate', maximum=self.fin_time, value=1)
            self.p_bar.start(1000)
            self.loud()
            self._on_scale()


    def _on_scale(self):
        value = int(value)
        self.minutes = value/60
        self.sec = value%60
        self.m_time.configure(text="%2.2d:%2.2d" % (self.minutes, self.seconds))


    def pause(self):
        pygame.init()
        self.playing = False

        if self.paused:
            self.playing = True
            pygame.mixer.music.unpause()
            self.paused = False
        else:

            self.paused = True
            pygame.mixer.music.pause()

    def loud(self):
        pygame.mixer.music.set_volume(self.volume)



    def conventer_durability(self):
        tag = TinyTag.get(self.port1)
        self.fin_time = tag.duration
        self.fin_time = int(self.fin_time)
        minutes = self.fin_time / 60
        sec = self.fin_time % 60
        self.minutes = minutes
        self.sec = sec







    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)





    def print_value(self):
        print(self.value)


    def createsound_path(self):
        pass






class Demo2:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x400')
        self.frame = tk.Frame(self.master)
        servo_n = [ 'servo_1','servo_2','servo_3',
                    'servo_4','servo_5','servo_6',
                    'servo_7','servo_8','servo_9',]

        self.lab_ser_1 = ttk.Label(self.master, text='servo-driver_1,choose driver and angle ').grid(row=0,column=1)
        self.check_1 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=1,column=1)
        self.angle_box1 = ttk.Entry(self.master, width=3).grid(row=2,column=1)

        self.lab_ser_2 = ttk.Label(self.master, text='servo-driver_2,choose driver and angle ').grid(row=4,column=1)
        self.check_2 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=5,column=1)
        self.angle_box2 =ttk.Entry(self.master,width=3).grid(row=6,column=1)

        self.lab_ser_3 = ttk.Label(self.master, text='servo-driver_3,choose driver and angle ').grid(row=8,column=1)
        self.check_3 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=9,column=1)
        self.angle_box3 = ttk.Entry(self.master, width=3).grid(row=10,column=1)

        self.lab_ser_4 = ttk.Label(self.master, text='servo-driver_4,choose driver and angle ').grid(row=0,column=2)
        self.check_4 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=1,column=2)
        self.angle_box4 = ttk.Entry(self.master, width=3).grid(row=2,column=2)

        self.lab_ser_5 = ttk.Label(self.master, text='servo-driver_5,choose driver and angle ').grid(row=4,column=2)
        self.check_5 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=5,column=2)
        self.angle_box5 = ttk.Entry(self.master, width=3).grid(row=6,column=2)

        self.lab_ser_6 = ttk.Label(self.master, text='servo-driver_6,choose driver and angle ').grid(row=8,column=2)
        self.check_6 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=9,column=2)
        self.angle_box6 = ttk.Entry(self.master, width=3).grid(row=10,column=2)

        self.lab_ser_7 = ttk.Label(self.master, text='servo-driver_7,choose driver and angle ').grid(row=0,column=3)
        self.check_7 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=1,column=3)
        self.angle_box7 = ttk.Entry(self.master, width=3).grid(row=2,column=3)

        self.lab_ser_8 = ttk.Label(self.master, text='servo-driver_8,choose driver and angle ').grid(row=4,column=3)
        self.check_8 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=5,column=3)
        self.angle_box8 = ttk.Entry(self.master, width=3).grid(row=6,column=3)

        self.lab_ser_9 = ttk.Label(self.master, text='servo-driver_9,choose driver and angle ').grid(row=8,column=3)
        self.check_9 = ttk.Combobox(self.master, textvariable=servo_n).grid(row=9,column=3)
        self.angle_box9 = ttk.Entry(self.master, width=3).grid(row=10,column=3)


        self.button = ttk.Button(self.master,text ='pull value',command= self.take_angle_box_answer).grid(row=13,column=2)

        self.preview = ttk.Button(self.master,text = "preview").grid(row = 14 ,column=2)

        self.add_position = ttk.Button(self.master, text="add action").grid(row=16, column=2)







    def take_angle_box_answer(self):
        answer = self.angle_box1.get()
        print(answer)









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

