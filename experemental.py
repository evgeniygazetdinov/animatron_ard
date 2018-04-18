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
from loop_shit import Looper
from collections import OrderedDict


class SERVO_MAN(Player,Default_position,new_base,Looper):
    def __init__(self, master):
        self.master = master
        self.master.geometry('950x380')
        self.frame = tk.Frame(self.master)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.master.title('серво менеджер')

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
        self.model = {}
        ####################

        self.lab_ser_1 = ttk.Label(self.master,
                                   text='глаз левый ').grid(row=1, column=1)
        self.left_eye = IntVar()
        self.angle_box1 = ttk.Entry(self.master,
                                    width=3,
                                    textvariable=self.left_eye)
        self.angle_box1.grid(row=2, column=1)
        self.loop_l_e = ttk.Radiobutton(self.master,
                                        command=self.check_loop
                                        ).grid(row=1, column=2, padx=10)

        self.lab_ser_2 = ttk.Label(self.master,text='глаз правый').grid(row=4, column=1)
        self.right_e = IntVar()
        self.angle_box2 = ttk.Entry(self.master, textvariable=self.right_e, width=3)
        self.angle_box2.grid(row=5, column=1)
        self.loop_r_e = ttk.Radiobutton(self.master,
                                        command=self.check_loop2).grid(row=4, column=2, padx=10)

        self.lab_ser_3 = ttk.Label(self.master, text='плечо левое').grid(row=8, column=1)
        self.right_sholder = IntVar()
        self.angle_box3 = ttk.Entry(self.master,
                                    textvariable=self.right_sholder, width=3)
        self.angle_box3.grid(row=9, column=1)
        self.loop_r_s = ttk.Radiobutton(self.master,command=self.check_loop3
                                        ).grid(row=8, column=2, padx=10)

        self.lab_ser_4 = ttk.Label(self.master, text='плечо правое').grid(row=1, column=3, )
        self.right_hand = IntVar()
        self.angle_box4 = ttk.Entry(self.master, textvariable=self.right_hand, width=3)
        self.angle_box4.grid(row=2, column=3)
        self.loop_r_h = ttk.Radiobutton(self.master,command=self.check_loop4
                                        ).grid(row=1, column=4, padx=10)

        self.lab_ser_5 = ttk.Label(self.master, text='рука левая').grid(row=4, column=3)
        self.left_hand = IntVar()
        self.angle_box5 = ttk.Entry(self.master, textvariable=self.left_hand, width=3)
        self.angle_box5.grid(row=5, column=3)
        self.loop_r_l = ttk.Radiobutton(self.master,command=self.check_loop5
                                        ).grid(row=4, column=4, padx=10)

        self.lab_ser_6 = ttk.Label(self.master, text='рука правая').grid(row=8, column=3)
        self.left_leg = IntVar()
        self.angle_box6 = ttk.Entry(self.master, textvariable=self.left_leg, width=3)
        self.angle_box6.grid(row=9, column=3)
        self.loop_l_l = ttk.Radiobutton(self.master,command=self.check_loop6
                                        ).grid(row=8, column=4, padx=10)

        self.lab_ser_7 = ttk.Label(self.master, text='нога правая ').grid(row=1, column=6)
        self.right_leg = IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.right_leg, width=3)
        self.angle_box7.grid(row=2, column=6)

        self.loop_r_l = ttk.Radiobutton(self.master,command=self.check_loop7
                                        ).grid(row=1, column=7, padx=10)

        self.lab_ser_8 = ttk.Label(self.master, text='нога левая ').grid(row=4, column=6)
        self.reserved_1 = IntVar()
        self.angle_box8 = ttk.Entry(self.master, textvariable=self.reserved_1, width=3)
        self.angle_box8.grid(row=5, column=6)
        self.loop_res = ttk.Radiobutton(self.master,command=self.check_loop8
                                        ).grid(row=4, column=7, padx=10)

        self.lab_ser_9 = ttk.Label(self.master, text='жопа ').grid(row=8, column=6)
        self.reserved_2 = IntVar()
        self.angle_box9 = ttk.Entry(self.master, textvariable=self.reserved_2, width=3)
        self.angle_box9.grid(row=9, column=6)
        self.loop_res2 = ttk.Radiobutton(self.master,command=self.check_loop9
                                        ).grid(row=8, column=7, padx=10)

        self.play_butt = ttk.Button(self.master,
                                    text='проиграть',command= self.some_play
                                    ).grid(row=12, column=3)
        self.button = ttk.Button(self.master,
                                 text='записать позиции',
                                 command = self.most_bigger_loop_ever)
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
                                    from_=0, to=self.duration,
                                    command = self.printime
                                    )
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

        # stand default position for servo before start
        self.default()
        self.loop1 = False
        self.loop2 = False
        self.loop3 = False
        self.loop4 = False
        self.loop5 = False
        self.loop6 = False
        self.loop7 = False
        self.loop8 = False
        self.loop9 = False

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


    def some_play(self):
        t1 = threading.Thread(target=compiling)
        t1.start()

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



        print(self.model)

    def save(self):
        self.most_bigger_loop_ever()


    # loop func write loop from 4 values taken this from loop window.
    #  and will do check for comparison values with exist to model 9 window and 18 checks
    # very important saving sequense on second comparison.there obtain from second window values
    def sp_finder(self):
        self.sp_variable_loop1 = round(self.speed_slider.get())
        self.sp_variable_loop2 = round(self.speed_slider.get())
        self.sp_variable_loop3 = round(self.speed_slider.get())
        self.sp_variable_loop4 = round(self.speed_slider.get())
        self.sp_variable_loop5 = round(self.speed_slider.get())
        self.sp_variable_loop6 = round(self.speed_slider.get())
        self.sp_variable_loop7 = round(self.speed_slider.get())
        self.sp_variable_loop8 = round(self.speed_slider.get())
        self.sp_variable_loop9 = round(self.speed_slider.get())
        if self.loop1 == True:
            self.sp_variable_loop1 = self.loop_speed1.get()
        if self.loop2 == True:
            self.sp_variable_loop2 = self.loop_speed2.get()
        if self.loop3 == True:
            self.sp_variable_loop3 = self.loop_speed3.get()
        if self.loop4== True:
            self.sp_variable_loop4 = self.loop_speed4.get()
        if self.loop5 == True:
            self.sp_variable_loop5 = self.loop_speed5.get()
        if self.loop6 == True:
            self.sp_variable_loop6 = self.loop_speed6.get()
        if self.loop7 == True:
            self.sp_variable_loop7 = self.loop_speed7.get()
        if self.loop8 == True:
            self.sp_variable_loop8 = self.loop_speed8.get()
        if self.loop9 == True:
            self.sp_variable_loop9 = self.loop_speed9.get()




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


    def write_to_h(self,path):

        # take all from data base
        conn = sqlite3.connect(path)  # here will be avaliable data bases
        cursor = conn.cursor()
        # time
        try:
            cursor.execute("SELECT * FROM `time` order by  `time_pos` ")
            sql_time = cursor.fetchall()
        except:
            messagebox.showwarning("ОШИБКА", "НЕ ВЫБРАНА БАЗА ДАНННЫХ\n"
                                             "создайте новую или выберите\n"
                                             "cуществующую")
        finally:
            # servo_1
            cursor.execute("SELECT * FROM `servo_0`  ")
            sql_servo_1 = cursor.fetchall()
            # servo_2
            cursor.execute("SELECT * FROM `servo_1`  ")
            sql_servo_2 = cursor.fetchall()
            # servo_3
            cursor.execute("SELECT * FROM `servo_2` ")
            sql_servo_3 = cursor.fetchall()
            # servo_4
            cursor.execute("SELECT * FROM `servo_3`  ")
            sql_servo_4 = cursor.fetchall()
            # servo_5
            cursor.execute("SELECT * FROM `servo_4`  ")
            sql_servo_5 = cursor.fetchall()
            # servo_6
            cursor.execute("SELECT * FROM `servo_5`  ")
            sql_servo_6 = cursor.fetchall()
            # servo_7
            cursor.execute("SELECT * FROM `servo_6`  ")
            sql_servo_7 = cursor.fetchall()
            # servo_8
            cursor.execute("SELECT * FROM `servo_7`  ")
            sql_servo_8 = cursor.fetchall()
            # servo_9
            cursor.execute("SELECT * FROM `servo_8`  ")
            sql_servo_9 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_0` order by  `speed0_pos` ")
            sql_speed1 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_1` order by  `speed1_pos` ")
            sql_speed2 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_2` order by  `speed2_pos` ")
            sql_speed3 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_3` order by  `speed3_pos` ")
            sql_speed4 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_4` order by  `speed4_pos` ")
            sql_speed5 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_5` order by  `speed5_pos` ")
            sql_speed6 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_6` order by  `speed6_pos` ")
            sql_speed7 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_7` order by  `speed7_pos` ")
            sql_speed8 = cursor.fetchall()

            cursor.execute("SELECT * FROM `speed_8` order by  `speed8_pos` ")
            sql_speed9 = cursor.fetchall()


            # servo_1
            with open('template.h', 'w') as file:
                file.writelines('int time_play={};\n'.format(self.duration*1000))
                file.writelines('int speed_row[] = {')
                file.writelines(str(sql_speed1))
                file.writelines('};\n')
                file.writelines('int speed_row2[] = {')
                file.writelines(str(sql_speed2))
                file.writelines('};\n')
                file.writelines('int speed_row3[] = {')
                file.writelines(str(sql_speed3))
                file.writelines('};\n')
                file.writelines('int speed_row4[] = {')
                file.writelines(str(sql_speed4))
                file.writelines('};\n')
                file.writelines('int speed_row5[] = {')
                file.writelines(str(sql_speed5))
                file.writelines('};\n')
                file.writelines('int speed_row6[] = {')
                file.writelines(str(sql_speed6))
                file.writelines('};\n')
                file.writelines('int speed_row7[] = {')
                file.writelines(str(sql_speed7))
                file.writelines('};\n')
                file.writelines('int speed_row8[] = {')
                file.writelines(str(sql_speed8))
                file.writelines('};\n')
                file.writelines('int speed_row9[] = {')
                file.writelines(str(sql_speed9))
                file.writelines('};\n')
                file.writelines('int LEyeArray[][] = {')
                file.writelines(str(sql_servo_1))
                file.writelines('};\n')
                file.writelines('int REyeArray[] = {')
                file.writelines(str(sql_servo_2))
                file.writelines('};\n')
                file.writelines('int LArmArray[] = {')
                file.writelines(str(sql_servo_3))
                file.writelines('};\n')
                file.writelines('int RArmArray[] = {')
                file.writelines(str(sql_servo_4))
                file.writelines('};\n')
                file.writelines('int LhandArray[] = {')
                file.writelines(str(sql_servo_5))
                file.writelines('};\n')
                file.writelines('int RhandArray[] = {')
                file.writelines(str(sql_servo_6))
                file.writelines('};\n')
                file.writelines('int LLegArray[] = {')
                file.writelines(str(sql_servo_7))
                file.writelines('};\n')
                file.writelines('int RLegArray[] = {')
                file.writelines(str(sql_servo_8))
                file.writelines('};\n')
                file.writelines('int AssArray[] = {')
                file.writelines(str(sql_servo_9))
                file.writelines('};\n')
                file.writelines('unsigned long KeyArray[] = {')
                file.writelines(str(sql_time))
                file.writelines('};\n')
            print('write to file')
            self.clear_strings()

            call(('rm template.db '),shell =True)

    def clear_strings(self):
        # clean by rubish
        f = open('template.h', 'r')
        o = open('VAL.h', 'w')
        print('writing1')
        while 1:
            line = f.readline()
            if not line: break
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace(',,', ',')
            line = line.replace("''", '0')
            line = line.replace('[][]', '[]')
            line = line.replace('{[]}', '{}')
            line = line.replace('{[', '{')
            line = line.replace(']}', '}')
            line = line.replace(')]};', '')
            o.write(line)
        o.close()
        call('rm template.h', shell=True)
        try:

            shutil.move("/home/qbc/PycharmProjects/ard/VAL.h",
                        "/usr/share/arduino/hardware/arduino/cores/arduino/VAL.h")
        except:
            shutil.move("/home/qbc/PycharmProjects/ard/sketchbooks/SW/VAL.h",
                        "/home/qbc/PycharmProjects/ard/VAL.h")
            shutil.move("/home/qbc/PycharmProjects/ard/VAL.h",
                        "/usr/share/arduino/hardware/arduino/cores/arduino/VAL.h")

        print('writing2')


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

def main():
    root = tk.Tk()
    root.title("SERVO_M")

    app = SERVO_MAN(root)
    root.mainloop()


if __name__ == '__main__':
    main()
