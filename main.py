from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

import os
import pygame
from tinytag import TinyTag
import time
import serial.tools.list_ports
import pyfirmata


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
        self.values = 1
        self.info = ''
        ##########

        self.master = master
        self.master.geometry('300x200')

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.button1 = tk.Button(self.frame, text='servo_config', width=25, command=self.new_window)
        self.button1.pack()

        self.scale = ttk.Scale(orient='horizontal', from_=0.01, to=0.9, command=self.loud).pack()

        self.p_bar = ttk.Progressbar(self.frame, orient='horizontal', length=200)
        self.p_bar.pack()

        self.b = ttk.Button(self.frame, text="play/replay", command=self.play_music)
        self.b.pack()

        self.pause = ttk.Button(self.frame, text='pause/unpause', command=self.pause)
        self.pause.pack()

        self.loop_butt = ttk.Button(self.frame, text='loop', command=self.loop).pack()

        self.open_new = ttk.Button(self.frame, text='open', command=self.add).pack()

        self.m_time = ttk.Label(self.frame, text='')
        self.m_time.pack()

    def play_music(self):
        self.playing = True
        pygame.init()
        pygame.mixer.music.load(self.port2)
        pygame.mixer.music.set_volume(0)  # set volume on zero before play
        pygame.mixer.music.play(-1, 0.0)

        if self.playing == True:
            self.p_bar.config(mode='determinate', maximum=self.fin_time, value=1)
            self.p_bar.start(1000)
            self.conventer_durability()
            self._on_scale()

    def _on_scale(self):
        # initialize time track
        time = int(pygame.mixer.music.get_pos() / 1000)
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        self.m_time.configure(text="%2.2d:%2.2d" % (m, s))
        self.frame.after(1000, self._on_scale)

    '''
    def update_timeslider(self, _=None):
        time = (pygame.mixer.music.get_pos() / 1000)
        timeslider.set(time)
        self.after(10, self.update_timeslider)
    '''

    def pause(self):
        pygame.init()
        self.playing = False

        if self.paused:

            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.p_bar.stop()
            self.paused = True
            pygame.mixer.music.pause()

    def loud(self, value):
        pygame.init()
        pygame.mixer.music.set_volume((float(value)))  # put on pygame module value from scale widget

    def loop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1, 0.0)

    def conventer_durability(self):
        tag = TinyTag.get(self.port2)
        self.fin_time = tag.duration
        self.fin_time = int(self.fin_time)
        minutes = self.fin_time / 60
        sec = self.fin_time % 60

    def add(self):
        file = ttk.askopenfilenames(initialdir='C:/Users/babbu/Downloads')
        songsTuple = self.frame.splitlist(file)  # turn user's opened filenames into tuple
        songsList = list(songsTuple)  # convert to list
        # Add the full filename of songto playlist list, and a shortened version to the listBox
        for song in songsList:
            playlist.append(song);
            tempArray = song.split('/')
            songShort = tempArray[len(tempArray) - 1]
            self.playlistbox.insert(END, songShort)

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
        self.port = []
        self.angles = []
        self.pins = []
        self.actions = []
        self.values =0
        self.temp_varibal= []

        ##########angles from window######################
        self.left_eye = 0
        self.right_e = 0
        self.right_sholder = 0
        self.right_hand = 0
        self.left_hand = 0
        self.left_leg = 0
        self.right_leg = 0
        self.reserved_1 = 0
        self.reserved_2 = 0


        self.lab_ser_1 = ttk.Label(self.master, text='глаз левый ').grid(row=0, column=1)
        self.left_eye = IntVar()
        self.angle_box1=ttk.Entry(self.master, textvariable=self.left_eye ,width=3)
        self.angle_box1.grid(row=1, column=1)



        self.lab_ser_2 = ttk.Label(self.master, text='глаз правый').grid(row=4, column=1)
        self.right_e = IntVar()
        self.angle_box2 = ttk.Entry(self.master,textvariable=self.right_e,width=3)
        self.angle_box2.grid(row=5, column=1)




        self.lab_ser_3 = ttk.Label(self.master, text='плечо правое').grid(row=8, column=1)
        self.right_sholder = IntVar()
        self.angle_box3 = ttk.Entry(self.master,textvariable=self.right_sholder, width=3)
        self.angle_box3.grid(row=9, column=1)



        self.lab_ser_4 = ttk.Label(self.master, text='рука правая').grid(row=0, column=2)
        self.right_hand = IntVar()
        self.angle_box4 = ttk.Entry(self.master,textvariable=self.right_hand, width=3)
        self.angle_box4.grid(row=1, column=2)





        self.lab_ser_5 = ttk.Label(self.master, text='рука левая').grid(row=4, column=2)
        self.left_hand = IntVar()
        self.angle_box5 = ttk.Entry(self.master,textvariable=self.left_hand, width=3)
        self.angle_box5.grid(row=5, column=2)


        self.lab_ser_6 = ttk.Label(self.master, text='нога левая').grid(row=8, column=2)
        self.left_leg= IntVar()
        self.angle_box6 = ttk.Entry(self.master,textvariable=self.left_leg, width=3)
        self.angle_box6.grid(row=9, column=2)


        self.lab_ser_7 = ttk.Label(self.master, text='нога правая ').grid(row=0, column=3)
        self.right_leg = IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.right_leg, width=3)
        self.angle_box7.grid(row=1, column=3)

        self.lab_ser_8 = ttk.Label(self.master, text='reserved_1 ').grid(row=4, column=3)
        self.reserved_1 = IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.reserved_1, width=3)
        self.angle_box7.grid(row=5, column=3)

        self.lab_ser_9 = ttk.Label(self.master, text='reserved_2 ').grid(row=8, column=3)
        self.reserved_2= IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.reserved_2, width=3)
        self.angle_box7.grid(row=9, column=3)




        self.button = ttk.Button(self.master, text='pull value', command=self.time_lapse)
        self.button.grid(row=13,column=2)

        # self.preview = ttk.Button(self.master,text = "preview",command =self.just_one_action2).grid(row = 14 ,column=2)

        self.add_position = ttk.Button(self.master, text="add action",command = self.time_lapse).grid(row=16, column=2)

        self.time_scale = ttk.Scale(self.master, orient='horizontal', length=450, from_=0.00, to=4.50,
                                    command=self.print_values)
        self.time_scale.grid(row=22, column=2)


        self.port =StringVar()
        self.port_selector = ttk.Combobox(self.master, textvariable=self.port)
        self.port_selector.grid(row=11, column=3)

    # self.but_init = ttk.Button(self.master,text = 'initports',command = self.arduino_port_indit).grid(row= 12,column=2)



   ################################main func with angles########################


    def refresh_angle(self):
        self.left_eye.get()



    def arduino_port_indit(self):
        self.ports = list(serial.tools.list_ports.comports())
        self.port_selector = ttk.Combobox(self.master, values=self.ports)
    '''
    #mind this stuff after    
    def just_one_action(self):
        dict(self.pins)
        self.pin_init()
        self.take_angle_box_answer()
        for angl in self.angles:
            for pin in self.pins:
                self.actions.append(str(pin)+'.write(%d)'%angl)
                print(self.actions)
    '''

    def take_angle(self):
        pass





    def word_limiter(self):
        pass

    def close_windows(self):
        self.master.destroy()
    '''
    def take(self):
        x = self.servo_box3.get()
        print(x)

    def take_left_e(self):
        left_e_angle = self.angle_box1.get()
        print('left angle is ' + left_e_angle)

    def take_right_e(self):
        right_e_angle = self.angle_box2.get()
        print('right eye angle is ' + right_e_angle)

    def take_right_sholder(self):
        right_sholder_angle = self.angle_box3.get()
        print('right sholder angle is ' + right_sholder_angle)

    def take_right_hand(self):
        right_hand_angle = self.angle_box4.get()
        print('right hand angle is ' + right_hand_angle)

    def take_left_hand(self):
        left_hand_angle = self.angle_box5.get()
        print('left hand angle is ' + left_hand_angle)

    def take_right_leg(self):
        right_leg_angle = self.angle_box6.get()
        print('right leg angle is ' + right_leg_angle)

    def take_left_leg(self):
        left_leg_angle = self.angle_box6.get()
        print('left leg angle is ' + left_leg_angle)

    '''
    def pin_init(self):
        # init pin ardiuno

        port = '/dev/ttyACM0'
        port2 = '/dev/ttyUSB0'
        board = pyfirmata.Arduino(port2)

        self.right_e = board.get_pin('d:8:s')
        self.left_e = board.get_pin('d:9:s')
        self.sholder_right = board.get_pin('d:7:s')
        self.right_hand = board.get_pin('d:3:s')
        self.left_hand = board.get_pin('d:6:s')
        self.left_leg = board.get_pin('d:4:s')
        self.right_leg = board.get_pin('d:5:s')

        
        self.pins.append(right_e)
        self.pins.append(left_e)
        self.pins.append(sholder_right)
        self.pins.append(right_hand)
        self.pins.append(left_hand)
        self.pins.append(left_leg)
        self.pins.append(right_leg)


    '''take each angle'''

    def time_lapse(self):  # time scaling
        # temp variable is value for  obtain time scale and save first number is time, after value of angles

        self.take_angle_box_answer()
        self.temp_varibal.append(float(self.values))  # add double list for time
        self.temp_varibal.append(self.left_eye.get())
        self.temp_varibal.append(self.right_e.get())
        self.temp_varibal.append(self.right_sholder.get())
        self.temp_varibal.append(self.right_hand.get())
        self.temp_varibal.append(self.left_hand.get())
        self.temp_varibal.append(self.left_leg.get())
        self.temp_varibal.append(self.right_leg.get())
        self.temp_varibal.append(self.reserved_1.get())
        self.temp_varibal.append(self.reserved_2.get())


        print(self.temp_varibal)

    def print_values(self, value):
        self.values = value










    def take_angle_box_answer(self):

        '''ANSWERS BY PULL VALUE'''

        pass





def main():
    root = tk.Tk()
    root.title("SERVO_M")

    app = Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()