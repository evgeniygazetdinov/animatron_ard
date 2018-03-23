import sqlite3
begin_time=20
final_time=100
interval=1
first_value=100
second_value=200


def popup_bonus():
    #on sql

    for i in range(begin_time,final_time,interval):
        if  i % 2  == 0:
            conn = sqlite3.connect('/home/qbc/PycharmProjects/ard/scenario/d.db')
            cursor = conn.cursor()
            cursor.executescript("""
             insert into `time` values (%d)
            """ % (i))#time
            cursor.executescript("""
            insert into `servo_1` values (%d)
            """ % (first_value) )# speed
        if i % 2 != 0:
            print('x')
            conn = sqlite3.connect('/home/qbc/PycharmProjects/ard/scenario/d.db')
            cursor = conn.cursor()
            cursor.executescript("""
             insert into `speed` values (%d)
            """ % (i))  # time
            cursor.executescript("""
            insert into `servo_2` values (%d)
            """ % (second_value))  # speed






popup_bonus()


def check_loop_2(self):
    newonfWindow = tk.Toplevel(self.master)
    newonfWindow.geometry('150x120')
    newonfWindow.title('цикл_2')
    first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
    self.right_eye = IntVar()
    loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_eye, width=4)
    loop_le1.grid(row=1, column=2)

    second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
    loop_le2 = ttk.Entry(newonfWindow, textvariable='e', width=4)
    loop_le2.grid(row=2, column=2)

    interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
    loop_le_int = ttk.Entry(newonfWindow, textvariable='e', width=4)
    loop_le_int.grid(row=3, column=2)

    ok_b = ttk.Button(newonfWindow, text='oк', command=self.loop_to_sql)
    ok_b.grid(row=4, column=1)

    cancell_but = ttk.Button(newonfWindow, text='отмена', command=self.cancell)
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

    cancell_but = ttk.Button(newonfWindow, text='отмена', command=self.cancell)
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

    cancell_but = ttk.Button(newonfWindow, text='отмена', command=self.cancell)
    cancell_but.grid(row=5, column=1)


def check_loop_5(self):
    newonfWindow = tk.Toplevel(self.master)
    newonfWindow.geometry('150x120')
    newonfWindow.title('цикл')
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

    cancell_but = ttk.Button(newonfWindow, text='отмена', command=self.cancell)
    cancell_but.grid(row=5, column=1)


def check_loop_6(self):
    newonfWindow = tk.Toplevel(self.master)
    newonfWindow.geometry('150x120')
    newonfWindow.title('цикл')
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

    cancell_but = ttk.Button(newonfWindow, text='отмена', command=self.cancell)
    cancell_but.grid(row=5, column=1)


def check_loop_7(self):
    newonfWindow = tk.Toplevel(self.master)
    newonfWindow.geometry('150x120')
    newonfWindow.title('цикл')
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

    cancell_but = ttk.Button(newonfWindow, text='отмена', command=self.cancell)
    cancell_but.grid(row=5, column=1)


def check_loop_8(self):
    newonfWindow = tk.Toplevel(self.master)
    newonfWindow.geometry('150x120')
    newonfWindow.title('цикл')
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

    cancell_but = ttk.Button(newonfWindow, text='отмена', command=self.cancell)
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

    cancell_but = ttk.Button(newonfWindow, text='отмена', command=self.cancell)
    cancell_but.grid(row=5, column=1)