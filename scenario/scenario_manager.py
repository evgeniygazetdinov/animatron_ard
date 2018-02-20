
#!/usr/bin/python3
# -*- coding: utf-8 -*-



from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication,
                             QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import pygame
from tinytag import TinyTag

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.paused = False
        self.playing = False
        self.vol = 0
        self.sec= 00
        self.minutes =00
        self.primary_time =''
        self.final_time = ''
    def initUI(self):




        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        sld.valueChanged[int].connect(self.get_value)

        loud = QSlider(Qt.Vertical,self)
        loud.setGeometry(150,20,200,40)
        loud.valueChanged[int].connect(self.loudness)

        pybutton = QPushButton('get value', self)
        pybutton.clicked.connect(self.get_value)
        pybutton.resize(100, 32)
        pybutton.move(10, 10)

        start_music = QPushButton('start music',self)
        start_music.clicked.connect(self.play_music)
        start_music.move(10,70)
        start_music.resize(100,32)

        stop_music = QPushButton('stop_music',self)
        stop_music.clicked.connect(self.pause)
        stop_music.move(10,100)
        stop_music.resize(100,32)

        time_label = QLabel('',self)
        time_label.move(220,20)


        self.label = QLabel(self)
        self.label.setGeometry(160, 40, 180, 30)



        self.setGeometry(600, 500, 280, 170)
        self.setWindowTitle('status')
        self.show()

    def changeValue(self, value):

        if value == 0:
            print(value)
            return self.value

        elif value > 0 and value <=1000:
            print(value)
            return self.value


    def get_value(self):
        pass





###########################MUSIC##############################
    def play_music(self):
        self.playing = True
        self.conventer_durability()
        self.doAction()
        pygame.init()
        pygame.mixer.music.load('/home/qbc/Downloads/c.mp3')
        pygame.mixer.music.play(0)



    def pause(self):
        pygame.init()
        if  self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.paused = True
            pygame.mixer.music.pause()


    def loudness(self,vol):
        pygame.init()
        pygame.mixer.music.set_volume()




    def atEnd(self):
        endOfSong = pygame.event.get(SONGEND)
        if (endOfSong):
            return True
        return False

##################################################################


    def conventer_durability(self):
        tag = TinyTag.get('/home/qbc/Downloads/c.mp3')
        value = tag.duration
        minutes = str(int((value// 60) % 60))
        sec = str(int(value % 60))
        print(minutes+':'+sec)


    def getPosition(self):
        if self.playing == True:
            position = pygame.mixer.music.get_pos()
            return self.conventer_durability(position)
        return "00:00"

    def doAction(self):
        if self.play_music:
            while True:
                self.sec -= 1
                print(self.sec)
                if self.sec == 60:
                    self.minutes -= 1





###################################################################










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
'''