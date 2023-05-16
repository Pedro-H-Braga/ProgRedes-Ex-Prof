import socket

url_host    = 'httpbin.org'
url_image   = '/image/png'
url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

host_port   = 80
buffer_size = 512

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, host_port))
sock_img.sendall(url_request.encode())

print('-'*100)

while True:
   dados = sock_img.recv(buffer_size)
   if not dados: break
   print(dados)

print('-'*100)

sock_img.close()