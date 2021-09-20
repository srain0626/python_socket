from socket import *
from select import *
import sys
from time import ctime
from typing import Collection


HOST = '222.121.116.159'
PORT = 8080
BUF_SIZE = 1024
ADDR = (HOST, PORT)

clientSocket = socket(AF_INET, SOCK_STREAM) # 1. 서버에 접속하기 위한 소켓을 생성

try:
    clientSocket.connect(ADDR)              # 2. 서버에 접속을 시도
except Exception as e:
    print("%s:%s %ADDR")
    sys.exit()

print("연결 성공")

"""
1. 소켓을 생성하는 것으로부터 시작, clientSocket은 이제 socket 클래스의 인스턴스
2. connet 함수를 호출하여 서버 접속을 시도
"""