import socket, sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005 # Defines server port
MESSAGE = "Hello, World!"
LISTEN_PORT = 5006 # Defines client port

def print_man():
    print "LT - returns temperature value"
    print "LP - returns pressure value"
    print "LV - returns flow value"
    print "qc - terminates client"
    print "qs - terminates server"



sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, LISTEN_PORT))

print "Type 'man' for a command list"
while True:
    MESSAGE = raw_input()
    if MESSAGE == "man":
        print_man()
    elif MESSAGE == "qc":
        sys.exit()
    else:
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(4) # buffer size is 4 bytes
        # print the data received from serve
        print data
