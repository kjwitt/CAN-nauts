
import socket
import time

IP_ADDR = "192.168.1.1"
PORT = 5006

BUFFER_SIZE = 1024
WIDTH = 100

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.bind( (IP_ADDR, PORT) )
s.listen(1)

conn, addr = s.accept()
print "Connection Address:", addr
message = False
while not message:
	message = conn.recv( BUFFER_SIZE )
print message
while True:
	print "Bytes Sent",conn.send("3")
	time.sleep(2)
conn.close()
s.close()
print "Connection Closed"

