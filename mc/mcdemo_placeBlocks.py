#A Miciche
#set blocks example

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("hi")

# setup for Buttons and leds
import RPi.GPIO as GPIO #import Raspberry pi GPIO libary
GPIO.setwarnings(False) #ignore warning for now
GPIO.setmode(GPIO.BCM) #use physical pin numbering

GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def buildHouse():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x + 1, pos.y, pos.z + 1, pos.x + 6, pos.y + 5, pos.z + 6, 5)
    mc.setBlocks(pos.x + 2, pos.y + 1, pos.z + 2, pos.x + 5, pos.y + 4, pos.z + 5, 0)
    mc.setBlocks(pos.x + 3, pos.y + 1, pos.z + 1, pos.x + 3, pos.y + 2, pos.z + 1, 64)
    mc.setBlocks(pos.x)

while True:
    
    if GPIO.input(6) == GPIO.LOW:
        mc.postToChat("Button 6 was pressed")

        buildHouse()