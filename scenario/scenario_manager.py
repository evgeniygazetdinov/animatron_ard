#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication,
                             QPushButton)
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QPixmap
import sys
import pygame
from tinytag import TinyTag
import time


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.paused = False
        self.playing = False
        self.vol = 0
        self.sec = 0
        self.minutes = 0

        self.primary_time = 0
        self.final_time = 0
        self.port1 = '/Users/evgeshakrasava/PycharmProjects/c.mp3'
        self.port2 = '/home/qbc/Downloads/c.mp3'
        self.value = 0

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 150, 700, 600)
       # sld.valueChanged.connect(self.primary_time)

        loud = QSlider(Qt.Vertical, self)
        loud.setGeometry(150, 20, 200, 20)
        loud.valueChanged[int].connect(self.loudness)

        pybutton = QPushButton('get value', self)
        pybutton.clicked.connect(self.get_value)
        pybutton.resize(100, 32)
        pybutton.move(10, 10)

        start_music = QPushButton('start music', self)
        start_music.clicked.connect(self.play_music)
        start_music.move(10, 70)
        start_music.resize(100, 32)

        stop_music = QPushButton('stop_music', self)
        stop_music.clicked.connect(self.pause)
        stop_music.move(10, 100)
        stop_music.resize(100, 32)

        rec_btn = QPushButton('REC',self)
        rec_btn.clicked.connect(self.thread_func)
        rec_btn.move(800,600)



        self.time_label = QLabel('1',self)
        self.time_label.move(220, 20)

        self.label = QLabel(self)
        self.label.setGeometry(160, 40, 180, 30)

        self.setGeometry(400, 400, 1024, 768)
        self.setWindowTitle('scenario-manager')
        self.show()

    def changeValue(self,position):

        if value == 0:
            print(value)
            return self.value

        elif value > 0 and value <= 1000:
            print(value)
            return self.value

    def get_value(self):
        pass

    def thread_func (self):
        pass
    ###########################MUSIC##############################
    def play_music(self):
        self.playing = True
       # self.conventer_durability()
        #self.plus_sec()

        pygame.init()
        pygame.mixer.music.load(self.port2)
        pygame.mixer.music.play(-1)
        self.plus_sec()
        if self.playing == True:
            self.timer.isActive:\
                self.timer.stop()

    def pause(self):
        pygame.init()
        self.playing = False
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.paused = True
            pygame.mixer.music.pause()

    def loudness(self, vol):

        pygame.init()
        pygame.mixer.music.set_volume(self.vol)

    def atEnd(self):
        print(self.timer)



    ##############################time####################################


    def conventer_durability(self):
        tag = TinyTag.get(self.port2)
        self.value = tag.duration

    def sec_to_min(self,time):
        minutes = str(int((time // 60) % 60))
        sec = str(int(time % 60))
        self.minutes = minutes
        self.sec = sec

    def plus_sec(self):
        while self.playing:
            time.sleep(1)
            self.primary_time +=1
            self.sec_to_min(self.primary_time)
            print(self.minutes,self.sec)
            if self.value == self.primary_time:
                break
            if self.playing == False:
                break



###################################################################
'''
 def timerEvent(self, e):
        #global x

        if self.position >= self.sld.valueChanged() :
            self.timer.stop()
            return

        self.step = self.step + 1

    def doAction(self):

        if  self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(1000, self)
            self.btn.setText('Stop')

    def changeValue(self, value):
            self.lbl1.setNum(value)
            self.lbl1.adjustSize()


'''










if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

'''

# here will be begin initizion
class Scenario():
    def __init__(self,*args):
        self.times= times
        self.angle = angle
        self.servo_number = servo_number
        self.port1 ='/dev/ttyACM0'
        self.port2 = '/dev/ttyUSB0'
        self.board = pyfirmata.Arduino()
        self.
    def up(self):
        times(self.time)
        self.servo_number

import threading

def printit():
  threading.Timer(1, printit).start()
  n=0
  n+=1

printit()

'''
