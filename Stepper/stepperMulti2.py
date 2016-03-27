#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

motor1_A_1_pin = 17
motor1_A_2_pin = 4
motor1_B_1_pin = 18
motor1_B_2_pin = 23
motor2_A_1_pin = 22
motor2_A_2_pin = 27
motor2_B_1_pin = 24
motor2_B_2_pin = 25


GPIO.setup(motor1_A_1_pin, GPIO.OUT)
GPIO.setup(motor1_A_2_pin, GPIO.OUT)
GPIO.setup(motor1_B_1_pin, GPIO.OUT)
GPIO.setup(motor1_B_2_pin, GPIO.OUT)
GPIO.setup(motor2_A_1_pin, GPIO.OUT)
GPIO.setup(motor2_A_2_pin, GPIO.OUT)
GPIO.setup(motor2_B_1_pin, GPIO.OUT)
GPIO.setup(motor2_B_2_pin, GPIO.OUT)

def forwardMotor1(delay, steps):  
  for i in range(0, steps):
    setStep1(1, 0, 1, 0)
    time.sleep(delay)
    setStep1(0, 1, 1, 0)
    time.sleep(delay)
    setStep1(0, 1, 0, 1)
    time.sleep(delay)
    setStep1(1, 0, 0, 1)
    time.sleep(delay)  

def backwardsMotor1(delay, steps):  
  for i in range(0, steps):
    setStep1(1, 0, 0, 1)
    time.sleep(delay)
    setStep1(0, 1, 0, 1)
    time.sleep(delay)
    setStep1(0, 1, 1, 0)
    time.sleep(delay)
    setStep1(1, 0, 1, 0)
    time.sleep(delay)

def forwardMotor2(delay, steps):  
  for i in range(0, steps):
    setStep2(1, 0, 1, 0)
    time.sleep(delay)
    setStep2(0, 1, 1, 0)
    time.sleep(delay)
    setStep2(0, 1, 0, 1)
    time.sleep(delay)
    setStep2(1, 0, 0, 1)
    time.sleep(delay)  

def backwardsMotor2(delay, steps):  
  for i in range(0, steps):
    setStep2(1, 0, 0, 1)
    time.sleep(delay)
    setStep2(0, 1, 0, 1)
    time.sleep(delay)
    setStep2(0, 1, 1, 0)
    time.sleep(delay)
    setStep2(1, 0, 1, 0)
    time.sleep(delay)

def setStep1(w1, w2, w3, w4):
  GPIO.output(motor1_A_1_pin, w1)
  GPIO.output(motor2_A_1_pin, w1)
  GPIO.output(motor1_A_2_pin, w2)
  GPIO.output(motor2_A_2_pin, w2)
  GPIO.output(motor1_B_1_pin, w3)
  GPIO.output(motor2_B_1_pin, w3)
  GPIO.output(motor1_B_2_pin, w4)
  GPIO.output(motor2_B_2_pin, w4)

def setStep2(w1, w2, w3, w4):
  GPIO.output(motor1_A_1_pin, w1)
  GPIO.output(motor2_A_1_pin, w1)
  GPIO.output(motor1_A_2_pin, w2)
  GPIO.output(motor2_A_2_pin, w2)
  GPIO.output(motor1_B_1_pin, w3)
  GPIO.output(motor2_B_1_pin, w3)
  GPIO.output(motor1_B_2_pin, w4)
  GPIO.output(motor2_B_2_pin, w4)

i = 0
while(i < 5):
  i = i + 1
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  forwardMotor1(int(delay) / 1000.0, int(steps))
  forwardMotor2(int(delay) / 1000.0, int(steps))
  steps = raw_input("How many steps backwards? ")
  backwardsMotor1(int(delay) / 1000.0, int(steps))
  backwardsMotor2(int(delay) / 1000.0, int(steps))
GPIO.cleanup()
