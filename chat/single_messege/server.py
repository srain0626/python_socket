from socket import *

HOST = ''
PORT = 8080
ADDR = (HOST, PORT)
BUF_SIZE = 1024


s_S = socket(AF_INET, SOCK_STREAM)
s_S.bind(ADDR)
s_S.listen(100)

connectionSock, addr_info = s_S.accept() 

print((str(addr_info), "에서 접속했습니다"))

data = connectionSock.recv(BUF_SIZE)
print(data.decode("utf-8"))

connectionSock.send("I am a server.".encode("utf-8"))
print("I am a server 메시지를 보냈습니다.")