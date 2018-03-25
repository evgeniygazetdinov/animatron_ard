from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import threading
import sqlite3
from subprocess import call, PIPE, Popen
import shutil
from sketchbooks.SW.run_servo import compiling
from db_input import *
from tkinter.messagebox import showinfo


class Demo2:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x400')
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
        #################VALUES FOR TIMER##################################
        self.timer = False
        self.default_seconds = 0
        self.timer_seconds = self.default_seconds
        self.sql_time = []
        self.sql_servo_1 = 0
        self.sql_servo_2 = 0
        self.sql_servo_3 = 0
        self.sql_servo_4 = 0
        self.sql_servo_5 = 0
        self.sql_servo_6 = 0
        self.sql_servo_7 = 0
        self.sql_servo_8 = 0
        self.sql_servo_9 = 0
        self.sql_speed = 0
        self.speed = 0
        self.time = 0
        #########values for changer default databases#########
        self.current_name_db = ''
        self.path = 'position.dms'
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
        self.loop_int_entry1 = 0
        self.loop_int_entry2 = 0
        self.loop_int_entry3 = 0
        self.loop_int_entry4 = 0
        self.loop_int_entry5 = 0
        self.loop_int_entry6 = 0
        self.loop_int_entry7 = 0
        self.loop_int_entry8 = 0
        self.loop_int_entry9 = 0

        self.lab_ser_1 = ttk.Label(self.master, text='глаз левый ').grid(row=1, column=1)
        self.left_eye = IntVar()
        self.angle_box1 = ttk.Entry(self.master, textvariable=self.left_eye, width=3)
        self.angle_box1.grid(row=2, column=1)
        self.loop_l_e = ttk.Checkbutton(self.master, command=self.check_loop_1).grid(row=1, column=2, padx=10)

        self.lab_ser_2 = ttk.Label(self.master, text='глаз правый').grid(row=4, column=1)
        self.right_e = IntVar()
        self.angle_box2 = ttk.Entry(self.master, textvariable=self.right_e, width=3)
        self.angle_box2.grid(row=5, column=1)
        self.loop_r_e = ttk.Checkbutton(self.master, command=self.check_loop_2).grid(row=4, column=2, padx=10)

        self.lab_ser_3 = ttk.Label(self.master, text='плечо правое').grid(row=8, column=1)
        self.right_sholder = IntVar()
        self.angle_box3 = ttk.Entry(self.master, textvariable=self.right_sholder, width=3)
        self.angle_box3.grid(row=9, column=1)
        self.loop_r_s = ttk.Checkbutton(self.master, command=self.check_loop_3).grid(row=8, column=2, padx=10)

        self.lab_ser_4 = ttk.Label(self.master, text='рука правая').grid(row=1, column=3, )
        self.right_hand = IntVar()
        self.angle_box4 = ttk.Entry(self.master, textvariable=self.right_hand, width=3)
        self.angle_box4.grid(row=2, column=3)
        self.loop_r_h = ttk.Checkbutton(self.master, command=self.check_loop_4).grid(row=1, column=4, padx=10)

        self.lab_ser_5 = ttk.Label(self.master, text='рука левая').grid(row=4, column=3)
        self.left_hand = IntVar()
        self.angle_box5 = ttk.Entry(self.master, textvariable=self.left_hand, width=3)
        self.angle_box5.grid(row=5, column=3)
        self.loop_r_l = ttk.Checkbutton(self.master, command=self.check_loop_5).grid(row=4, column=4, padx=10)

        self.lab_ser_6 = ttk.Label(self.master, text='нога левая').grid(row=8, column=3)
        self.left_leg = IntVar()
        self.angle_box6 = ttk.Entry(self.master, textvariable=self.left_leg, width=3)
        self.angle_box6.grid(row=9, column=3)
        self.loop_l_l = ttk.Checkbutton(self.master, command=self.check_loop_6).grid(row=8, column=4, padx=10)

        self.lab_ser_7 = ttk.Label(self.master, text='нога правая ').grid(row=1, column=6)
        self.right_leg = IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.right_leg, width=3)
        self.angle_box7.grid(row=2, column=6)

        self.loop_r_l = ttk.Checkbutton(self.master, command=self.check_loop_6).grid(row=1, column=7, padx=10)

        self.lab_ser_8 = ttk.Label(self.master, text='reserved_1 ').grid(row=4, column=6)
        self.reserved_1 = IntVar()
        self.angle_box8 = ttk.Entry(self.master, textvariable=self.reserved_1, width=3)
        self.angle_box8.grid(row=5, column=6)
        self.loop_res = ttk.Checkbutton(self.master, command=self.check_loop_6).grid(row=4, column=7, padx=10)

        self.lab_ser_9 = ttk.Label(self.master, text='reserved_2 ').grid(row=8, column=6)
        self.reserved_2 = IntVar()
        self.angle_box9 = ttk.Entry(self.master, textvariable=self.reserved_2, width=3)
        self.angle_box9.grid(row=9, column=6)
        self.loop_res2 = ttk.Checkbutton(self.master, command=self.check_loop_6).grid(row=8, column=7, padx=10)

        self.play_butt = ttk.Button(self.master,
                                    text='проиграть',
                                    command=self.some_play).grid(row=12, column=3)
        self.button = ttk.Button(self.master,
                                 text='записать позиции',
                                 command=self.write_position)
        self.button.grid(row=13, column=3)

        self.new = ttk.Button(self.master, text="новый сценарий", command=self.new_data).grid(row=1, column=8)
        self.window_curr = ttk.Button(self.master,
                                      text="выбрать сценарий",
                                      command=self.choose_db).grid(row=1, column=9)

        self.window_db = Listbox(self.master, width=28, height=10)
        self.window_db.grid(row=2, column=8,rowspan=8,columnspan=10)
        self.request_butt = ttk.Button(self.master, text='выбрать текущий', command=self.current_db).grid(row=10, column=8)
        self.label_time = ttk.Label(self.master)
        self.label_time.grid(row=11, column=3)

        self.time_scale = ttk.Scale(self.master, orient='horizontal', length=400, from_=0, to=180,
                                    command=self.printime)
        self.time_scale.grid(row=19, column=0, columnspan=8)
        # digit near "время"
        self.time_label = ttk.Label(self.master, text="время").grid(row=17, column=1)
        self.time_digit = ttk.Label(self.master)
        self.time_digit.grid(row=17, column=0,rowspan=1,columnspan=7)
        self.speed_label = ttk.Label(self.master, text="cкорость").grid(row=22, column=1)
        self.speed_digit = ttk.Label(self.master)
        self.speed_digit.grid(row=22, column=1,columnspan=6)
        self.speed_slider = ttk.Scale(self.master, orient="horizontal", length=100, from_=0, to=100, command=self.prinw)
        self.speed_slider.grid(row=23, column=0,columnspan=3)

    def prinw(self, val):
        # define for speed
        self.speed = round(float(val))
        # change label to define speed
        self.speed_digit.configure(text=round(self.speed))

    def printime(self, val):
        # define for speed
        self.time = round(float(val))
        m = self.time // 60
        s = self.time - m * 60
        self.time_digit.configure(text='%02d:%02d' % (m, s))

    def choose_db(self):
        fname = askopenfilename(filetypes=(("scenario", "*.db"),
                                           ("All files", "*.*")))
        print(fname[-6:-1])
        self.current_name_db = fname
        self.window_db.insert(END, fname[-25:-1] + '\n')

    def current_db(self):
        self.path = self.current_name_db

    def write_position(self):
        # on sql
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.executescript("""
         insert into `time` values (%d)
        """ % (round(self.time_scale.get() * 1000)))  # time
        cursor.executescript("""
        insert into `speed` values (%d)
        """ % (round(self.speed_slider.get())))  # speed
        cursor.executescript("""
        insert into `servo_2` values (%d)
        """ % (self.left_eye.get()))  # servo_1
        cursor.executescript("""
        insert into `servo_1` values (%d)
        """ % (self.right_e.get()))  # servo_2
        cursor.executescript("""
        insert into `servo_3` values (%d)
        """ % (self.right_sholder.get()))  # servo_3
        cursor.executescript("""
        insert into `servo_4` values (%d)
        """ % (self.left_hand.get()))  # servo_4
        cursor.executescript("""
        insert into `servo_5` values (%d)
        """ % (self.right_hand.get()))  # servo_5
        cursor.executescript("""
        insert into `servo_6` values (%d)
        """ % (self.right_leg.get()))  # servo_6
        cursor.executescript("""
        insert into `servo_7` values (%d)
        """ % (self.left_leg.get()))  # servo_7
        cursor.executescript("""
        insert into `servo_8` values (%d)
        """ % (self.reserved_1.get()))  # servo_8
        cursor.executescript("""
        insert into `servo_9` values (%d)
        """ % (self.reserved_2.get()))  # servo_9
        self.write_to_h()

    def clear_strings(self):
        # clean by rubish
        f = open('template.h', 'r')
        o = open('VAL.h', 'w')
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
        # move VAL.h with values from sql to arduino library:******************
        shutil.move("/home/qbc/PycharmProjects/ard/VAL.h", "/usr/share/arduino/hardware/arduino/cores/arduino/VAL.h")
        # call('rm VAL.h',shell =True)

    def write_to_h(self):
        # take all from data base
        conn = sqlite3.connect(self.path)  # here will be avalibale data bases
        cursor = conn.cursor()
        # time
        cursor.execute("SELECT * FROM `time` order by  `time_pos` ")
        self.sql_time = cursor.fetchall()
        # servo_1
        cursor.execute("SELECT * FROM `servo_1`  ")
        self.sql_servo_1 = cursor.fetchall()
        # servo_2
        cursor.execute("SELECT * FROM `servo_2`  ")
        self.sql_servo_2 = cursor.fetchall()
        # servo_3
        cursor.execute("SELECT * FROM `servo_3` ")
        self.sql_servo_3 = cursor.fetchall()
        # servo_4
        cursor.execute("SELECT * FROM `servo_4`  ")
        self.sql_servo_4 = cursor.fetchall()
        # servo_5
        cursor.execute("SELECT * FROM `servo_5`  ")
        self.sql_servo_5 = cursor.fetchall()
        # servo_6
        cursor.execute("SELECT * FROM `servo_6`  ")
        self.sql_servo_6 = cursor.fetchall()
        # servo_7
        cursor.execute("SELECT * FROM `servo_7`  ")
        self.sql_servo_7 = cursor.fetchall()
        # servo_8
        cursor.execute("SELECT * FROM `servo_8`  ")
        self.sql_servo_8 = cursor.fetchall()
        # servo_9
        cursor.execute("SELECT * FROM `servo_9`  ")
        self.sql_servo_9 = cursor.fetchall()
        cursor.execute("SELECT * FROM `speed` order by  `speed_pos` ")
        self.sql_speed = cursor.fetchall()
        # servo_1

        with open('template.h', 'w') as file:
            file.writelines('int time_play=1;\n')
            file.writelines('int speed_row[] = {')
            file.writelines(str(self.sql_speed))
            file.writelines('};\n')
            file.writelines('int LEyeArray[][] = {')
            file.writelines(str(self.sql_servo_1))
            file.writelines('};\n')
            file.writelines('int REyeArray[] = {')
            file.writelines(str(self.sql_servo_2))
            file.writelines('};\n')
            file.writelines('int LArmArray[] = {')
            file.writelines(str(self.sql_servo_3))
            file.writelines('};\n')
            file.writelines('int RArmArray[] = {')
            file.writelines(str(self.sql_servo_4))
            file.writelines('};\n')
            file.writelines('int LhandArray[] = {')
            file.writelines(str(self.sql_servo_5))
            file.writelines('};\n')
            file.writelines('int RhandArray[] = {')
            file.writelines(str(self.sql_servo_6))
            file.writelines('};\n')
            file.writelines('int LLegArray[] = {')
            file.writelines(str(self.sql_servo_7))
            file.writelines('};\n')
            file.writelines('int RLegArray[] = {')
            file.writelines(str(self.sql_servo_8))
            file.writelines('};\n')
            file.writelines('int AssArray[] = {')
            file.writelines(str(self.sql_servo_9))
            file.writelines('};\n')
            file.writelines('unsigned long KeyArray[] = {')
            file.writelines(str(self.sql_time))
            file.writelines('};\n')
        self.clear_strings()

    def create_new(self):
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        for i in range(9):
            cursor.execute(
                'CREATE TABLE  servo_{} (servo{}_pos integer );'.format(i,i))
        cursor.execute(
            'CREATE TABLE  speed (speed_pos integer );')
        cursor.execute(
            'CREATE TABLE  time (time_pos integer );')
        # self.deleteall()

    def deleteall(self):
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        for i in range(9):
            cursor.execute('DELETE FROM  servo_{} '.format(i))
        cursor.execute('DELETE FROM  speed ')
        cursor.execute('DELETE FROM  time ')
        conn.commit()

    def some_play(self):
        t1 = threading.Thread(target=compiling)
        t1.start()

    # window for create new data bases(described in db_input)
    def new_data(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = new_base(self.newWindow)

    # each func for each window

    def check_loop_1(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл1')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.left_eye = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.left_eye, width=4)
        loop_le1.insert(0, 'угол')
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry1 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry1, width=4)
        loop_le2.grid(row=2, column=2)
        loop_le2.insert(0, 'угол')
        self.loop_int_entry1 = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry1, width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)
        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)
        self.angle_box1.state(["disabled"])
        if cancell_but:
            self.angle_box1.state(["!disabled"])

    def check_loop_2(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл_2')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.right_eye = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_eye, width=4)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry2 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry2, width=4)
        loop_le2.grid(row=2, column=2)
        self.loop_int_entry2 = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry2, width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)

    def check_loop_3(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.right_sholder = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_sholder, width=4)
        loop_le1.grid(row=1, column=2)

        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le2.grid(row=2, column=2)

        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)

    def check_loop_4(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл4')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.right_hand = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_hand, width=4)
        loop_le1.grid(row=1, column=2)

        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le2.grid(row=2, column=2)

        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)

    def check_loop_5(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл5')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.left_hand = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.left_hand, width=4)
        loop_le1.grid(row=1, column=2)

        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le2.grid(row=2, column=2)

        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)

    def check_loop_6(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл6')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.left_leg = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.left_leg, width=4)
        loop_le1.grid(row=1, column=2)

        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le2.grid(row=2, column=2)

        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)

    def check_loop_7(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл7')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.right_leg = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_leg, width=4)
        loop_le1.grid(row=1, column=2)

        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le2.grid(row=2, column=2)

        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)

    def check_loop_8(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл8')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.reserved_1 = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.reserved_1, width=4)
        loop_le1.grid(row=1, column=2)

        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le2.grid(row=2, column=2)

        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)

    def check_loop_9(self):
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('150x120')
        newonfWindow.title('цикл')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.reserved_2 = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.reserved_2, width=4)
        loop_le1.grid(row=1, column=2)

        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le2.grid(row=2, column=2)

        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable='e', width=4)
        loop_le_int.grid(row=3, column=2)

        ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
        ok_b.grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=1)

    def loop_to_sql(self):
        for i in range(begin_time, final_time, self.loop_int_entry1.get()):
            if i % 2 == 0:
                conn = sqlite3.connect('/home/qbc/PycharmProjects/ard/scenario/d.db')
                cursor = conn.cursor()
                cursor.executescript("""
                 insert into `time` values (%d)
                """ % (i))  # time
                cursor.executescript("""
                insert into `servo_1` values (%d)
                """ % (self.left_eye.get()))  # speed
            if i % 2 != 0:
                conn = sqlite3.connect('/home/qbc/PycharmProjects/ard/scenario/d.db')
                cursor = conn.cursor()
                cursor.executescript("""
                 insert into `time` values (%d)
                """ % (i))  # time
                cursor.executescript("""
                insert into `servo_1` values (%d)
                """ % (self.loop_sec_entry1()))  # speed

    #
    #     #
    #
    #     # if self.check_loop_4():
    #     #     pass
    #     # if self.check_loop_5():
    #     #     pass
    #     # if self.check_loop_6():
    #     #     pass
    #     # if self.check_loop_7():
    #     #     pass
    #     # if self.check_loop_8():
    #     #     pass
    #     # if self.check_loop_9():
    #     #     pass
