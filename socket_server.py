import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_socket(sock, addr):
    while True:
        data = sock.recv(1024)
        data = data.decode('utf8')
        print(data)
        if data == '2':
            break
        re_data = input()
        sock.send(re_data.encode('utf8'))
    sock.close()
    server.close()


while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_socket, args=(sock, addr))
    client_thread.start()
    # sock.send('hello {}'.format(data.decode('utf8')).encode('utf8'))
    # server.close()
    # sock.close()