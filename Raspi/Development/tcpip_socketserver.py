import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler):
	def setup(self):
		print self.client_address, "connected"

	def handle(self):
		while True:
			self.data = self.request.recv(1024)
			print "{} wrote:".format(self.client_address[0])
			print self.data.strip()
			self.request.send(self.data)
			if self.data.strip() == "close":
				self.request.close();
				return			

	def finish(self):
		print self.client_address, "disconnected"
		

if __name__ == "__main__":
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
