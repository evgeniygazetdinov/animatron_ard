
<<<<<<< HEAD


def first_sec():
    left.write(up)
    time.sleep(2)
    left.write(down)
    time.sleep(2)
    left.write(up)
    time.sleep(2)
    left.write(down)

def second_sec():
    right.write(up)
    time.sleep(2)
    right.write(down)
    time.sleep(2)
    right.write(up)
    time.sleep(2)
    right.write(down)
    time.sleep(2)
    right.write(up)
def delay10():
    time.sleep(10)
def delay():
    time.sleep(5)

time_bar.append(first_sec)
time_bar.append(second_sec)
time_bar.append(delay10)
delay10(),first_sec(),delay10(),second_sec(),delay10(),delay10()
=======
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

>>>>>>> 0d26ad640e5622fec04724e44875d02f76bd65c0
