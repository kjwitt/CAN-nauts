import serial
import time

arduino = serial.Serial("/dev/ttyACM0",9600)
print "Open port with Arduiner"

while True:
	arduino.write('0')
	print "opcode:",arduino.readline().strip()
	#time.sleep(1) 
	print "temp:",arduino.readline().strip()
	#time.sleep(1)
	arduino.write('1')
	print "opcode:",arduino.readline().strip()
	#time.sleep(1)
	print "message:",arduino.readline().strip()
	time.sleep(1)
	
