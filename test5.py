from tkinter import IntVar
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename,asksaveasfile
from tkinter import messagebox
import threading
import sqlite3
from subprocess import call, PIPE, Popen
import shutil
from sketchbooks.SW.run_servo import compiling
from db_input import *
from tkinter.messagebox import showinfo
from default_positon import Default_position
from player import Player
from example4 import EXAMPLER
from variables import Variables
from collections import OrderedDict
import time

class SERVO_MAN(Variables,Player,Default_position,
                new_base,EXAMPLER,):
    def __init__(self, master):
        self.master = master
        self.master.geometry('950x380')
        self.frame = tk.Frame(self.master)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.master.title('серво менеджер')
        ####################
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
        self.duration =180
        self.count=0
        self.counter =0
        self.min_interval = 0
        #################VALUES FOR TIMER##################################
        self.timer = False
        self.default_seconds = 0
        self.timer_seconds = self.default_seconds
        self.sql_time = []
        self.time = 0
        #########values for changer default databases#########
        self.current_name_db = ''
        self.path = ''
        ######## additional loop variables ##################
        self.loop_sec_entry1 = 0
        self.loop_sec_entry2 = 0
        self.loop_sec_entry3 = 0
        self.loop_sec_entry4 = 0
        self.loop_sec_entry5 = 0
        self.loop_sec_entry6 = 0
        self.loop_sec_entry7 = 0
        self.loop_sec_entry8 = 0
        self.loop_sec_entry9 = 0

        self.loop_variable  = IntVar()
        self.loop_variable1 = IntVar()
        self.loop_variable2 = IntVar()
        self.loop_variable3 = IntVar()
        self.loop_variable4 = IntVar()
        self.loop_variable5 = IntVar()
        self.loop_variable6 = IntVar()
        self.loop_variable7 = IntVar()
        self.loop_variable8 = IntVar()

        self.loop1 = False
        self.loop2 = False
        self.loop3 = False
        self.loop4 = False
        self.loop5 = False
        self.loop6 = False
        self.loop7 = False
        self.loop8 = False
        self.loop9 = False

        self.loop_speed1=0
        self.loop_speed2=0
        self.loop_speed3=0
        self.loop_speed4=0
        self.loop_speed5=0
        self.loop_speed6=0
        self.loop_speed7=0
        self.loop_speed8=0
        self.loop_speed9=0

        self.loop_int_entry1 = 0
        self.loop_int_entry2 = 0
        self.loop_int_entry3 = 0
        self.loop_int_entry4 = 0
        self.loop_int_entry5 = 0
        self.loop_int_entry6 = 0
        self.loop_int_entry7 = 0
        self.loop_int_entry8 = 0
        self.loop_int_entry9 = 0
        # variable for independent servos interval

        self.interval_1 = 0
        self.interval_2 = 0
        self.interval_3 = 0
        self.interval_4 = 0
        self.interval_5 = 0
        self.interval_6 = 0
        self.interval_7 = 0
        self.interval_8 = 0
        self.interval_9 = 0

        # variable for choose loop on or off
        self.loop_variator = IntVar()
        self.loop_variator1 = IntVar()
        self.loop_variator2 = IntVar()
        self.loop_variator3 = IntVar()
        self.loop_variator4 = IntVar()
        self.loop_variator5 = IntVar()
        self.loop_variator6 = IntVar()
        self.loop_variator7 = IntVar()
        self.loop_variator8 = IntVar()

        self.primary_time = 0
        self.final_time = 0
        self.interval_fall_down = 0
        self.count=0
        ############# constants for dictionaries###############
        self.LEFT_EYE = 0
        self.RIGHT_EYE = 1
        self.RIGHT_SHOLDER = 2
        self.RIGHT_HAND = 3
        self.LEFT_HAND = 4
        self.LEFT_LEG = 5
        self.RIGHT_LEG = 6
        self.RESERVED_1 = 7
        self.RESERVED_2 = 8
        ####################
        self.model =[]
        self.intervals_for_model = []
        self.GRAND_MODEL = {}
        ####################

        self.lab_ser_1 = ttk.Label(self.master,
                                   text='глаз левый ').grid(row=1, column=1)
        self.left_eye = IntVar()
        self.angle_box1 = ttk.Entry(self.master,
                                    width=3,
                                    textvariable=self.left_eye)
        self.angle_box1.grid(row=2, column=0,columnspan =2)
        self.loop_l_e = ttk.Checkbutton(self.master,
                                        onvalue =1,offvalue  =1,
                                        command = lambda: self.loop_enabler(self.loop_variator,self.loop,self.loop_sec_entry1,2,0,4,self.loop_variable)).grid(row=1, column=2, padx=10)

        self.lab_ser_2 = ttk.Label(self.master,text='глаз правый').grid(row=4, column=1)
        self.right_e = IntVar()
        self.angle_box2 = ttk.Entry(self.master, textvariable=self.right_e, width=3)
        self.angle_box2.grid(row=5, column=1)
        self.loop_r_e = ttk.Checkbutton(self.master,
                                        command = lambda: self.loop_enabler(self.loop_variator1,self.loop2,self.loop_sec_entry2,5,0,2,self.loop_variable1)
                                        ).grid(row=4, column=2, padx=10)

        self.lab_ser_3 = ttk.Label(self.master, text='плечо левое').grid(row=8, column=1)
        self.right_sholder = IntVar()
        self.angle_box3 = ttk.Entry(self.master,
                                    textvariable=self.right_sholder, width=3)
        self.angle_box3.grid(row=9, column=0,columnspan =2)
        self.loop_r_s = ttk.Checkbutton(self.master,command = lambda: self.loop_enabler(self.loop_variator2,self.loop3,self.loop_sec_entry3,9,0,2,self.loop_variable2)).grid(row=8, column=2, padx=10)

        self.lab_ser_4 = ttk.Label(self.master, text='плечо правое').grid(row=1, column=3, )
        self.right_hand = IntVar()
        self.angle_box4 = ttk.Entry(self.master, textvariable=self.right_hand, width=3)
        self.angle_box4.grid(row=2, column=2,columnspan = 3 )
        self.loop_r_h = ttk.Checkbutton(self.master,command = lambda: self.loop_enabler(self.loop_variator3,self.loop4,self.loop_sec_entry4,2,2,4,self.loop_variable3)).grid(row=1, column=4, padx=10)

        self.lab_ser_5 = ttk.Label(self.master, text='рука левая').grid(row=4, column=3)
        self.left_hand = IntVar()
        self.angle_box5 = ttk.Entry(self.master, textvariable=self.left_hand, width=3)
        self.angle_box5.grid(row=5, column=3)
        self.loop_r_l = ttk.Checkbutton(self.master,command = lambda: self.loop_enabler(self.loop_variator4,self.loop5,self.loop_sec_entry5,5,2,4,self.loop_variable4)).grid(row=4, column=4, padx=10)

        self.lab_ser_6 = ttk.Label(self.master, text='рука правая').grid(row=8, column=3)
        self.left_leg = IntVar()
        self.angle_box6 = ttk.Entry(self.master, textvariable=self.left_leg, width=3)
        self.angle_box6.grid(row=9, column=3)
        self.loop_l_l = ttk.Checkbutton(self.master,command = lambda: self.loop_enabler(self.loop_variator5,self.loop6,self.loop_sec_entry6,9,2,4,self.loop_variable5)).grid(row=8, column=4, padx=10)

        self.lab_ser_7 = ttk.Label(self.master, text='нога правая ').grid(row=1, column=6)
        self.right_leg = IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.right_leg, width=3)
        self.angle_box7.grid(row=2, column=6)

        self.loop_r_l = ttk.Checkbutton(self.master,command = lambda: self.loop_enabler(self.loop_variator6,self.loop7,self.loop_sec_entry7,2,7,4,self.loop_variable6)).grid(row=1, column=7, padx=10)

        self.lab_ser_8 = ttk.Label(self.master, text='нога левая ').grid(row=4, column=6)
        self.reserved_1 = IntVar()
        self.angle_box8 = ttk.Entry(self.master, textvariable=self.reserved_1, width=3)
        self.angle_box8.grid(row=5, column=6)
        self.loop_res = ttk.Checkbutton(self.master,command = lambda: self.loop_enabler(self.loop_variator7,self.loop8,self.loop_sec_entry8,5,7,4,self.loop_variable7)).grid(row=4, column=7, padx=10)

        self.lab_ser_9 = ttk.Label(self.master, text='жопа ').grid(row=8, column=6)
        self.reserved_2 = IntVar()
        self.angle_box9 = ttk.Entry(self.master, textvariable=self.reserved_2, width=3)
        self.angle_box9.grid(row=9, column=6)
        self.loop_res2 = ttk.Checkbutton(self.master,command = lambda: self.loop_enabler(self.loop_variator8,self.loop9,self.loop_sec_entry8,5,7,4,self.loop_variable7)
                                        ).grid(row=8, column=7, padx=10)

        self.play_butt = ttk.Button(self.master,
                                    text='проиграть',command= self.some_play
                                    ).grid(row=12, column=3)
        self.button = ttk.Button(self.master,
                                 text='записать позиции',
                                 command = self.count_clicks)
        self.button.grid(row=10, column=3,columnspan=1)
        self.button_save = ttk.Button(self.master,
                            text='сохранить сценарий ',
                            command= self.saving_changes
                            ).grid(row=11, column=3)
        # self.new = ttk.Button(
        #     self.master,
        #     text="новый сценарий",
        #     command=self.new_data
        #    ).grid(row=1, column=8)
        # self.window_curr = ttk.Button(self.master,
        #                               text="выбрать сценарий",
        #                               command =self.choose_db).grid(row=1, column=9)

        self.window_db = Listbox(self.master, width=28, height=8)
        self.window_db.grid(row=2, column=8,rowspan=8,columnspan=10)
        self.request_butt = ttk.Label(self.master, text='текущая база данных: не выбрана',)
        self.request_butt .grid(row=10, column=8,columnspan=4)
        self.current_music = ttk.Label(self.master, text='музыка : --  ',)
        self.choose_current_music =ttk.Button(self.master,
                                              text = 'музыка',
                                              command = self.add_music_return_duration)
        self.show_last_values = Listbox(self.master, width=62, height=5,selectmode=tk.MULTIPLE)
        self.show_last_values_label = Label(text = 'последние значения').grid(row=16, column=8,columnspan=15)
        self.show_last_values.grid(row=17 ,column=8,rowspan=8,columnspan=12)


        self.choose_current_music.grid(row=11, column=9,columnspan=15)

        self.current_music.grid(row=11, column=7,columnspan=3,)

        self.sql_model_upload = ttk.Button(self.master,
                                           text = 'проиграть существующий сценарий',
                                           command = self._play_exist_sql)
        self.clean_model_button = ttk.Button(self.master,text = 'удалить',
                                             command =self.clean_model).grid(row=10, column=3,columnspan=6)
        self.sql_model_upload.grid(row=12, column=8,columnspan=15)

        self.label_time = ttk.Label(self.master)
        self.label_time.grid(row=11, column=3)

        self.time_scale = ttk.Scale(self.master,
                                    orient='horizontal',
                                    length=400,
                                    from_=0, to=self.duration,command = self.printime)
        self.time_scale.grid(row=19, column=0, columnspan=8)
        # digit near "время"
        self.time_label = ttk.Label(self.master, text="время").grid(row=17, column=1)

        self.time_digit = ttk.Label(self.master)
        self.time_digit.grid(row=17, column=0,rowspan=1,columnspan=7)

        self.speed_label = ttk.Label(self.master, text="cкорость").grid(row=22, column=1)

        self.speed_digit = ttk.Label(self.master)
        self.speed_digit.grid(row=22, column=1,columnspan=6)

        self.speed_slider = ttk.Scale(self.master,
                                      orient="horizontal",
                                      length=100,
                                      from_=0, to=200,command=self.printspeed
                                      )
        self.speed_slider.grid(row=23, column=0,columnspan=3)
        # bigin speed state 50
        self.speed_slider.set(50)
        self.stop = False
        # stand default position for servo before start







    # draw func
        # self.draw_entrys(self.interval_1,self.loop_int_entry1,2,2,0)



        self.interval_1 = IntVar()
        self.loop_int_entry1 = ttk.Entry(self.master,textvariable = self.interval_1,width =2,)
        self.loop_int_entry1.grid(row =2,column =2 ,padx = 0)
        self.interval_2 = IntVar()
        self.loop_int_entry2 = ttk.Entry(self.master,textvariable = self.interval_2,width =2)
        self.loop_int_entry2.grid(row =5,column =2 ,padx = 0)
        self.interval_3 = IntVar()
        self.loop_int_entry3 = ttk.Entry(self.master,textvariable = self.interval_3,width =2)
        self.loop_int_entry3.grid(row =9,column =2 ,padx = 0)
        self.interval_4 = IntVar()
        self.loop_int_entry4 = ttk.Entry(self.master,textvariable = self.interval_4,width =2)
        self.loop_int_entry4.grid(row =2,column =4 ,padx = 0)
        self.interval_5 = IntVar()
        self.loop_int_entry5 = ttk.Entry(self.master,textvariable = self.interval_5,width =2)
        self.loop_int_entry5.grid(row =5,column =4 ,padx = 0)
        self.interval_6 = IntVar()
        self.loop_int_entry6 = ttk.Entry(self.master,textvariable = self.interval_6,width =2)
        self.loop_int_entry6.grid(row =9,column =4 ,padx = 0)
        self.interval_7 = IntVar()
        self.loop_int_entry7 = ttk.Entry(self.master,textvariable = self.interval_7,width =2)
        self.loop_int_entry7.grid(row =2,column =7 ,padx = 0)
        self.interval_8 = IntVar()
        self.loop_int_entry8 = ttk.Entry(self.master,textvariable = self.interval_8,width =2)
        self.loop_int_entry8.grid(row =5,column =7 ,padx = 0)
        self.interval_9 = IntVar()
        self.loop_int_entry9 = ttk.Entry(self.master,textvariable = self.interval_9,width =2)
        self.loop_int_entry9.grid(row =9,column =7 ,padx = 0)
        self.default()


    def draw_label(self,name,text,row,column):
        name = ttk.Label(self.master,text='{}'.format(text))
        name.grid(row=row, column=column)
    def draw_buttons(self,name,text,row,column,columnspan):
        name = ttk.Label(self.master, text='{}'.format(text))
        name.grid(row=row, column=column,columnspan=columnspan)
    def one_more_window(self,variable,name,row,column,pad):
        # if checkbut will be pushed draw new window new first window
        variable = IntVar()
        name = ttk.Entry(self.master, textvariable=variable, width=3)
        name.grid(row = row, column = column, padx = pad)

    # def draw_entrys(self,*args):
    #     self.one_more_window(variable1,name1,row1,column1,pad1,)
    #     self.one_more_window(variable2,name2,row2,column2,pad2,)
    #     self.one_more_window(variable3,name3,row3,column3,pad3,)
    #     self.one_more_window(variable4,name4,row4,column4,pad4,)
    #     self.one_more_window(variable5,name5,row5,column5,pad5,)
    #     self.one_more_window(variable6,name6,row6,column6,pad6,)
    #     self.one_more_window(variable7,name7,row7,column7,pad7,)
    #     self.one_more_window(variable8,name8,row8,column8,pad8,)
    #     self.one_more_window(variable9,name9,row9,column9,pad9,)






    def loop_activator(self,loop_entr,loop,loop_window):
        # this stuff must be indicating = if on or not on loop
        if loop_entr.get() == 1:
            loop = True
            print('True')
        if loop_entr.get() == 0:
            loop = False
            print('False')

            loop_entr.set(1)

        else:
            loop_entr.set(0)

    def loop_enabler(self,loop_entr,loop,loop_window,row,column,columnspan,variable):
        # action with active loop shit
        # draw addional window
        # and stand flag appropriate window True
        self.loop_activator(loop_entr,loop,loop_window)
        loop_window = ttk.Entry(self.master, textvariable=variable, width=2)
        loop_window.grid(row = row,column =column,columnspan =columnspan)
        if loop_entr.get() == 1:
            loop_window.configure(state =DISABLED)
            print('fafa')


    def default(self):
        # position before start state here
        # left_eye
        self.stand_default_position(self.angle_box1,0,270)
        #right_eye
        self.stand_default_position(self.angle_box2,0,270)
        # left sholder
        self.stand_default_position(self.angle_box3,100,270)
        # right sholder
        self.stand_default_position(self.angle_box4,100,270)
        # hand left
        self.stand_default_position(self.angle_box5,130,270)
        # hand right
        self.stand_default_position(self.angle_box6,30,270)
        # leg right
        self.stand_default_position(self.angle_box7,30,90)
        # leg left
        self.stand_default_position(self.angle_box8,30,90)
        # ass
        self.stand_default_position(self.angle_box9,0,270)
        self.stand_min_interval(self.interval_1)
        self.stand_min_interval(self.interval_2)
        self.stand_min_interval(self.interval_3)
        self.stand_min_interval(self.interval_4)
        self.stand_min_interval(self.interval_5)
        self.stand_min_interval(self.interval_6)
        self.stand_min_interval(self.interval_7)
        self.stand_min_interval(self.interval_8)
        self.stand_min_interval(self.interval_9)
        self.stand_min_interval(self.loop_variator)
        self.stand_min_interval(self.loop_variator1)
        self.stand_min_interval(self.loop_variator2)
        self.stand_min_interval(self.loop_variator3)
        self.stand_min_interval(self.loop_variator4)
        self.stand_min_interval(self.loop_variator5)
        self.stand_min_interval(self.loop_variator6)
        self.stand_min_interval(self.loop_variator7)
        self.stand_min_interval(self.loop_variator8)
    def printspeed(self, val):
        # define for speed
        speed = round(float(val))
        # change label to define speed
        self.speed_digit.configure(text=round(speed))

    def printime(self, val):
        # define for TIME
        time = self.time_scale.get()
        m = time // 60
        s = time - m * 60
        self.time_digit.configure(text='%02d:%02d' % (m, s))

        # HERE USING STOPPER
        self.stopper()


    def adden_key_to_model(self):
        #obtain values from windows
        model = [self.left_eye.get(), round(self.speed_slider.get()),
        self.right_e.get(),round(self.speed_slider.get()),
        self.right_sholder.get(),round(self.speed_slider.get()),
        self.right_hand.get(),round(self.speed_slider.get()),
        self.left_hand.get(),round(self.speed_slider.get()),
        self.left_leg.get(),round(self.speed_slider.get()),
        self.right_leg.get(),round(self.speed_slider.get()),
        self.reserved_1.get(),round(self.speed_slider.get()),
        self.reserved_2.get(),round(self.speed_slider.get())]
        self.show_dict(model)
        return model
    def adden_intervals_for_keys(self):
        # list for divider angle
        intervals_for_model = []
        intervals_for_model.append(self.loop_int_entry1.get())
        intervals_for_model.append(self.loop_int_entry2.get())
        intervals_for_model.append(self.loop_int_entry3.get())
        intervals_for_model.append(self.loop_int_entry4.get())
        intervals_for_model.append(self.loop_int_entry5.get())
        intervals_for_model.append(self.loop_int_entry6.get())
        intervals_for_model.append(self.loop_int_entry7.get())
        intervals_for_model.append(self.loop_int_entry8.get())
        intervals_for_model.append(self.loop_int_entry9.get())
        return intervals_for_model


    def calculate_scale(self,
                        time_begin,time_over,fi,):
        # create execution from 2 serifs with minimal
        self.min_interval = self.find_minimal_interval(self.adden_intervals_for_keys())
        execute = self.generateNumber(time_begin,time_over,int(self.min_interval),fi)
        print(str(execute)+'this is beginer execute')
        return execute



    def count_clicks(self):
        self.count+= 1

        # TODO ALL REFACTOR BELLOW
        if self.count == 1:
            self.primary_time = round(self.time_scale.get())
            messagebox.showinfo("значение", "записано первое значение")
            self.first_p = self.adden_key_to_model()
            print('write first key')
        if self.count == 2:
            self.count = 0
            messagebox.showinfo("значение", "записано второе значение ")
            final_time = round(self.time_scale.get())
            # this part breaks down stopper
            self.final_time = final_time
            print('write sevcond key')
            self.second_p = self.adden_key_to_model()
            interval_servo = self.adden_intervals_for_keys()
            execute = self.calculate_scale(self.primary_time,final_time,self.first_p)
            print(execute)
            print("THIS IS EXECUTEEXECUTEEXECUTEEXECUTEEXECUTEEXECUTE"+str(len(execute)))
            final_execute = self.servo_on_min_interval(execute,self.first_p,self.second_p
                                                        ,0,2,4,6,8,10,12,14,16,
                                                        self.second_p[0],self.second_p[2],self.second_p[4],
                                                        self.second_p[6],self.second_p[8],self.second_p[10],
                                                        self.second_p[12],self.second_p[14],self.second_p[16],
                                                        self.min_interval,
                                                        interval_servo[0],interval_servo[1],interval_servo[2],
                                                        interval_servo[3],interval_servo[4],interval_servo[5],
                                                        interval_servo[6],interval_servo[7],interval_servo[8],
                                                        self.first_p[0],self.first_p[2],self.first_p[4],
                                                        self.first_p[6],self.first_p[8],self.first_p[10],
                                                        self.first_p[12],self.first_p[14],self.first_p[16],
                                                        len(execute))



            self.get_more_position(final_execute)
            self.show_dict(self.GRAND_MODEL)
            print(str(self.GRAND_MODEL)+"this is GRAND MODEL!!!!")






    def stopper(self):
        self.stop = True
        if round(self.time_scale.get())<=self.final_time:

            self.time_scale.set(self.final_time)

    def get_more_position(self,new):
            self.GRAND_MODEL = {**self.GRAND_MODEL,**new}




    def saving_changes(self):
        self.write_changes_to_sql('template.db')
        # name = filedialog.asksaveasfile()
        # print(name)
        # self.write_changes_to_sql(name)

    def write_changes_to_sql(self,path):
        # init new window
        self.create_template()
        conn = sqlite3.connect(path)  # here will be avalibale data bases
        cursor = conn.cursor()
        for key,values in self.model.items():
            cursor.execute(""" insert into`servo_0`values( % d)""" % (values[0]))
            cursor.execute(""" insert into`servo_1`values( % d)""" % (values[2]))
            cursor.execute(""" insert into`servo_2`values( % d)""" % (values[4]))
            cursor.execute(""" insert into`servo_3`values( % d)""" % (values[6]))
            cursor.execute(""" insert into`servo_4`values( % d)""" % (values[8]))
            cursor.execute(""" insert into`servo_5`values( % d)""" % (values[10]))
            cursor.execute(""" insert into`servo_6`values( % d)""" % (values[12]))
            cursor.execute(""" insert into`servo_7`values( % d)""" % (values[14]))
            cursor.execute(""" insert into`servo_8`values( % d)""" % (values[16]))
            cursor.execute(""" insert into`speed_0`values( % d)""" % (values[1]))
            cursor.execute(""" insert into`speed_1`values( % d)""" % (values[3]))
            cursor.execute(""" insert into`speed_2`values( % d)""" % (values[5]))
            cursor.execute(""" insert into`speed_3`values( % d)""" % (values[7]))
            cursor.execute(""" insert into`speed_4`values( % d)""" % (values[9]))
            cursor.execute(""" insert into`speed_5`values( % d)""" % (values[11]))
            cursor.execute(""" insert into`speed_6`values( % d)""" % (values[13]))
            cursor.execute(""" insert into`speed_7`values( % d)""" % (values[15]))
            cursor.execute(""" insert into`speed_8`values( % d)""" % (values[17]))
            cursor.execute(""" insert into`time`values( % s)""" % (key))
            print(key,values)

        conn.commit()
        self.write_to_h(path)


    def _play_exist_sql(self):

        for key,values in self.model.items():
            del self.model[key]
            del self.model[values]
            print(self.model)
        self.choose_db()
        self.write_to_h()
    def clean_model(self):
        try:

            self.show_last_values.delete(0,END)
            self.model.popitem()
            print(self.model)

        except KeyError:
            messagebox.showwarning('ошибка','нет значений')
            self.stop = False
        self.show_dict()
    def show_dict(self,input):
        # separate model for display on listb
        self.model.append(input)
        base=str(self.model).split('],')
        self.show_last_values.insert(END,base[-1])



    def choose_db(self):
        fname = askopenfilename(filetypes=(("scenario", "*.db"),
                                           ("All files", "*.*")))

        base=fname.split('/')
        self.current_name_db = fname
        self.window_db.insert(END, base[-1] + '\n')
        messagebox.Message('')
        messagebox.showinfo("база данных выбрана",

                                           "     текущая база данных  \n "
                                           "     {}".format(base[-1]))
        self.path = self.current_name_db

        self.request_butt.config(text='текущая база данных : {}'.format(base[-1]))




    def new_data(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = new_base(self.newWindow)

    def add_music_return_duration(self):

        # mp3 shit using methods from player)and add some label with music information
        name= self.add()
        self.duration = int(self.conventer_durability())
        minutes = self.duration / 60
        sec = self.duration % 60

        self.time_scale.configure(to=self.duration)
        self.duration_label = tk.Label(self.master,text = "%2.2d:%2.2d"%(minutes,sec)).grid(column=8,row =12)

        self.name_song_label = tk.Label(self.master,text = name).grid(column=9,row =12)
        self.current_music.configure(text='музыка :выбрана')
        self.current_music.grid(row=11, column=6,columnspan=20)
        self.choose_current_music.grid(row=11, column=9,columnspan=10)
        self.sql_model_upload.grid(row=13, column=8,columnspan=15)

    def some_play(self):
        t1.start()
        t1 = threading.Thread(target=compiling)

def main():
    root = tk.Tk()
    root.title("SERVO_M")

    app = SERVO_MAN(root)
    root.mainloop()


# self.new = ttk.Button(
#     self.master,
#     text="новый сценарий",
#     command=self.new_data
#    ).grid(row=1, column=8)
# self.window_curr = ttk.Button(self.master,
#                               text="выбрать сценарий",
#                               command =self.choose_db).grid(row=1, column=9)

if __name__ == '__main__':
    main()
