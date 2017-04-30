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
	
def light_setup(number):
    led = Raspin(number, True)
    led.setup(True)
    led.on()
    return led

def switch_after(sec, light):
    time.sleep(sec)
    light.switch()

def daddoo_pattern():
    print "Daddoos pattern..."
    red = light_setup(27)
    blue = light_setup(17)
    blue.off()

    for i in range(0,5):
        switch_after(1, blue)
        switch_after(1, red)

    time.sleep(1)
    red.off()
    blue.off()

    GPIO.cleanup()

   
def papa_pattern():
    print "pappas pattern..."
    led17 = light_setup(17)
    jude = light_setup(27)
    
    time.sleep(2)

    led17.off()

    time.sleep(2)

    jude.off()
    led17.on()

    time.sleep(2)

    jude.on()
    led17.on()

    time.sleep(1)

    jude.switch()
    led17.switch()

    GPIO.cleanup()



def judes_lights():
    print "judes pattern..."
    red = light_setup(27)
    blue = light_setup(17)

    time.sleep(2)
    red.off()
    time.sleep(2)
    blue.off()
    time.sleep(2)
    red.on()
    blue.on()
    time.sleep(2)
    blue.off()
    time.sleep(2)
    red.off()
    blue.on()
    time.sleep(2)
    red.switch()
    time.sleep(2)

    GPIO.cleanup()










def main():
    judes_lights()
    papa_pattern()
    daddoo_pattern()

if __name__ == "__main__":
    main()
