#A Miciche
#places a ramdomly colored wool block

'''
Set up program fo MC and two buttons
create a 'counter' variable that starts at 0
create a list of blockdata numbers for different color wool
define a function called placeNext
- it takes one argument called direction
- it changes the counter by adding the direction argument
- place a wool block of the color from the list where
  the index matches the counter variable
- if the counter is out of bounds of the index, reset it
in a forever loop:
- if the first button was pressed, placeNext(1)
- if the second button was pressed, placeNext(-1)
'''
import time


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
print(mc.player.getTilePos())
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN,pull_up_down=GPIO.PUD_UP)

counter = 0
woolColors = [6, 5, 10]

def placeNext(direction):
    global counter
    counter += direction
    
    if counter > 2:
        counter = 0
    elif counter < 0:
        counter = 2was
    
    mc.setBlock(-63, 6, -42, 35, woolColors[counter])

while True:
    time.sleep(0.1)
    
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    elif GPIO.input(13) == GPIO.LOW:
        placeNext(-1)
    
    

    