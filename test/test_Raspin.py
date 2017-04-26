#  FILE: test_Raspin.py
#  hstone
#  2017-04-22
#
#
"""
Test the Raspin Class
"""
import unittest
import time
from Raspi_stuff import Raspin as Rpin

class TestRapian(unittest.TestCase):


    def test_rapian(self):
        print("Running the Tests")
        Rpin.Raspin.led17 = Rpin.Raspin(17, True)
    
        Rpin.Raspin.led17.setup(True)
        print("led17 setup and now: led17.on()")
        Rpin.Raspin.led17.on()
        print("time.sleep 2")
        time.sleep(2)
        print("led17.off()")
        Rpin.Raspin.led17.off()
        print("time.sleep 2")
        time.sleep(2)
        print("now let17.switch() it should go ON")
        Rpin.Raspin.led17.switch()
        print(Rpin.Raspin.led17.state)
        print(Rpin.Raspin.led17.ioid)
        time.sleep(2)
        print("now let17.switch() it should go OFF")
        Rpin.Raspin.led17.switch()
if __name__ == '__main__':
    unittest.main()
