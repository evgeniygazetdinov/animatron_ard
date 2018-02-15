
import pyfirmata
import time
from main import port2,port
'file contain methods for using servo'
board = pyfirmata.Arduino(port2)
left = board.get_pin('d:8:s')
right = board.get_pin('d:6:s')


def leftw():
    time.sleep(2)
    left.write(value)
    time.sleep(2)
    left.write(0)

def rightw():
    right.write(360)
    time.sleep(20)
    right.write(0)

