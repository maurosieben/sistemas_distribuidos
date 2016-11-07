import socket, time
from datetime import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "B"
#hour = datetime.now().time()

def check_data(data):
    count = 0; 
    for value in data:
        if value == 'T':
            print "Temperatura: %s oC" %data[count+1]  
        elif value == 'P':
            print "Pressao: %s bar" %data[count+1] #" bar"
        elif value == 'V':
            print "Vazao: %s l/min " %data[count+1] #" l/s"
        elif value == 'R':
            print "Receita: ", data[count+1] 
        elif value == 'Q':
            print "Quantidade: ", data[count+1] 
        else:
            pass
        count = count+1
    print "At: ", time.strftime("%H:%M:%S") #datetime.now().time() 
    print "\n"

    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while(1):
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print "Cliente:", TCP_IP
    if data == '255':
        print "ID not found"
    else:   
        data = data.split('|')
        check_data(data)
    time.sleep(2)
s.close()

