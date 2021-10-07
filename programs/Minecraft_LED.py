#A Miciche
#Minecraft Code Example

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("hi")

# setup for Buttons and leds
import RPi.GPIO as GPIO #import Raspberry pi GPIO libary
GPIO.setwarnings(False) #ignore warning for now
GPIO.setmode(GPIO.BCM) #use physical pin numbering

GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    
    if GPIO.input(6) == GPIO.LOW:
        mc.postToChat("Button 6 was pressed")

        