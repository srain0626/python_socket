from socket import *
from select import *
import sys
from time import ctime

HOST = '222.121.116.159'
PORT = 8080
BUF_SIZE = 1024
ADDR = (HOST, PORT)

severSocket = socket(AF_INET, SOCK_STREAM)  # 1. 소켓 생성

severSocket.bind(ADDR)                      # 2. 소켓 주소 정보 할당
print("할당 완료")

severSocket.listen(100)                     # 3. 연결 수신 대기 상태
print("대기 중")

clientSocket, addr_info, = severSocket.accept() # 4. 연결 수락
print("수락")

clientSocket.close()                        #소켓 종료
severSocket.close()
print("종료")

"""
1. 소켓을 생성, severSocket은 socket 클래스의 인스턴스
2. bind 함수를 호출하여 주소 정보인 ADDR을 할당
3. listen 함수를 호출하여 연결 수신 대기 상태를 만듦
4. 클라이언트가 연결을 하면 accept 함수를 이용하여 연결을 수락, 동시에 연결을 수라갛면서 연결 클라이언트와 송수신을 하는 소켓(clientSocket)을 하나 리턴 받음
5. close 함수를 호출하여 바로 종료 시킴
"""