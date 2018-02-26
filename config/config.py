
import pyfirmata
import time
'file contain methods for using servo'
port ='/dev/ttyACM0'
port2 ='/dev/ttyUSB0'
board = pyfirmata.Arduino(port2)
#sholder_eft('d:2:s')
right_e = board.get_pin('d:8:s')
left_e = board.get_pin('d:9:s')
sholder_right = board.get_pin('d:7:s')
right_hand = board.get_pin('d:3:s')
left_hand = board.get_pin('d:6:s')
left_leg = board.get_pin('d:4:s')
right_leg = board.get_pin('d:5:s')
up = 180
down =90









