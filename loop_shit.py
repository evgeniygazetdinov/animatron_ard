from collections import OrderedDict
from tkinter import IntVar
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename,asksaveasfile
from tkinter.messagebox import showinfo
from tkinter import messagebox






class Looper:
    def __init__(self):
        pass

    def check_loop1(self):
        # using self loop for indicate for for loop servo
        self.loop1 = True
        ###############
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл1')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.left_eye = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.left_eye, width=4)
        self.stand_default_position(loop_le1,0,150)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry1 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry1, width=4)
        self.stand_default_position(loop_le2,0,150)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry1, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed1 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed1, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)



    def check_loop2(self):

        self.loop2 = True
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл2')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.right_e = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_e, width=4)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry2 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry2, width=4)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry2 = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry2, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed2 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed2, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)


    def check_loop3(self):
        self.loop3 = True
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл3')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.right_sholder = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_sholder, width=4)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry3 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry3, width=4)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry3, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed3 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed3, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)

    def check_loop4(self):
        self.loop4 = True
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл4')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.right_hand = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_hand, width=4)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry4 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry4, width=4)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry4, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed4 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed4, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)

    def check_loop5(self):
        self.loop5 = True
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл5')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.left_hand = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.left_hand, width=4)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry5 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry5, width=4)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed5 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed5, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)

    def check_loop6(self):
        self.loop6 = True
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл6')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.left_leg = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.left_leg, width=4)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry6 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry6, width=4)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry6, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed6 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed6, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)

    def check_loop7(self):
        self.loop7 = True
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл7')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.right_leg = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.right_leg, width=4)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry7 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry7, width=4)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry7, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed7 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed7, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)
    def check_loop8(self):
        self.loop8 = True
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл8')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.reserved_1 = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.reserved_1, width=4)
        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry8 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry8, width=4)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry8, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed8 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed8, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)

    def check_loop9(self):
        self.loop9 = True
        newonfWindow = tk.Toplevel(self.master)
        newonfWindow.geometry('200x130')
        newonfWindow.title('цикл9')
        first_label = ttk.Label(newonfWindow, text='первый', borderwidth=3).grid(row=1, column=1)
        self.reserved_2 = IntVar()
        loop_le1 = ttk.Entry(newonfWindow, textvariable=self.reserved_2, width=4)

        loop_le1.grid(row=1, column=2)
        self.loop_sec_entry9 = IntVar()
        second_label = ttk.Label(newonfWindow, text='второй', borderwidth=3).grid(row=2, column=1)
        loop_le2 = ttk.Entry(newonfWindow, textvariable=self.loop_sec_entry9, width=4)
        loop_le2.grid(row=2, column=2)

        self.loop_int_entry = IntVar()
        interval_label = ttk.Label(newonfWindow, text='интервал', borderwidth=3).grid(row=3, column=1)
        loop_le_int = ttk.Entry(newonfWindow, textvariable=self.loop_int_entry8, width=4)
        loop_le_int.grid(row=3, column=2)

        self.loop_speed9 = IntVar()
        loop_speed = ttk.Entry(newonfWindow, textvariable=self.loop_speed9, width=4)
        loop_speed.grid(row=4, column=2)
        speed_label = ttk.Label(newonfWindow, text='cкорость', borderwidth=3).grid(row=4, column=1)

        cancell_but = ttk.Button(newonfWindow, text='отмена', command=lambda: newonfWindow.destroy())
        cancell_but.grid(row=5, column=2)



    def count_clicks(self, calling_loop):
        # before loop count push
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
            self.most_bigger_loop_ever()


    def sp_finder(self):
        # if you using loop define individal loop speed for each servos
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




    def interval_comparer(self):
        # compare all intervat that find most tiny
        if self.loop1 == True:
            self.intrval_finder()
        if self.loop2 == True:
            self.intrval_finder()
        if self.loop3 == True:
            self.intrval_finder()
        if self.loop4== True:
            self.intrval_finder()
        if self.loop5 == True:
            self.intrval_finder()
        if self.loop6 == True:
            self.intrval_finder()
        if self.loop7 == True:
            self.intrval_finder()
        if self.loop8 == True:
            self.intrval_finder()
        if self.loop9 == True:
            self.intrval_finder()

    def intrval_finder(self):
        # find most less interval from all loops
        min_key_binder = min(self.loop_int_entry1.get(),self.loop_int_entry2.get(),
                             self.loop_int_entry3.get(),self.loop_int_entry4.get(),
                             self.loop_int_entry5.get(),self.loop_int_entry6.get(),
                             self.loop_int_entry7.get(),self.loop_int_entry8.get(),
                             self.loop_int_entry9.get())
        return min_key_binder

    def loop_finder(self):
        # if loop radiobutton open begin loop
        if self.loop1 == True:
            self.single_looper(self.loop1,self.final_time,
                               self.loop_int_entry1,1,self.left_eye)
        if self.loop2 == True:
            self.single_looper(self.loop2,self.final_time,
                               self.loop_int_entry2,1,self.right_e)
        if self.loop3 == True:
            self.single_looper(self.loop3,self.final_time,
                               self.loop_int_entry3,1,self.right_sholder)
        if self.loop4== True:
            self.single_looper(self.loop4,self.final_time
                               ,self.loop_int_entry4,1,self.right_hand)
        if self.loop5 == True:
            self.single_looper(self.loop5,self.final_time,
                               self.loop_int_entry5,1,self.left_hand)
        if self.loop6 == True:
            self.single_looper(self.loop6,self.final_time,
                               self.loop_int_entry6,1,self.left_leg)
        if self.loop7 == True:
            self.single_looper(self.loop7,self.final_time,
                               self.loop_int_entry7,1,self.right_leg)
        if self.loop8 == True:
            self.single_looper(self.loop8,self.final_time,
                               self.loop_int_entry8,1,self.reserved_1)
        if self.loop9 == True:
            self.single_looper(self.loop9,self.final_time,
                               self.loop_int_entry9,1,self.reserved_2)

    def single_looper(self,loop,final_time,interval,
                      number_posotion,servo_first_angle
                      ,servo_second_angle):
        # discrube just one loop for one window
        range_index = 0
        if loop == True:
            for i in range(int(primary_time),
                           int(final_time),
                           int(lnterval.get() * 1000)):
                if range_index % 2 == 0:
                    if '{}'.format(primary_time) in self.model:
                        self.sp_finder()
                        current = self.model['{}'.format(primary_time)]
                        current[number_posotion] = servo_first_angle.get()
                        current[1] = self.sp_variable_loop1
                        current[3] = self.sp_variable_loop2
                        current[5] = self.sp_variable_loop3
                        current[7] = self.sp_variable_loop4
                        current[9] = self.sp_variable_loop5
                        current[11] = self.sp_variable_loop6
                        current[13] = self.sp_variable_loop7
                        current[15] = self.sp_variable_loop8
                        current[17] = self.sp_variable_loop9
                    else:
                        self.model['{}'.format(primary_time)] = [
                        self.loop_sec_entry1.get(),self.sp_variable_loop1 ,
                        self.right_e.get(),self.sp_variable_loop2,
                        self.right_sholder.get(),self.sp_variable_loop3,
                        self.right_hand.get(),self.sp_variable_loop4,
                        self.left_hand.get(),self.sp_variable_loop5,
                        self.left_leg.get(),self.sp_variable_loop6,
                        self.right_leg.get(),self.sp_variable_loop7,
                        self.reserved_1.get(),self.sp_variable_loop8,
                        self.reserved_2.get(),self.sp_variable_loop9]
                if range_index % 2 !=  0:
                    if '{}'.format(primary_time) in self.model:
                        self.sp_finder()
                        current = self.model['{}'.format(primary_time)]
                        current[number_posotion] = servo_second_angle.get()
                        current[1] = self.sp_variable_loop1
                        current[3] = self.sp_variable_loop2
                        current[5] = self.sp_variable_loop3
                        current[7] = self.sp_variable_loop4
                        current[9] = self.sp_variable_loop5
                        current[11] = self.sp_variable_loop6
                        current[13] = self.sp_variable_loop7
                        current[15] = self.sp_variable_loop8
                        current[17] = self.sp_variable_loop9
                    else:
                        self.model['{}'.format(primary_time)] = [
                        self.loop_sec_entry1.get(),self.sp_variable_loop1 ,
                        self.right_e.get(),self.sp_variable_loop2,
                        self.right_sholder.get(),self.sp_variable_loop3,
                        self.right_hand.get(),self.sp_variable_loop4,
                        self.left_hand.get(),self.sp_variable_loop5,
                        self.left_leg.get(),self.sp_variable_loop6,
                        self.right_leg.get(),self.sp_variable_loop7,
                        self.reserved_1.get(),self.sp_variable_loop8,
                        self.reserved_2.get(),self.sp_variable_loop9]




    def most_bigger_loop_ever(self):

        # define interval for looop
        min_interval = self.interval_comparer()
        print(min_interval)
        #obtain values from windows

        while self.primary_time != self.final_time:
            # load default position
            self.default()

            self.model[round(self.time_scale.get()*1000+(min_interval*1000))] = [
            self.left_eye.get(), round(self.speed_slider.get()),
            self.right_e.get(),round(self.speed_slider.get()),
            self.right_sholder.get(),round(self.speed_slider.get()),
            self.right_hand.get(),round(self.speed_slider.get()),
            self.left_hand.get(),round(self.speed_slider.get()),
            self.left_leg.get(),round(self.speed_slider.get()),
            self.right_leg.get(),round(self.speed_slider.get()),
            self.reserved_1.get(),round(self.speed_slider.get()),
            self.reserved_2.get(),round(self.speed_slider.get()),]
            self.self.primary_time = self.model.key()
            # if any button loop will be pushed ==> add sequance to model
            self.loop_finder()
            # # plus one if slider dont move for remove usefull repeat values
            # last_values = OrderedDict(self.model)
            # self.counter=+1
            # if (round(self.time_scale.get()*1000)) in sorted(last_values.keys()):
            #     self.counter = round(self.time_scale.get())
            #     self.time_scale.set(min_interval)

        self.show_dict()
