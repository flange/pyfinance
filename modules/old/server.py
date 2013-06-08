import socket
import threading
import socketserver

import helper


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	"""
	Server-side object that contains handler functions which determine
	how to handle incoming client requests.
	"""

	def handle(self):
		"""
		Bread & butter of our server. Defines what happens with a
		client request, which means parsing the request, filtering it
		for commands and then executing them.
		"""

		data = str(self.request.recv(1024), 'utf-8')

		timestamp = helper.Helper.get_timestamp()


		if (data == 'shutdown\n'):
			print(timestamp, "Shutting down")
			server.shutdown()
		elif (data != '\n'):
			print(timestamp, data)




class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	"""
	Wrapper class needed to set up a threaded TCP Server.
	"""
	pass




class Server:
	"""
	Our PyFinance server. It periodically fetches the stock prices from
	Yahoo Finance and handles the clients/players accounts as well as
	their actions on those accounts.
	"""
	pass



if __name__ == "__main__":

	HOST, PORT = "localhost", 9999

	server = ThreadedTCPServer((HOST, PORT),
	         ThreadedTCPRequestHandler,
	         False)                          # don't bind & activate yet

	server.allow_reuse_address = True        # keep port from blocking
	server.server_bind()                     # now bind and activate
	server.server_activate()


	server_thread = threading.Thread(target=server.serve_forever)
	server_thread.daemon = True              # main dies -> server dies

	server_thread.start()
	print("Server running.")

	server_thread.join()                     # main waits for server
