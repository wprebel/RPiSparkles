from sense_hat import SenseHat
#import RPi.GPIO as gpio
from random import randint
from time import sleep

sense = SenseHat()

try:
    
    while True:

        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(100, 255)
        g = randint(100, 255)
        b = randint(100, 255)

        sense.set_pixel(x, y, r, g, b)
        sleep(0.01)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    #print "\n", counter # print value of counter  
    sense.clear()
    #gpio.cleanup() # this ensures a clean exit  
