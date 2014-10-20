import RPi.GPIO as GPIO
import time

# lock:		gpio pin 23
# unlock:	gpio pin 21
# panic:	gpio pin 19
# trunk:	gpio pin 15
LOCK = 23
UNLOCK = 21
PANIC = 19
TRUNK = 15
LED = 5

def initialize():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(LOCK, GPIO.OUT)
	GPIO.setup(UNLOCK, GPIO.OUT)
	GPIO.setup(PANIC, GPIO.OUT)
	GPIO.setup(TRUNK, GPIO.OUT)
	GPIO.setup(LED, GPIO.OUT)
	
	GPIO.output(LED, True)
	GPIO.output(LOCK, False)
	GPIO.output(UNLOCK, False)
	GPIO.output(PANIC, False)
	GPIO.output(TRUNK, False)

def press_button(gpio_pin):
	GPIO.output(gpio_pin, True)
	time.sleep(.25)
	GPIO.output(gpio_pin, False)

def lock():
	press_button(LOCK)

def unlock():
	press_button(UNLOCK)

def unlock_all():
	press_button(UNLOCK)
	time.sleep(.25)
	press_button(UNLOCK)

def trunk():
	press_button(TRUNK)

def panic():
	press_button(PANIC)

def main():
	initialize()
	input_var = 0
	while input_var != 9:
		input_var = input("Enter Command (1-Lock, 2-Unlock, 3-Unlock all, 4-Trunk, 5-Panic, 9-Quit): ")
		if input_var == 2:
			GPIO.output(LED,False)
			unlock()
			time.sleep(.15)
			GPIO.output(LED,True)
		elif input_var == 3:
			GPIO.output(LED,False)
			unlock_all()
			GPIO.output(LED,True)
		elif input_var == 1:
			GPIO.output(LED,False)
			lock()
			time.sleep(.15)
			GPIO.output(LED,True)
		elif input_var == 4:
			GPIO.output(LED,False)
			trunk()
			time.sleep(.15)
			GPIO.output(LED,True)
		elif input_var == 5:
			GPIO.output(LED,False)
			panic()
			time.sleep(.15)
			GPIO.output(LED,True)
		elif input_var == 9:
			print "Exiting..."
		else:
			print "INVALID"
	print "Successful Exit"

main()
