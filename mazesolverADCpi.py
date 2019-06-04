#!/usr/bin/python3

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import time
import os

"""
================================================
ABElectronics ADC Pi ACS712 30 Amp current sensor demo
Version 1.0 Created 29/02/2015

Requires python 3 smbus to be installed
run with: python3 demo-acs712-30.py
================================================

Initialise the ADC device using the default addresses and sample rate,
change this value if you have changed the address selection jumpers

Sample rate can be 12,14, 16 or 18
"""

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x6e, 0x6f, 12)

# change the 2.5 value to be half of the supply voltage.


def sensornumconv(sensor):
    return (sensor+3)%8 + 1