import sys
import socket


#Creating a INTET and Streaming socket with TCP Protocol
#The port number is defined for the test is 7272. This is arbitrary
#The host IP address will be the server address to which client will be connected and in this case IP of Kyle's PC

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=7272
host='192.168.1.249'

#Command to connect with server using IP AND PORT
client_socket.connect((host, port))
print("Connected to Kyle's PC")
print("\nBut it probably killed the host immediately because it is a test")
