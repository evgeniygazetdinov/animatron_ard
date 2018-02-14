from multiprocessing import Pool,freeze_support,Process
import threading
import pyfirmata
import time
'''file contain methods for using servo'''
board = pyfirmata.Arduino('/dev/ttyACM0')
left = board.get_pin('d:8:s')
right = board.get_pin('d:6:s')
flag =True
def action():
    while flag:
        left.write(360)
        time.sleep(1)
        left.write(180)
        time.sleep(1)
def non():
   while flag :
       right.write(180)
       time.sleep(1)
       right.write(360)
       time.sleep(1)
