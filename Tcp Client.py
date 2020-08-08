#Tcp Client
import socket
host = "127.0.0.1"
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print s.sendto("Hello all", (host, port))
s.close()
