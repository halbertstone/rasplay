#  FILE: Raspin.py
#  hstone
#  2017-04-16
#  Class to represent a single Item connection on the rasp pi a single GPIO 
#
#  some good info but for older Rasp Pi
#  http://raspi.tv/2013/rpi-gpio-basics-5-setting-up-and-using-outputs-with-rpi-gpio
#
"""
Model:
RaspIOBus - class to represent the entire set of GPIO PINS
Raspin    - class to represent a single pin on the GPIO BUS

-- Things --
-    Some pins on the BUS are GROUND, 5v, 3.3v, not all are IO
-    IO pins can be set for Output, or Input

-    IO Output pins can be:
-      - 
-    IO Input pins can be:
-      - 

== == GPIO methods ==
+ GPIO.setmodel     Pin Numbering scheme to use [ BCM or BOARD ]
+ GPIO.setup        Pin Number is assigned an attribute
+ GPIO.output       An Output Pin's power is set on/off
+ GPIO.cleanup()    resets all GPIO ports; only works after GPIO.setup
+ 
"""


import time

import RPi.GPIO as GPIO


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
