from pyfirmata import Arduino,INPUT,PWM,util,Board

from time import sleep

import random

'''board.digital[13].write()
'''
port  = '/dev/ttyACM0'

board = Arduino(port)
iter8 = py
while True:
    board.servo_config(7,200,100,30,90)


