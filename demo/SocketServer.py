from socket import *

udp_sock=socket(AF_INET, SOCK_DGRAM)
sendAddr=("192.168.1.88","8080")

udp_sock.sendto("hello world!",sendAddr)


udp_sock.close()

