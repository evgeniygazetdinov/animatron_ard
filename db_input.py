from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
import sqlite3


class new_base:

    def __init__(self,master):


        #####variables######

        self.db_name=''

        self.master = master
        self.master.geometry('300x70')
        self.master.title('создать новый сценарий')
        self.frame = tk.Frame(self.master)
        self.db_name = StringVar()
        self.name_label = ttk.Label(self.master,text= 'имя сценария')
        self.name_label.grid(row=1,column=1,sticky = 'w',padx=10 )
        self.data_base = ttk.Entry(self.master,textvariable = self.db_name,width=30)
        self.data_base.grid(row=3,column=1,sticky="w",padx=10)

        self.ok_b = ttk.Button(self.master,text = 'создать',command = self.create_newdb)
        self.ok_b.grid(row =4 ,column =1,sticky='w',padx=30,pady=5)
        self.cancell_but = ttk.Button(self.master,text = 'отмена',command = self.cancell)
        self.cancell_but.grid(row=4,column=1,padx=120,pady=5)



    def create_newdb(self):
        call('mkdir scenario', shell=True)
        path = '{}.db'.format(self.db_name.get())
        con = sqlite3.connect(path)
        cursor = con.cursor()
        for i in range(9):
            cursor.execute(
                'CREATE TABLE  servo_{} (servo{}_pos integer );'.format(i,i))
            cursor.execute(
                'CREATE TABLE  speed_{} (speed{}_pos integer );'.format(i, i))

        cursor.execute(
            'CREATE TABLE  time (time_pos integer );')
        con.commit()
        call('mv {}.db /home/qbc/PycharmProjects/ard/scenario/'.format(self.db_name.get()),shell =True)
        db='{}'.format(self.db_name.get())
        messagebox.showinfo("база данных", " База создана выберите ее \n "
                                           "    из папки SCENARIO\n"
                                           "       затем НАЖАТЬ   \n "
                                           " ВЫБРАТЬ СЦЕНАРИЙ ")
    def cancell(self):
        self.master.destroy()
