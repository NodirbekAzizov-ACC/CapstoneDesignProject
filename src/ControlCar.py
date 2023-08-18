import RPi.GPIO as gpio
from time import sleep, time

#### Left
PIN1F=18
#### Right
PIN2F=24
#### Ultrasonic
Ult_T = 21
Ult_E = 20

gpio.setmode(gpio.BCM)
gpio.setup(PIN1F,gpio.OUT)
gpio.setup(PIN2F,gpio.OUT)

gpio.setup(Ult_T, gpio.OUT)
gpio.setup(Ult_E, gpio.IN)
gpio.output(Ult_T, False)

pin_f1=gpio.PWM(PIN1F, 50)
pin_f2=gpio.PWM(PIN2F, 50)

pin_f1.start(0)
pin_f2.start(0)


def stopCar():
    pin_f1.ChangeDutyCycle(0)
    pin_f2.ChangeDutyCycle(0)
    
def FastForward(speed):
	pin_f1.ChangeDutyCycle(speed+10)
	pin_f2.ChangeDutyCycle(speed+10)

def MiddleForward():
	pin_f1.ChangeDutyCycle(25)
	pin_f2.ChangeDutyCycle(25)
	
	
def StrongTurnR():
	pin_f1.ChangeDutyCycle(50)
	pin_f2.ChangeDutyCycle(0)
def smoothTurnR():
	pin_f1.ChangeDutyCycle(40)
	pin_f2.ChangeDutyCycle(30)
	
def StrongTurnL():
	pin_f1.ChangeDutyCycle(0)
	pin_f2.ChangeDutyCycle(50)
def smoothTurnL():
	pin_f1.ChangeDutyCycle(30)
	pin_f2.ChangeDutyCycle(40)

	
def Destroy():
	gpio.cleanup()
	

def F_UltMeasure():
    gpio.output(Ult_T, True)
    sleep(0.00001)
    gpio.output(Ult_T, False)
    start = time()
        
    while gpio.input(Ult_E)==0:
        start = time()
    while gpio.input(Ult_E)==1:
        stop = time()

    elapsed = stop - start
    distance = (elapsed * 34300)/2
    return distance

        
