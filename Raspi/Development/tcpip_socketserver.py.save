import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		self.data = self.request.recv(1024).strip()
		print "{} wrote:".format(self.client_address[0])
		print self.data
		self.request.sendall(self.data)

if __name__ == "__main__":
	HOST, PORT = "192.168.1.1",8000

	server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
	
	server.serve_forever()
