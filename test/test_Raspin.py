#  FILE: test_Raspin.py
#  hstone
#  2017-04-22
#
#
"""
Test the Raspin Class
"""

import time
import unittest

from Raspi_stuff import Raspin as Rpin


class Test_Raspin(unittest):
    def test_rapian(self):
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
