import socket
from random import randrange as rand

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

def gen_values():
    T = str(rand(0,150,1))
    P = str(rand(0,100,1))
    V = str(rand(0,50,1))
    R = str(rand(0,10,1))
    Q = str(rand(0,5000,1))
    data  = 'T|'+ T +'|P|' + P + '|V|' + V + '|R|' + R + '|Q|' + Q
    return data
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
#print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    #if not data: break
    #print "received data:", data
    #data = "T|110|P|50|V|32|R|11|Q|5000"
    if data == "R":
        data  = gen_values()
        conn.send(data)  # echo
    else:
        conn.send("255")  # echo
conn.close()
