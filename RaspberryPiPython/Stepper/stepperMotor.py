import RPi.GPIO as GPIO
import time



class StepperMotor(object):
    def __init__(self, A_1_pin, A_2_pin, B_1_pin, B_2_pin, MAXFULLSTEPS, TOTALDISTANCE):
        self.A_1_pin = A_1_pin
        self.A_2_pin = A_2_pin
        self.B_1_pin = B_1_pin
        self.B_2_pin = B_2_pin
        self.MAXFULLSTEPS = MAXFULLSTEPS
        self.TOTALDISTANCE = TOTALDISTANCE
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(A_1_pin, GPIO.OUT)
        GPIO.setup(A_2_pin, GPIO.OUT)
        GPIO.setup(B_1_pin, GPIO.OUT)
        GPIO.setup(B_2_pin, GPIO.OUT)
        PERSISION = TOTALDISTANCE/(MAXFULLSTEPS*4)
        STATE = 1
        POSITION = 0

    def moveStep():
        if(STATE = 1):
            setStep(0,1,1,0
        
        


