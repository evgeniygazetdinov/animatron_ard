from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pyfirmata
import pygame
from tinytag import TinyTag




class Player:

    def __init__(self, master):
        ##########
        self.position = 0
        self.playing = False
        self.paused = False


        ##########
        self.pr_time = 0
        self.fin_time = 0
        self.min = 0
        self.sec = 0
        self.values = 1
        self.info = ''
        self.duration = 1
        ##########
    def play_music(self):
        self.playing = True
        pygame.init()
        pygame.mixer.music.load(self.song)
        print('music')
        # pygame.mixer.music.set_volume(0)  # set volume on zero before play
        # pygame.mixer.music.play(-1, 0.0)
        # if self.playing == True:
        #     self.p_bar.config(mode='determinate', maximum=self.fin_time, value=1)
        #     self.p_bar.start(1000)
        #     self.conventer_durability()
        #     self._on_scale()

    def _on_scale(self):
        # initialize time track
        time = int(pygame.mixer.music.get_pos() / 1000)
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        self.m_time.configure(text="%2.2d:%2.2d" % (m, s))
        self.duration = pygame.mixer.music.get_pos() / 1000
        self.frame.after(1000, self._on_scale)


    def update_timeslider(self, _=None):
        time = (pygame.mixer.music.get_pos() / 1000)
        print(time)
        self.scaleposition.set(time)
        self.after(1000, self.update_timeslider)

    def position_seek(self,val):
        pass


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
        tag = TinyTag.get(self.song)
        self.duration =  tag.duration
        self.fin_time = tag.duration
        self.fin_time = int(self.fin_time)
        minutes = self.fin_time / 60
        sec = self.fin_time % 60
        time =[round(minutes),':',round(sec)]
        return time

    def add(self):
        file = askopenfilename(filetypes=(("music", "*.mp3"),
                                            ("All files", "*.*")),
                                            initialdir = '~/PycharmProjects/ard/')

        name = file.split('/')
          # turn user's opened filenames into tuple
        self.song =file
        return name[-1]
