from socket import *

from multiprocessing import Process
import re

HTML_ROOT_URL = "./html"


def handle_client(client_socket):
    """处理客户端请求"""
    # 接受客户端请求
    request_data = client_socket.recv(1024)
    print(request_data)

    # 获取客户端请求什么资源
    lines = request_data.splitlines()
    file_name = re.match(r"\w+ +(/[^ ]*) ", lines[0].decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/index.html"
    # 本地获取资源
    try:
        file = open(HTML_ROOT_URL + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 NOT Found\r\n"
        response_header = "server: Dinson server\r\n"
        response_body = "This file is not found"
    else:
        file_data = file.read()
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_header = "server: Dinson server\r\n"
        response_body = file_data.decode("utf-8")

    response = response_start_line + response_header + "\r\n" + response_body

    client_socket.send(bytes(response, "utf-8"))
    client_socket.close()


if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("", 8000))
    server_socket.listen(128)
    while True:
        client_socket, client_address = server_socket.accept()
        p = Process(target=handle_client, args={client_socket, })
        p.start()
        client_socket.close()
