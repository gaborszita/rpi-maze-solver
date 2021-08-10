# A Raspberry Pi maze solver robot

I built a little maze solver robot controller by a Raspberry Pi. You 
watch it solving a maze [here](https://youtu.be/M53tOSj7gX4).

The robot uses an infrared sensor to follow the path.

I used an [Adafruit DC and Stepper Motor HAT for Raspberry Pi](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/)
on my robot. If you also use this HAT, you are free to install the software 
required for using it by running the setup.py file in the 
Adafruit-Motor-HAT-Python-Library directory. You are free to use another 
HAT, but then you will need to modify the code in order for it to work.

I used the [ADC Pi analogue to digital converter](https://www.abelectronics.co.uk/p/69/adc-pi-raspberry-pi-analogue-to-digital-converter) 
for reading sensor data.
If you also use this analogue to digital converter, install it's library by 
following the directions in the ABElectronics_Python3_Libraries directory. 

Please note that the Adafruit-Motor-HAT-Python-Library and the 
ABElectronics_Python3_Libraries is NOT my code. The Adafruit Motor HAT 
library was copied from [https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library](https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library) 
and the ABEElectronics Python 3 library was copied from 
[https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library](https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library).

You need to run the ```mazesolver1.py``` python program for the robot 
to start solving the maze.
