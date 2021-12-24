import socket, threading

soc_list = []   # 채팅방. 연결된 클라이언트 소켓

def client(soc, addr):
    soc_list.append(soc)    # 방금 접속한 클라이언트 소켓을 리스트에 담음

    while True:
        data = soc.recv(1024)
        msg = data.decode()
        if msg == '/stop':
            soc.sendall(data)   # 본인한테 /stop 전송
            soc_list.remove(soc)
            msg = str(addr) + ' 님이 퇴장하셨습니다. '
            for s in soc_list:
                s.sendall(msg.encode())
            break
        else:
            print('Received from ', addr, msg)
            msg = str(addr) + ' : ' + msg
            for s in soc_list:
                s.sendall(msg.encode())
        soc.close()
        print(addr, '퇴장')

def main():
    HOST = ''
    PORT = '8080'
    INFO = (HOST, PORT)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 포트 여러번 바인드하면 발생하는 에러 방지

    server_socket.bind(INFO)
    server_socket.listen()

    print('서버 시작')
    # accept로 client의 접속을 기다리다 요청시 처리.
    # client와 1:1 통신할 작은 소켓과 연결된 상대방의 주소 반환

    while True:
        client_socket, addr = server_socket.accept()
        print("Connected by", addr)
        thread = threading.Thread(target = client, args = (client_socket, addr))

    server_socket.close()

main()