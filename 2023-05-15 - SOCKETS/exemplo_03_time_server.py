import socket

# Como os servidores de horário podem mudar, 
# verificar umnovo servidor em  https://www.ntppool.org/en/

host = 'time.nist.gov'
port = 13

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect((host, port))
tcp_socket.sendall(b'')

print(str(tcp_socket.recv(4096), 'utf-8'))

tcp_socket.close()

