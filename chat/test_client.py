import socket, threading
import tkinter as tk



client_socket = None    # 서버와 1:1 통신할 소켓
label = None
Msg = None
root = None

def send(e):    # 이벤트 핸들러 함수, 엔트리 엔터 입력시 호출.
    global client_socket

    msg = Msg.get() # 입력박스에 입력한 텍스트 읽어옴
    client_socket.sendall(msg.encode())
    Msg.delete(0, tk.END)

def th_read():
    global client_socket
    while True:
        data = client_socket.recv(1024)
        msg = data.decode()
        label.configure(text = label.cget('text') + '\n' + msg)
        if msg == '/stop':
            break

    print('서버 메시지 출력 쓰레드 종료')