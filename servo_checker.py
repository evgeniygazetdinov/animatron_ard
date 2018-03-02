import pyfirmata
import time
def first():
    board = pyfirmata.Arduino('/dev/ttyUSB0')
    right_e = board.get_pin('d:8:s')
    left_e = board.get_pin('d:9:s')
    sholder_right = board.get_pin('d:7:s')
    right_hand = board.get_pin('d:3:s')
    left_hand = board.get_pin('d:6:s')
    left_leg = board.get_pin('d:4:s')


    left_e.write(90)
    left_e.write(100)
    left_e.write(110)
    left_e.write(120)

def second():
    board = pyfirmata.Arduino('/dev/ttyUSB0')
    right_e = board.get_pin('d:8:s')
    left_e = board.get_pin('d:9:s')
    sholder_right = board.get_pin('d:7:s')
    right_hand = board.get_pin('d:3:s')
    left_hand = board.get_pin('d:6:s')
    left_leg = board.get_pin('d:4:s')
    for i in range(180):
       time.sleep(0.02)
       left_leg.write(i)
       time.sleep(0.02)
       if i>=180:
           break




second()

