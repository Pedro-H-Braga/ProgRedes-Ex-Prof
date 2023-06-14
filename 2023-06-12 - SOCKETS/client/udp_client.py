import socket
from socket_constants import *

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicitar o arquivo
    nome_arquivo = input('Digite o nome do arquivo (EXIT p/ sair): ')
    
    # Enviando o nome do arquivo para o servidor
    print(f'\nSolicitando o arquivo {nome_arquivo}')
    udp_socket.sendto(nome_arquivo.encode(CODE_PAGE), (HOST_SERVER, SOCKET_PORT))
    
    if nome_arquivo.upper() == 'EXIT': break

    # Recebendo o conteúdo do servidor
    dado_retorno, ip_retorno = udp_socket.recvfrom(BUFFER_SIZE)

    # Gravar o dado recebido em arquivo
    print(f'Gravando o arquivo {nome_arquivo}')
    arquivo = open(nome_arquivo, 'wb')
    arquivo.write(dado_retorno)
    arquivo.close()

# Fechando o socket
udp_socket.close()