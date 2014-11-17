import SocketServer
import serial
import time
import RPi.GPIO as GPIO

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
	# GPIO.setup(LED, GPIO.OUT)
	
	# GPIO.output(LED, True)
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

class TCPHandler(SocketServer.BaseRequestHandler):
	def setup(self):
		print self.client_address, "connected"

	def handle(self):
		while True:
			self.data = self.request.recv(1024)

			print "{} wrote:".format(self.client_address[0])
			print self.data.strip()

			if self.data.strip().find("keyfob") != -1:
				fobcode = int(self.data.strip().split('-')[1])
				if fobcode == 1:
					# GPIO.output(LED,False)
					print "locking..."
					lock()
					time.sleep(.15)
					# GPIO.output(LED,True)
				elif fobcode == 2:
					# GPIO.output(LED,False)
					print "unlocking..."
					unlock()
					time.sleep(.15)
					# GPIO.output(LED,True)
				elif fobcode == 3:
					# GPIO.output(LED,False)
					print "unlocking all.."
					unlock_all()
					# GPIO.output(LED,True)
				elif fobcode == 4:
					# GPIO.output(LED,False)
					print "opening trunk..."
					trunk()
					time.sleep(.15)
					# GPIO.output(LED,True)
				elif fobcode == 5:
					# GPIO.output(LED,False)
					print "panicking..."
					panic()
					time.sleep(.15)
					# GPIO.output(LED,True)
				self.request.send('done'+'-' + str(fobcode) + '\n')

			elif self.data.strip().find("status") != -1:
				statcode = int(self.data.strip().split('-')[1])
				if statcode == 1:
					arduino.write('0')
					print "opcode:",arduino.readline().strip()
					#time.sleep(1) 
					temperature = arduino.readline().strip()
					print "temperature:",temperature
					self.request.send(temperature+'\n')
				elif statcode == 2:
					arduino.write('1')
					print "opcode:",arduino.readline().strip()
					#time.sleep(1)
					wet = arduino.readline().strip()
					print "wet:",wet
					self.request.send(wet+'\n')
			elif self.data.strip() == "close" or self.data.strip() == "":
				self.request.send(self.data)
				self.request.close();
				return			

	def finish(self):
		print self.client_address, "disconnected"
		

if __name__ == "__main__":
	initialize();
	print "Keyfob initialized"
	print

	arduino = serial.Serial("/dev/ttyACM0",9600)
	print "Arduiner serial port opened (9600 baud)"
	print

	HOST, PORT = "192.168.1.1",8000
	print "Server established on:",HOST,PORT
	print 

	SocketServer.TCPServer.allow_reuse_address = True
	server = SocketServer.TCPServer((HOST, PORT), TCPHandler)

	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.shutdown()
		server.socket.close()
