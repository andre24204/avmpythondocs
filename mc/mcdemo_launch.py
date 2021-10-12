#A Miciche
#gets minecraft blocks by Position

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

import RPi.GPIO as GPIO #import Raspberry pi GPIO libary
GPIO.setwarnings(False) #ignore warning for now
GPIO.setmode(GPIO.BCM) #use physical pin numbering

GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(6) == GPIO.LOW:
        pos = mc.player.getTilePos()
        print(pos)
        blockData = mc.getBlock(pos.x, pos.y - 1, pos.z)
        print(blockData)
        #if the blockData is a Diamond block,
        #change the player's position toit current position
        #plus 20 to get the y position
        if blockData == 57:
            mc.player.setTilePos(pos.x, pos.y + 20, pos.z)