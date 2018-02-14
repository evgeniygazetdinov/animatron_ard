from multiprocessing import Pool,freeze_support,Process
import threading
import pyfirmata
import time
'''file contain methods for using servo'''
board = pyfirmata.Arduino('/dev/ttyACM0')
left = board.get_pin('d:8:s')
right = board.get_pin('d:6:s')
while True:
   left.write(360)
   time.sleep(2)
   left.write(0)
   right.write(360)
   time.sleep(2)
   right.write(0)