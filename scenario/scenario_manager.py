
#!/usr/bin/python3
# -*- coding: utf-8 -*-



from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication,
                             QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import pygame


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.paused = False
        self.playing = False


    def initUI(self):




        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        sld.valueChanged[int].connect(self.get_value)



        pybutton = QPushButton('get value', self)
        pybutton.clicked.connect(self.get_value)
        pybutton.resize(100, 32)
        pybutton.move(10, 10)

        start_music = QPushButton('start music',self)
        start_music.clicked.connect(self.play_music)
        start_music.move(10,70)
        start_music.resize(100,32)

        stop_music = QPushButton('stop_music',self)
        stop_music.clicked.connect(self.stop)
        stop_music.move(10,100)
        stop_music.resize(100,32)

        time_label = QLabel('12',self)
        time_label.move(220,20)


        self.label = QLabel(self)
        self.value =0
        self.label.setPixmap(QPixmap('mute.png'))
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


    def play_music(self):

        self.playing = True
        pygame.init()
        pygame.mixer.music.load('/home/qbc/Downloads/c.mp3')
        pygame.mixer.music.play(0)
        if self.playing == False:
             return pygame.mixer.music.unpause()


    def stop(self):
        self.playing = False
        if  self.stop:
            pygame.mixer.music.pause()



    def getPosition(self):
            value = pygame.mixer.music.get_pos()
            print(value)
            return self.value

    def millisecondConverter(self,value ):
        minutes = str(int((self.value / (1000 * 60)) % 60))
        seconds = str(int(self.value / 1000) % 60)

        if (len(minutes) < 2):
            minutes = "0" + minutes

        if (len(seconds) < 2):
            seconds = "0" + seconds

        er= minutes + ":" + seconds
        return er


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
