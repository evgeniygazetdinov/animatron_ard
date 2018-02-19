# here will be begin initizion

import pyfirmata
import time

class Scenario:
    port = '/dev/ttyACM0'
    port2 = '/dev/ttyUSB0'
    def __init__(self):
        self.angle = angle
        self.value = value
        self.servo_number = servo_number
        self.number_pin = number_pin

    def delay(self, timeout):
        time.sleep(timeout )

    def init_pin(self,number_pin):
        left = board.get_pin('d:%d:s')%self.number_pin

    def init_port_ard(self):
         pyfirmata.Arduino('/dev/ttyACM0')

    def change_pos(self,angle):



