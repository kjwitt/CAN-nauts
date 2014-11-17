
import socket
import time

IP_ADDR = "192.168.1.1"
PORT = 5010

BUFFER_SIZE = 1024
WIDTH = 100

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( (IP_ADDR, PORT) )
	
while True:
	s.listen(1)
	conn, addr = s.accept()
	print "Connection Address:", addr
	message = False
	while not message:
		message = conn.recv( BUFFER_SIZE )
	print message
	print conn.send("3")
	conn.close()
s.close()
print "Connection Closed"

