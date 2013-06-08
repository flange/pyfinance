import socket
import sys


class Client:
	"""
	Representation of player. A client can contact the PyFinance server
	to login and then interact with it to make his transactions.
	"""
	pass

HOST, PORT = "87.170.105.193", 61234
#HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	# Connect to server and send data
	sock.connect((HOST, PORT))
	sock.sendall(bytes(data + '\n', "utf-8"))

	# Receive data from the server and shut down
	received = str(sock.recv(512), "utf-8")

finally:
	sock.close()



#print("Sent:     {}".format(data))
#print("Received: {}".format(received))
