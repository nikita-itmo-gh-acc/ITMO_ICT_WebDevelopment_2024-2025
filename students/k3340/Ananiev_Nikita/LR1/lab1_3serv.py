import sys
import socket

try:
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(('', 8888))
except socket.error:
    print('Failed to create socket')
    sys.exit()

max_conn_count = 5

serv_socket.listen(max_conn_count)
listening = True

while listening:
    conn_socket, addr = serv_socket.accept()
    request_msg = conn_socket.recv(1024).decode().split()
    if request_msg[0] != "GET":
        conn_socket.close()
        print("Invalid HTTP request")
        conn_socket.send(b'HTTP/1.1 400 Bad Request')
        conn_socket.close()
        break
    print(request_msg)
    with open('templates/index.html', 'r') as index:
        response = 'HTTP/1.1 200 OK\n' \
                   'Server: My own\n' \
                   'Content-Type: text/html; charset=utf-8\n' \
                   'Allow: GET\n\n' \
                   f'{index.read()}'
        print(response)
        conn_socket.send(response.encode('utf-8'))
        conn_socket.close()