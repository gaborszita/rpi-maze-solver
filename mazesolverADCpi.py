from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x6e, 0x6f, 12)

def sensornumconv(sensor):
    return (sensor+3)%8 + 1
