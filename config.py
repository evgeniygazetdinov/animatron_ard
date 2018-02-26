
from tkinter import *
from  tkinter import ttk
import pyfirmata
import time
import serial.tools.list_ports
'file contain methods for using servo'


port ='/dev/ttyACM0'
port2 ='/dev/ttyUSB0'
port3 = []
ports = list(serial.tools.list_ports.comports())
print(port3)



def port_indit():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        port3.append(str(p))
        return port3


root =Tk()

choiceport = Spinbox(root,value = port3).pack()
root.mainloop()


port ='/dev/ttyACM0'
port2 ='/dev/ttyUSB0'
port3 = []
ports = list(serial.tools.list_ports.comports())
port_indit()
print(port3)






'''

#sholder_eft('d:2:s')


sholder_right= board.get_pin('d:7:s')
left_leg = board.get_pin('d:4:s')
right_leg = board.get_pin('d:5:s')
left_hand = board.get_pin('d:6:s')
right_hand = board .get_pin('d:3:s')
right_e =board.get_pin('d:8:s')
left_e = board.get_pin('d:9:s')
up = 180
down =90
'''


