import socket, sys
from random import randrange as rand

UDP_IP = "127.0.0.1"
LISTEN_PORT = 5005 # defines server port
UDP_PORT = 5006 # defines client port

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, LISTEN_PORT))

# function to check data
def check_data(data):
    if data[0] == "L":
        print "Requisicao de leitura"
        if data[1] == "T":
            # creates a pseudo value to send
            temperatura = str(rand(0,100,1))
            sock.sendto(temperatura, (UDP_IP, UDP_PORT))

        elif data[1] == "P": 
            pressao = str(rand(1,8,1))
            sock.sendto(pressao, (UDP_IP, UDP_PORT))
            
        elif data[1] == "V":
            vazao = str(rand(2,7,1))
            sock.sendto(vazao, (UDP_IP, UDP_PORT))
            
        else:
            sock.sendto("NI", (UDP_IP, UDP_PORT))
            
    elif data[0] == "E":
        print "Requisicao de escrita"
        sock.sendto("E", (UDP_IP, UDP_PORT))

    elif data[0] == "q" and data[1] == "s":
        sys.exit()
    else:
        print "Requisicao invalida"
        sock.sendto("NA", (UDP_IP, UDP_PORT))
    

while True:
    data, addr = sock.recvfrom(4) # buffer size is 4 bytes
    data = list(data)
    check_data(data)
