from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)     # 소켓 생성
clientSocket.connect(('222.121.116.159', 8080)) # 소보애 접속하기 위한 connect((호스트주소, 포트))

