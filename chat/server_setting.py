from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)      # 소켓 생성

serverSocket.bind(('', 8080))                    # bind-server 에서만 필요, 튜플 형식이라 (())이고 ip, port가 한 쌍

serverSocket.listen(1)                           # 1개의 동시 접속만 허용

clientSocket, addr = serverSocket.accept()       # 누가 접속할 때까지 대기

