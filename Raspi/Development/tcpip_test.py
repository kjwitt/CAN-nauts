import socket

IP_ADDR = "192.168.1.1"
PORT = 5005

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

conn.send( "WUDDUP" )
s.close()

