#  FILE: Raspin.py
#  hstone
#  2017-04-16
#  Class to represent a single Item connection on the rasp pi a single GPIO 
#
"""
Turn a item on via the Raspberry Pi GPIO 

"""

import RPi.GPIO as GPIO
import time


class Raspin():
    ioid = None
    state = True

    def __init__(self, ioid, state=False):
        self.ioid = ioid
        self.state = state

    def setup(self, state):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ioid, GPIO.OUT)
        GPIO.output(self.ioid, self.state)
	
    def on(self):
        self.state = True
        GPIO.output(self.ioid, self.state)
	
    def off(self ):
        self.state = False
        GPIO.output(self.ioid, self.state)
	
    def switch(self):
        self.state = not self.state
        GPIO.output(self.ioid, self.state)
	
def main():
    led17 = Raspin(17,True)

    led17.setup(True)
    print("led17 setup and now: led17.on()")
    led17.on()
    print("time.sleep 2")
    time.sleep(2)
    print("led17.off()")
    led17.off()
    print("time.sleep 2")
    time.sleep(2)
    print("now let17.switch() it should go ON")
    led17.switch()
    print(led17.state)
    print(led17.ioid)
    time.sleep(2)
    print("now let17.switch() it should go OFF")
    led17.switch()

		
if __name__ == "__main__":
    main()

