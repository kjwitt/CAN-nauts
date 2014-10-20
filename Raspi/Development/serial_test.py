import serial

arduino = serial.Serial("/dev/ttyACM0",9600)

state = 0
while state !=9:
	state=input("Enter a LED state (9 to quit): ")
	if state == 0:
		arduino.write('0')
		print("Waiting for reply")
		print(arduino.readline())
	elif state == 1:
		arduino.write('1')
		print("Waiting for reply")
		print(arduino.readline())
	else:
		print("Exiting")	
	
