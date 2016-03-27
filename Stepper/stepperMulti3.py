#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# For input pins on motor controller using two GPIOs per motor.
# This tested with a TI 7404 HEX INVERTER and with 2 TI 754410
# and 2 L298N Dual H Bridges


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

motor1_A_pin = 17
motor1_B_pin = 4
motor2_A_pin = 23
motor2_B_pin = 18
motor3_A_pin = 27
motor3_B_pin = 22
MAXSTEPS = 23
TOTALDISTANCE = 35
PERSISION = TOTALDISTANCE/MAXSTEPS


GPIO.setup(motor1_A_pin, GPIO.OUT)
GPIO.setup(motor1_B_pin, GPIO.OUT)
GPIO.setup(motor2_A_pin, GPIO.OUT)
GPIO.setup(motor2_B_pin, GPIO.OUT)
GPIO.setup(motor3_A_pin, GPIO.OUT)
GPIO.setup(motor3_B_pin, GPIO.OUT)

def forwardMotor1(delay, steps):  
  for i in range(0, steps):
    setStep1(1, 1)
    time.sleep(delay)
    setStep1(0, 1)
    time.sleep(delay)
    setStep1(0, 0)
    time.sleep(delay)
    setStep1(1, 0)
    time.sleep(delay)  

def backwardsMotor1(delay, steps):  
  for i in range(0, steps):
    setStep1(1, 0)
    time.sleep(delay)
    setStep1(0, 0)
    time.sleep(delay)
    setStep1(0, 1)
    time.sleep(delay)
    setStep1(1, 1)
    time.sleep(delay)

def setStep1(w1, w3):
  GPIO.output(motor1_A_pin, w1)
  GPIO.output(motor2_A_pin, w1)
  GPIO.output(motor3_A_pin, w1)
  GPIO.output(motor1_B_pin, w3)
  GPIO.output(motor2_B_pin, w3)
  GPIO.output(motor3_B_pin, w3)

def setStep2(w1, w3):
  GPIO.output(motor1_A_pin, w1)
  GPIO.output(motor2_A_pin, w1)
  GPIO.output(motor1_B_pin, w3)
  GPIO.output(motor2_B_pin, w3)

i = 0
while(i < 5):
  i = i + 1
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  forwardMotor1(int(delay) / 1000.0, int(steps))
  steps = raw_input("How many steps backwards? ")
  backwardsMotor1(int(delay) / 1000.0, int(steps))
GPIO.cleanup()
