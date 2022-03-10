import socket

my_client=socket.socket()
my_client.connect(("192.168.0.179",1234))

while True:
    data=raw_input("Enter a command: ")
    my_client.sendall(data.encode())
    if data=="stop":
        break
    
my_client.close()

