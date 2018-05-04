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
from example2 import EXAMPLER
from variables import Variables
from collections import OrderedDict


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
        # here unpack values from additional files  ===>variables
        self.values()
        # TODO change this shit on func
        self.loop_l_e = ttk.Checkbutton(self.master,
                                        command = lambda: self.one_more_window(self.loop_sec_entry1,self.loop_l_e,2,2,5),
                                        offvalue = tk.DISABLED,onvalue = tk.NORMAL
                                        ).grid(row=1, column=2, padx=10)
        self.loop_r_e = ttk.Checkbutton(self.master,
                                        command = lambda: self.one_more_window(self.loop_sec_entry2,self.loop_r_e,5,2,5),
                                        offvalue = tk.DISABLED,onvalue = tk.NORMAL
                                        ).grid(row=4, column=2, padx=10)
        self.loop_r_s = ttk.Checkbutton(self.master).grid(row=8, column=2, padx=10)
        self.loop_r_h = ttk.Checkbutton(self.master).grid(row=1, column=4, padx=10)
        self.loop_r_l = ttk.Checkbutton(self.master).grid(row=4, column=4, padx=10)
        self.loop_l_l = ttk.Checkbutton(self.master).grid(row=8, column=4, padx=10)
        self.loop_r_l = ttk.Checkbutton(self.master).grid(row=1, column=7, padx=10)
        self.loop_res = ttk.Checkbutton(self.master).grid(row=4, column=7, padx=10)
        self.loop_res2 = ttk.Checkbutton(self.master).grid(row=8, column=7, padx=10)
        self.play_butt = ttk.Button(self.master,text='проиграть',).grid(row=12, column=3)
        self.button = ttk.Button(self.master, text='записать позиции')
        self.button.grid(row=10, column=3,columnspan=1)
        self.button_save = ttk.Button(self.master,text='сохранить сценарий ').grid(row=11, column=3)
        self.choose_current_music =ttk.Button(self.master,text = 'музыка',)
        self.choose_current_music.grid(row=11, column=9,columnspan=15)
        self.sql_model_upload = ttk.Button(self.master,text = 'проиграть существующий сценарий',)
        self.clean_model_button = ttk.Button(self.master,text = 'удалить',).grid(row=10, column=3,columnspan=6)
        self.sql_model_upload.grid(row=12, column=8,columnspan=15)
        self.speed_slider = ttk.Scale(self.master,
                                      orient="horizontal",
                                      length=100,
                                      from_=0, to=200,command=self.printspeed
                                      )
        self.time_scale = ttk.Scale(self.master,orient='horizontal',length=400,from_=0, to=self.duration,
                                    command = self.printime)
        self.time_scale.grid(row=19, column=0, columnspan=8)
        # digit near "время"


        self.window_db = Listbox(self.master, width=28, height=8)
        self.window_db.grid(row=2, column=8,rowspan=8,columnspan=10)
        self.speed_slider.grid(row=23, column=0,columnspan=3)
        # bigin speed state 50
        self.speed_slider.set(50)
        self.show_last_values = Listbox(self.master, width=62, height=5,selectmode=tk.MULTIPLE)
        self.show_last_values.grid(row=17 ,column=8,rowspan=8,columnspan=12)
        self.request_butt = ttk.Label(self.master, text='текущая база данных: не выбрана',)
        self.request_butt.grid(row=10, column=8,columnspan=4)
        self.current_music = ttk.Label(self.master, text='музыка : --  ',)
        self.current_music.grid(row=11, column=7,columnspan=3,)
        self.time_label = ttk.Label(self.master, text="время").grid(row=17, column=1)
        self.time_digit = ttk.Label(self.master)
        self.time_digit.grid(row=17, column=0,rowspan=1,columnspan=7)
        self.speed_label = ttk.Label(self.master, text="cкорость").grid(row=22, column=1)
        self.speed_digit = ttk.Label(self.master)
        self.speed_digit.grid(row=22, column=1,columnspan=6)
        self.show_last_values_label = Label(text = 'последние значения').grid(row=16, column=8,columnspan=15)
        self.label_time = ttk.Label(self.master)
        self.label_time.grid(row=11, column=3)

        # create interval_window
        self.draw_entrys(self.loop_int_entry1,self.interval_1,2,2,5,
                            self.loop_int_entry2,self.interval_2,5,2,5,
                            self.loop_int_entry3,self.interval_3,9,2,5,
                            self.loop_int_entry4,self.interval_4,2,4,5,
                            self.loop_int_entry5,self.interval_5,5,4,5,
                            self.loop_int_entry6,self.interval_6,9,4,5,
                            self.loop_int_entry7,self.interval_7,2,7,5,
                            self.loop_int_entry8,self.interval_8,5,7,5,
                            self.loop_int_entry9,self.interval_9,9,7,5,
                            )
        # create servo angle window
        self.draw_entrys(self.left_eye,self.angle_box1,2,1,0,
                        self.right_e,self.angle_box2,5,1,0,
                        self.right_sholder,self.angle_box3,9,1,0,
                        self.right_hand,self.angle_box4,2,3,0,
                        self.left_hand,self.angle_box5,5,3,0,
                        self.left_leg,self.angle_box6,9,3,0,
                        self.right_leg,self.angle_box7,2,6,0,
                        self.reserved_1,self.angle_box8,5,6,0,
                        self.reserved_2,self.angle_box9,9,6,0)

        self.draw_labels(self.lab_ser_1,'глаз левый',1,1,
                         self.lab_ser_2,'глаз правый',4,1,
                         self.lab_ser_3,'плечо левое',8,1,
                         self.lab_ser_4,'плечо правое',1,3,
                         self.lab_ser_5,'рука левая',4,3,
                         self.lab_ser_6,'рука правая',8,3,
                         self.lab_ser_7,'нога правая',1,6,
                         self.lab_ser_8,'нога левая',4,6,
                         self.lab_ser_9,'жопа',8,6)



        # stand default position for servo before start
        # self.default()



    # draw func

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

    def draw_entrys(self,variable1,name1,row1,column1,pad1,
                           variable2,name2,row2,column2,pad2,
                           variable3,name3,row3,column3,pad3,
                           variable4,name4,row4,column4,pad4,
                           variable5,name5,row5,column5,pad5,
                           variable6,name6,row6,column6,pad6,
                           variable7,name7,row7,column7,pad7,
                           variable8,name8,row8,column8,pad8,
                           variable9,name9,row9,column9,pad9):
        self.one_more_window(variable1,name1,row1,column1,pad1,)
        self.one_more_window(variable2,name2,row2,column2,pad2,)
        self.one_more_window(variable3,name3,row3,column3,pad3,)
        self.one_more_window(variable4,name4,row4,column4,pad4,)
        self.one_more_window(variable5,name5,row5,column5,pad5,)
        self.one_more_window(variable6,name6,row6,column6,pad6,)
        self.one_more_window(variable7,name7,row7,column7,pad7,)
        self.one_more_window(variable8,name8,row8,column8,pad8,)
        self.one_more_window(variable9,name9,row9,column9,pad9,)

    def draw_labels(self,name,text,row,column,
                            name1,text1,row1,column1,
                            name2,text2,row2,column2,
                            name3,text3,row3,column3,
                            name4,text4,row4,column4,
                            name5,text5,row5,column5,
                            name6,text6,row6,column6,
                            name7,text7,row7,column7,
                            name8,text9,row9,column9):
        self.draw_label(name,text,row,column)
        self.draw_label(name1,text1,row1,column1)
        self.draw_label(name2,text2,row2,column2)
        self.draw_label(name3,text3,row3,column3)
        self.draw_label(name4,text4,row4,column4)
        self.draw_label(name5,text5,row5,column5)
        self.draw_label(name6,text6,row6,column6)
        self.draw_label(name7,text7,row7,column7)
        self.draw_label(name8,text9,row9,column9)



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



    def stopper(self):
        pass
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
        # self.stopper()


    def adden_key_to_model(self):
        #obtain values from windows
        self.default()
        self.model[round(self.time_scale.get()*1000)] = [
        self.left_eye.get(), round(self.speed_slider.get()),
        self.right_e.get(),round(self.speed_slider.get()),
        self.right_sholder.get(),round(self.speed_slider.get()),
        self.right_hand.get(),round(self.speed_slider.get()),
        self.left_hand.get(),round(self.speed_slider.get()),
        self.left_leg.get(),round(self.speed_slider.get()),
        self.right_leg.get(),round(self.speed_slider.get()),
        self.reserved_1.get(),round(self.speed_slider.get()),
        self.reserved_2.get(),round(self.speed_slider.get()),]
        self.intervals_for_model.append(self.loop_int_entry1.get(),
                                  self.loop_int_entry2.get(),
                                  self.loop_int_entry3.get(),
                                  self.loop_int_entry4.get(),
                                  self.loop_int_entry5.get(),
                                  self.loop_int_entry6.get(),
                                  self.loop_int_entry7.get(),
                                  self.loop_int_entry8.get(),
                                  self.loop_int_entry9.get())


        self.show_dict()
        print(self.model)

    def count_clicks(self, calling_loop):
        self.count+= 1
        # TODO ALL REFACTOR BELLOW
        if self.count == 1:
            self.primary_time = round(self.time_scale.get() * 1000)
            messagebox.showinfo("значение", "записано первое значение")
        if self.count== 2:
            self.count = 0
            messagebox.showinfo("значение", "записано второе значение ")
            self.final_time = round(self.time_scale.get() * 1000)
            calling_loop()  # space for another loops



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
        self.show_dict()
    def show_dict(self):
        # separate model for display on listb
        base=str(self.model).split('],')
        self.show_last_values.insert(END,base[-1])



    def choose_db(self):
        fname = askopenfilename(filetypes=(("scenario", "*.db"),
                                           ("All files", "*.*")),
                                initialdir='~/PycharmProjects/ard/')
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
