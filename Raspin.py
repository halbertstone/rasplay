#  FILE: Raspin.py
#  hstone
#  2017-04-16
#  Class to represent a single Item connection on the rasp pi a single GPIO 
#

import RPi.GPIO as GPIO
import time


class Raspin():
    """
    Utility for working with the raspberry pi GPIO PINS
    based on the GPIO.BCM pin numbering scheme
    Concept: Peripheral is connected to a GPIO PIN
    Class can be used to associate the peripheral with 
    assigned PIN  and manipulate PIN power on, off, toggle

    USAGE: 
     ioid = None
     pin_map = None
    """

    def __init__(self
            , ioid
            , pin_map=GPIO.BCM):
        """ param: ioid is the pin number in the selected pin_mode
        param: pin_mode is the pin numbering system selected
        param: state is the initial power setting for the pin
        """
        self.ioid = ioid
        self.pin_mode = pin_mode

    def setup_output(self, state):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ioid, GPIO.OUT)
	
    def on(self):
        self.state = True
        GPIO.output(self.ioid, self.state)
	
    def off(self ):
        self.state = False
        GPIO.output(self.ioid, self.state)
	
    def switch(self):
        self.state = not self.state
        GPIO.output(self.ioid, self.state)

	
class PinOut(Raspin):
    """
    Utility for working with the raspberry pi GPIO PINS
    based on the GPIO.BCM pin numbering scheme
    Concept: Peripheral is connected to a GPIO PIN
    Class can be used to associate the peripheral with 
        assigned PIN  and manipulate PIN power on, off, toggle
    
    USAGE: 
        led17 = PinOut(17)
        led17.on() for power on
        led17.off() for power off
        led17.switch() to toggle power
         param: ioid is the pin number in the selected pin_mode
         param: pin_mode is GPIO.OUT (default)
         param: pin_map is pin number scheme GPIO.BCM (defalut), or GPIO.BOARD
         param: state is the initial power setting for the pin False (default)
        
    """
    state = False
    pin_mode = None

    def __init__(self
            , ioid
            , pin_mode=GPIO.OUT
            , pin_map=GPIO.BCM
            , state=False):
        # TODO: if not ioid in range(42): define valid numbers per pin_map
        # TODO:     raise exception   define appropriate exception
        # TODO: if pin_mode in ["GPIO.BCM", "GPIO.BOARD"]:
        
        super(type(PinOut), self).__init__(ioid, pin_map)

        # TODO: if state in [True, False]:
        self.state = state
        self.setup_output()


    def setup_output(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.ioid, GPIO.OUT)
	
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
    led17 = PinOut(17)
    led17.setup()

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

