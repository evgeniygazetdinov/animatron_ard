from config import *

def eyes():
    time.sleep(1)
    right_e.write(up)
    left_e.write(up)
    time.sleep(1)
def hands():
    time.sleep(1)
    right_leg.write(180)
    left_leg.write(180)
    right_hand.write(180)
    time.sleep(1)

def delay10():
    time.sleep(10)
def delay():
    time.sleep(5)

time_bar = []
time_bar.append(eyes)
time_bar.append(hands)
time_bar = [hands()]
