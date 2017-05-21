#! /usr/bin/env python

import os
import sys
from papirus import Papirus
import RPi.GPIO as GPIO

from show_wallet_address import show_wallet_address
from show_unspent import show_unspent

hatdir = '/proc/device-tree/hat'
SW1 = 21
SW2 = 16
SW3 = 20
SW4 = 19
SW5 = 26

papirus = Papirus()

GPIO.setmode(GPIO.BCM)

GPIO.setup(SW1, GPIO.IN)
GPIO.setup(SW2, GPIO.IN)
GPIO.setup(SW3, GPIO.IN)
GPIO.setup(SW4, GPIO.IN)
if SW5 != -1:
    GPIO.setup(SW5, GPIO.IN)

show_wallet_address()

while True:
    # Exit when SW1 and SW5 are pressed simultaneously
    if (GPIO.input(SW1) == False) and (GPIO.input(SW5) == False) :
        sys.exit()

    if (GPIO.input(SW5) == False) :
      show_wallet_address();

    if (GPIO.input(SW4) == False) :
      show_unspent();
