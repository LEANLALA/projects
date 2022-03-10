import socket
import RPi.GPIO as gpio
import time

server=socket.socket()
server.bind(("",1234))
server.listen(5)
print("Searching for clients...")
conn,addr=server.accept()
print("Client connected from address",addr)

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(8,gpio.OUT)

while True:
    data=conn.recv(1000)
    if data==b"on":
        gpio.output(8,True)
    elif data==b"off":
        gpio.output(8,False)
    elif data==b"blink":
        for i in range(10):
            gpio.output(8,True)
            time.sleep(0.4)
            gpio.output(8,False)
            time.sleep(0.4)
    else:
        break

conn.close()
server.close()

print("Client disconnected")
