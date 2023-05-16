import socket

host  = input('\nInforme o nome do HOST ou URL do site: ')
port  = 80

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((host , port))

requisicao = f'GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
tcp_socket.sendall(requisicao.encode())

while True:
    dados = tcp_socket.recv(1024)
    if not dados: break
    print(dados.decode())

print('\n'+'-'*100)
print('Fim dos dados')

tcp_socket.close()