#!/usr/bin/python3    #This is server.py file

import socket

#Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()

port = 9999

#bind to the port
serversocket.bind((host, port))

#queue up to 5 requests 
serversocket.listen(5)
#print("Server running now and waiting for connection")

while True:
	#establish a connection 
	clientsocket, addr = serversocket.accept()
	
	#print("Got a connection from %s", % str(addr))
	print("Got a connection from {0}".format(str(addr)))
	
	msg = "Thank you for connecting " + "\r\n"
	clientsocket.send(msg.encode('ascii'))
	clientsocket.close()
	
	
