import sys
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 7272
host = '10.166.208.171'
server = (host, port)

client_socket.connect((host, port))

message = input("-> ")
while message != 'q':
      client_socket.sendto(message.encode('utf-8'), server)
      data, addr = client_socket.recvfrom(1024)
      data = data.decode('utf-8')
      print("Received from server: " + data)
      message = input("-> ")
client_socket.close() 
