#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OKLED - Turn on then off the OK / Activity LED.
"""
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import RPi.GPIO as GPIO
from time import sleep

OKLED = 12
OKLED2 = 16

# setup GPIO, use Broadcom pin numbering.The only way to access pin 16
# on the BCM chip.
#GPIO.setmode(GPIO.BCM)

GPIO.setup(OKLED, GPIO.OUT)
GPIO.setup(OKLED2, GPIO.OUT)

# Turn on LED
i = 0
while(i < 50):
    i = i + 1
    print i
    GPIO.output(OKLED, True)
    GPIO.output(OKLED2, False)
    sleep(0.5)
    GPIO.output(OKLED, False)
    sleep(0.25)
    # Turn off LED
    GPIO.output(OKLED2, True)
    sleep(0.5)
# We are done, let's clean up after ourselves.
#GPIO.cleanup()
