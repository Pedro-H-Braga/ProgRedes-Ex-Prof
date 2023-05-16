import socket

url_host    = 'www.httpbin.org'
url_image   = '/image/png'
url_request = f'HEAD /{url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

host_port   = 80
buffer_size = 1024

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, host_port))
sock_img.sendall(url_request.encode())

print('-'*100)
dados = sock_img.recv(buffer_size)
print(str(dados, 'utf-8'))
print('-'*100)

sock_img.close()