from socket import *
from sys import call_tracing

HOST = "222.121.116.159"
PORT = 8080
ADDR = (HOST, PORT)
BUF_SIZE = 1024

c_S = socket(AF_INET, SOCK_STREAM)
c_S.connect(ADDR)


print("연결에 성공하였습니다.")
c_S.send("I am a client".encode("utf-8"))

print("I am a client 메시지를 전송했습니다.")

data = c_S.recv(BUF_SIZE)
print("받은 데이터: ", data.decode("utf-8"))
