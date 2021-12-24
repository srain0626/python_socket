from socket import *
import threading
import time

def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode("utf-8"))


def recieve(sock):
    while True:
        recvData = sock.recv(BUF_SIZE)
        print("상대방: ", recvData.decode("utf-8"))

        
HOST = '222.121.116.159'
PORT = 8080
ADDR = (HOST, PORT)
BUF_SIZE = 1024

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(ADDR)

print('접속완료')

sender = threading.Thread(target=send, args=(clientSock,))
reciever = threading.Thread(target=recieve, args=(clientSock,))

sender.start()
reciever.start()

while True:
    time.sleep(1)
    pass


