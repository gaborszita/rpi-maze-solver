# Copyright 2018, 2021 Gabor Szita
# 
# This file is part of Raspberry Pi maze solver.
# 
# Raspberry Pi maze solver is free software: you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Raspberry Pi maze solver is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Raspberry Pi maze solver.  If not, see 
# <https://www.gnu.org/licenses/>.

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers

i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x6e, 0x6f, 12)

def sensornumconv(sensor):
    return (sensor+3)%8 + 1
