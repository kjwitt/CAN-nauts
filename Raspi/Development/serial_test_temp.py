import serial

arduino = serial.Serial("/dev/ttyACM0",9600)

state = 0
while True
		arduino.write('0')
		arduino.readline()
		print "Waiting for reply" 
		print arduino.readline()
	
