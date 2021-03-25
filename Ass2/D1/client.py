'''    Simple socket server using threads
'''
import socket
import sys
HOST = 'cs2107-ctfd-i.comp.nus.edu.sg'   # Symbolic name, meaning all available interfaces
PORT = 2770 # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

s.connect((HOST, PORT))
print('Connected')
s.sendall(b'Hello, world')
print('Data Sent')
data = s.recv(1024)

print('Received', repr(data))
