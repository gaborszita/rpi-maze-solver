from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

from mazesolverADCpi import *

from threading import Thread
import time
import atexit
import sys

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)

myMotor1.run(Adafruit_MotorHAT.FORWARD)
myMotor2.run(Adafruit_MotorHAT.FORWARD)

#turnOffMotors()
########################!!!MAINPROGRAM!!!############################


def mainprogram():
    #rightsensors = []
    path = []
    while True:
        sensorvalues = SensorReadingsArrayCreator()
        #print(sensorvalues)
        # how many sensors are on the path
        sensorsonpath = 0
        for i in range(1, 7):
            if sensorvalues[i]>midValue:
                sensorsonpath+=1
        if  sensorsonpath == 1 or sensorsonpath == 2:
            # find sensor on path
            OnPathSensor = 1
            for i in range(2, 7):
                if sensorvalues[i]>sensorvalues[OnPathSensor]:
                    OnPathSensor = i
            OnPathSensor += 1
            if OnPathSensor == 3:          # close to middle left
                myMotor1.setSpeed(70)
                myMotor2.setSpeed(90)
            elif OnPathSensor == 6:        # close to middle right
                myMotor1.setSpeed(90)
                myMotor2.setSpeed(70)
            elif OnPathSensor == 2:        # far from middle left
                myMotor1.setSpeed(30)
                myMotor2.setSpeed(90)
            elif OnPathSensor == 7:        # far to middle right
                myMotor1.setSpeed(90)
                myMotor2.setSpeed(30)
            #elif OnPathSensor == 1:
             #   print("1 set")
              #  myMotor1.setSpeed(55)
               # myMotor2.setSpeed(90)
            #elif OnPathSensor == 8:
             #   print("8 set")
              #  myMotor1.setSpeed(90)
               # myMotor2.setSpeed(55)
            elif sensorvalues[3]>=midValue and sensorvalues[4]>=midValue:
                myMotor1.setSpeed(90)
                myMotor2.setSpeed(90)
            elif OnPathSensor == 4:
                myMotor1.setSpeed(80)
                myMotor2.setSpeed(90)
            elif OnPathSensor == 5:
                myMotor1.setSpeed(80)
                myMotor2.setSpeed(90)
        
        elif sensorvalues[1] >= midValue and sensorvalues[2] >= midValue and sensorvalues[3] >= midValue:
            time.sleep(0.35)
            sensorvalues = SensorReadingsArrayCreator()
            if sensorvalues[1] <= midValue and sensorvalues[2] <= midValue and sensorvalues[3] <= midValue and sensorvalues[4] <= midValue and sensorvalues[5] <= midValue and sensorvalues[6] <= midValue:
                path.append("L")
                myMotor2.setSpeed(90)
                myMotor1.setSpeed(0)
                #myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                #myMotor1.setSpeed(70)
                while sensorvalues[4]<=midValue:
                    sensorvalues = SensorReadingsArrayCreator()
                    if sensorvalues[1]>=midValue:
                        #myMotor1.setSpeed(45)
                        myMotor2.setSpeed(50)
                        #print("now")
            #myMotor1.run(Adafruit_MotorHAT.FORWARD)
            elif sensorvalues[1] <= midValue and sensorvalues[6] <= midValue:
                path.append("L")
                #print("st")
                myMotor2.setSpeed(90)
                myMotor1.setSpeed(0)
                while sensorvalues[6]<=midValue:
                    sensorvalues = SensorReadingsArrayCreator()
                #print("out1")
                #myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                #myMotor1.setSpeed(70)
                while sensorvalues[4]<=midValue:
                    sensorvalues = SensorReadingsArrayCreator()
                    if sensorvalues[1]>=midValue:
                        #myMotor1.setSpeed(45)
                        myMotor2.setSpeed(50)
                        #print("now")
            #myMotor1.run(Adafruit_MotorHAT.FORWARD)
            else:
                done(path)
            
        elif sensorvalues[7] >= midValue and sensorvalues[6] >= midValue and sensorvalues[5] >= midValue:
            #rightsensors.append(SensorReadingsArrayCreator())
            leftgo = 0
            starttime = time.clock_gettime(0)
            while time.clock_gettime(0) < (starttime + 0.35):
                sensorvalues = SensorReadingsArrayCreator()
                if sensorvalues[1] > midValue:
                    leftgo = 1
            #rightsensors.append(sensorvalues)
            #turnOffMotors()
            #print(rightsensors)
            #sys.exit()
            if leftgo == 1:
                path.append("L")
                if sensorvalues[1] <= midValue and sensorvalues[6] <= midValue:
                    myMotor2.setSpeed(90)
                    myMotor1.setSpeed(0)
                    #myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                    #myMotor1.setSpeed(70)
                    while sensorvalues[4]<=midValue:
                        sensorvalues = SensorReadingsArrayCreator()
                        if sensorvalues[1]>=midValue:
                            #myMotor1.setSpeed(45)
                            myMotor2.setSpeed(50)
                            #print("now")
                #myMotor1.run(Adafruit_MotorHAT.FORWARD)
                else:
                    done(path)
            else:
                if sensorvalues[1] <= midValue and sensorvalues[6] <= midValue and (sensorvalues[4] <= midValue and sensorvalues[5] <= midValue):
                    path.append("R")
                    #print("right")
                    myMotor1.setSpeed(90)
                    myMotor2.setSpeed(0)
                    #myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                    #myMotor2.setSpeed(70)
                    while sensorvalues[3]<=midValue:
                        sensorvalues = SensorReadingsArrayCreator()
                        if sensorvalues[6]>=midValue:
                            #myMotor1.setSpeed(45)
                            myMotor1.setSpeed(50)
                            #print("now")
                #myMotor1.run(Adafruit_MotorHAT.FORWARD)
                elif sensorvalues[1] <= midValue and sensorvalues[2] <= midValue and sensorvalues[3] <= midValue and sensorvalues[4] <= midValue and sensorvalues[5] <= midValue and sensorvalues[6] <= midValue:
                    done(path)
                else:
                    path.append("S")
        
        elif sensorsonpath == 0:
            myMotor1.setSpeed(90)
            myMotor2.run(Adafruit_MotorHAT.BACKWARD)
            myMotor2.setSpeed(90)
            while sensorvalues[3]<=midValue:
                sensorvalues = SensorReadingsArrayCreator()
                if sensorvalues[6]>=midValue:
                    myMotor1.setSpeed(45)
                    myMotor2.setSpeed(45)
                    #print("now")
            myMotor2.run(Adafruit_MotorHAT.FORWARD)
            path.append("B")

def pathSortSolver(path):
    pathPos = 0
    while True:
        sensorvalues = SensorReadingsArrayCreator()
        #print(sensorvalues)
        # how many sensors are on the path
        sensorsonpath = 0
        for i in range(1, 7):
            if sensorvalues[i]>midValue:
                sensorsonpath+=1
        if  sensorsonpath == 1 or sensorsonpath == 2:
            # find sensor on path
            OnPathSensor = 1
            for i in range(2, 7):
                if sensorvalues[i]>sensorvalues[OnPathSensor]:
                    OnPathSensor = i
            OnPathSensor += 1
            if OnPathSensor == 3:          # close to middle left
                myMotor1.setSpeed(70)
                myMotor2.setSpeed(90)
            elif OnPathSensor == 6:        # close to middle right
                myMotor1.setSpeed(90)
                myMotor2.setSpeed(70)
            elif OnPathSensor == 2:        # far from middle left
                myMotor1.setSpeed(30)
                myMotor2.setSpeed(90)
            elif OnPathSensor == 7:        # far to middle right
                myMotor1.setSpeed(90)
                myMotor2.setSpeed(30)
            #elif OnPathSensor == 1:
             #   print("1 set")
              #  myMotor1.setSpeed(55)
               # myMotor2.setSpeed(90)
            #elif OnPathSensor == 8:
             #   print("8 set")
              #  myMotor1.setSpeed(90)
               # myMotor2.setSpeed(55)
            elif sensorvalues[3]>=midValue and sensorvalues[4]>=midValue:
                myMotor1.setSpeed(90)
                myMotor2.setSpeed(90)
            elif OnPathSensor == 4:
                myMotor1.setSpeed(80)
                myMotor2.setSpeed(90)
            elif OnPathSensor == 5:
                myMotor1.setSpeed(80)
                myMotor2.setSpeed(90)
        elif pathPos>=len(path):
            turnOffMotors()
            sys.exit()
        elif path[pathPos] == 'L':
            print('L')
            time.sleep(0.35)
            sensorvalues = SensorReadingsArrayCreator()
            if sensorvalues[1] <= midValue and sensorvalues[2] <= midValue and sensorvalues[3] <= midValue and sensorvalues[4] <= midValue and sensorvalues[5] <= midValue and sensorvalues[6] <= midValue:
                myMotor2.setSpeed(90)
                myMotor1.setSpeed(0)
                #myMotor1.run(Adafruit_MotorHAT.BACKWARD)
                #myMotor1.setSpeed(70)
                while sensorvalues[4]<=midValue:
                    sensorvalues = SensorReadingsArrayCreator()
                    if sensorvalues[1]>=midValue:
                        #myMotor1.setSpeed(45)
                        myMotor2.setSpeed(50)
                        #print("now")
            #myMotor1.run(Adafruit_MotorHAT.FORWARD)
            elif sensorvalues[1] <= midValue and sensorvalues[6] <= midValue:
                continue
                
            pathPos += 1
            
        elif path[pathPos] == 'R':
            print('R')
            time.sleep(0.35)
            sensorvalues = SensorReadingsArrayCreator()
            if sensorvalues[1] <= midValue and sensorvalues[6] <= midValue:
                print("ent")
                #print("right")
                myMotor1.setSpeed(90)
                myMotor2.setSpeed(0)
                #myMotor2.run(Adafruit_MotorHAT.BACKWARD)
                #myMotor2.setSpeed(70)
                while sensorvalues[3]<=midValue:
                    sensorvalues = SensorReadingsArrayCreator()
                    if sensorvalues[6]>=midValue:
                        #myMotor1.setSpeed(45)
                        myMotor1.setSpeed(50)
                        #print("now")
            #myMotor1.run(Adafruit_MotorHAT.FORWARD)
            pathPos += 1
        
        elif path[pathPos] == 'B':
            myMotor1.setSpeed(90)
            myMotor2.run(Adafruit_MotorHAT.BACKWARD)
            myMotor2.setSpeed(90)
            while sensorvalues[3]<=midValue:
                sensorvalues = SensorReadingsArrayCreator()
                if sensorvalues[6]>=midValue:
                    myMotor1.setSpeed(45)
                    myMotor2.setSpeed(45)
                    #print("now")
            myMotor2.run(Adafruit_MotorHAT.FORWARD)
            pathPos += 1

        elif path[pathPos] == 'S':
            time.sleep(0.35)
            pathPos += 1

####################!!!MidValueCalculator!!!##############################

def MiddleValueCalc():
    global midValue
    sensorvalues = SensorReadingsArrayCreator()
    midValue = (FindBiggest(sensorvalues[1:6]) + FindLeast(sensorvalues[1:6]))/2
    while True:
        time.sleep(0.1)
        # get sensor values
        sensorvalues = SensorReadingsArrayCreator()
        # check is bigger value in the sensor readings
        biggerlist = 0
        for i in range(1, 7):
            if sensorvalues[i]>midValue:
                biggerlist+=1
        if (FindBiggest(sensorvalues[1:6]) - FindLeast(sensorvalues[1:6]))>=0.2:
            midValue = (FindBiggest(sensorvalues[1:6]) + FindLeast(sensorvalues[1:6]))/2

##########################!!!Other additional defines!!!#########################


def SensorReadingsArrayCreator():
    while True:
        try:
            sensorvalues = []
            for i in range(1, 9):
                sensorvalues.append(adc.read_voltage(sensornumconv(i)))
            return sensorvalues
        except:
            continue

def FindBiggest(value):
    biggest = value[0]
    for i in range(1, len(value)):
        if value[i]>biggest:
            biggest = value[i]
    return biggest

def FindLeast(value):
    least = value[0]
    for i in range(1, len(value)):
        if value[i]<least:
            least = value[i]
    return least

    

def tof():
    turnOffMotors()

def done(path):
    myMotor1.setSpeed(0)
    myMotor2.setSpeed(0)
    print("done")
    print(path)
    path = pathsortener(path)
    print(path)
    time.sleep(8)
    pathSortSolver(path)

def pathsortener(path):
    found = True
    while found == True:
        found = False
        for i in range(0, len(path)-2):
            if path[i:i+3] == ['L', 'B', 'R']:
                path[i] = 'B'
                path[i+1] = 'NULL'
                path[i+2] = 'NULL'
                found = True
                break
            elif path[i:i+3] == ['L', 'B', 'S']:
                path[i] = 'R'
                path[i+1] = 'NULL'
                path[i+2] = 'NULL'
                found = True
                break
            elif path[i:i+3] == ['R', 'B', 'L']:
                path[i] = 'B'
                path[i+1] = 'NULL'
                path[i+2] = 'NULL'
                found = True
                break
            elif path[i:i+3] == ['S', 'B', 'L']:
                path[i] = 'R'
                path[i+1] = 'NULL'
                path[i+2] = 'NULL'
                found = True
                break
            elif path[i:i+3] == ['S', 'B', 'S']:
                path[i] = 'B'
                path[i+1] = 'NULL'
                path[i+2] = 'NULL'
                found = True
                break
            elif path[i:i+3] == ['L', 'B', 'L']:
                path[i] = 'S'
                path[i+1] = 'NULL'
                path[i+2] = 'NULL'
                found = True
                break
        if found == True:
            path.remove('NULL')
            path.remove('NULL')
    return path

Thread(target=MiddleValueCalc).start()
time.sleep(1)
mainprogram()

