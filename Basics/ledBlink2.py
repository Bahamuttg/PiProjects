#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OKLED - Turn on then off the OK / Activity LED.
"""
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

import RPi.GPIO as GPIO
from time import sleep

OKLED = 17

# setup GPIO, use Broadcom pin numbering.The only way to access pin 16
# on the BCM chip.
GPIO.setmode(GPIO.BCM)

GPIO.setup(OKLED, GPIO.OUT)

# Turn on LED
i = 0
while(i < 50):
    i = i + 1
    print i
    GPIO.output(OKLED, True)
    sleep(0.35)
    # Turn off LED
    GPIO.output(OKLED, False)
    sleep(0.15)
    GPIO.output(OKLED, True)
    sleep(0.5)
    # Turn off LED
    GPIO.output(OKLED, False)
    sleep(0.25)
# We are done, let's clean up after ourselves.
GPIO.cleanup()
