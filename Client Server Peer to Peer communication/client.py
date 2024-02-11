# Import socket module
import socket, pickle		

# Create a socket object
s = socket.socket()
clientAdress = ('127.0.0.1', 11122)
s.bind(clientAdress)

ip = '127.0.0.1'
port = 12345

addr = (ip, port)

# Define the port on which you want to connect
		

# connect to the server on local computer
s.connect(addr)

# receive data from the server and decoding to get the string.
print (pickle.loads (s.recv(11122)))
data = pickle.dumps('hi')
s.sendto(data, addr)
# close the connection
s.close()