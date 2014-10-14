import RPi.GPIO as gpio
import time

LED = 5

print "Indicating successful boot via LED..."

gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)

gpio.setup(LED, gpio.OUT)

gpio.output(LED, True)
time.sleep(.25)
gpio.output(LED, False)
time.sleep(.25)
gpio.output(LED,True)
time.sleep(.25)
gpio.output(LED, False)
time.sleep(.25)
gpio.output(LED,True)
time.sleep(.25)
gpio.output(LED, False)
time.sleep(.25)
gpio.output(LED,True)
