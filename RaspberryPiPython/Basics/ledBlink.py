#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import RPi.GPIO as GPIO
import time
# blinking function
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(100)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(100)
    return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)
# set up GPIO output channel
GPIO.setup(17, GPIO.OUT)
# blink GPIO17 50 times
for i in range(0,5):
    blink(11)
GPIO.cleanup()
