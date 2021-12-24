from socket import *
import threading
import time


def send(sock):
    sendData = input(">>>")
    sock.send(sendData.encode("utf-8"))

def receive(sock):
    while True:
        recvData = sock.recv(BUF_SIZE)
        print("상대방: ", recvData.decode("utf-8"))


HOST = ''
PORT = 8080
ADDR = (HOST, PORT)
BUF_SIZE = 1024

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(ADDR)
serverSock.listen(100)

print("%d번 포트로 접속 대기중"%PORT)

connectionSock, addr_info = serverSock.accept()

print(str(addr_info), "에서 접속되었습니다")

sender = threading.Thread(target=send, args=(connectionSock,))      # send 함수를 인자로 넣어 쓰레드 생성
reciever = threading.Thread(target=receive, args=(connectionSock,)) # receive 함수를 인자로 넣어 쓰레드 생성

sender.start()
reciever.start()

while True: #프로그램 계속 실행
    time.sleep(1)
    pass
