#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)

coil_A_1_pin = 11
coil_A_2_pin = 7
coil_B_1_pin = 12
coil_B_2_pin = 16

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def forward(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)  

def backwards(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)  

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

while True:  
  forward(int(2) / 1000.0, int(25))
  time.sleep(0.1)
  backwards(int(2) / 1000.0, int(25))
  time.sleep(0.1)
