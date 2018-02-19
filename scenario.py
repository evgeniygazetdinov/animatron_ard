
#!/usr/bin/python3
# -*- coding: utf-8 -*-



from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication,
                             QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 200, 30)
        sld.valueChanged[int].connect(self.changeValue)
        sld.valueChanged[int].connect(self.get_value)


        pybutton = QPushButton('get value', self)
        pybutton.clicked.connect(self.get_value)
        pybutton.resize(100, 32)
        pybutton.move(10, 10)

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
        parameter = []
        parameter.append(self.value)
        print("value will added"+str(self.value))
        print(parameter)

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
