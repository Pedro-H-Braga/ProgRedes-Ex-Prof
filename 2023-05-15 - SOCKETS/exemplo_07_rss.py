import socket, ssl, sys
import xml.etree.ElementTree as ET

# Constantes da Aplicação
RSS_SERVER   = 'agenciabrasil.ebc.com.br'
RSS_PATH     = '/rss/ultimasnoticias/feed.xml'
RSS_PORT     = 443
CODE_PAGE    = 'utf-8'
MAX_NOTICIAS = 10
BUFFER_SIZE  = 4096

# Construir requisição HTTP para obter o feed RSS
request  = f'GET {RSS_PATH} HTTP/1.1\r\n'
request += f'Host: {RSS_SERVER}\r\n'
request += 'User-Agent: Python\r\n'
request += 'Connection: close\r\n\r\n'

# Iniciar conexão segura com o servidor
context         = ssl.create_default_context()
socket_rss      = socket.create_connection((RSS_SERVER, RSS_PORT))
socket_rss_wrap = context.wrap_socket(socket_rss, server_hostname=RSS_SERVER)

# Enviar a requisição
socket_rss_wrap.send(request.encode(CODE_PAGE))

# Receber a resposta
retorno_noticias = ''
while True:
    resposta = socket_rss_wrap.recv(BUFFER_SIZE).decode(CODE_PAGE)
    if not resposta: break
    retorno_noticias += resposta

# Encontrar o início do conteúdo do feed RSS
posicao_inicial = retorno_noticias.find('<?xml')
posicao_final   = retorno_noticias.find('</rss>')

# Verificando se há conteúdo ma resposta do request
if (posicao_inicial == -1):
    print('Conteúdo do feed RSS inválido ou vazio.')
    sys.exit()

# Parsear o conteúdo do feed RSS
rss_content = retorno_noticias[posicao_inicial:posicao_final+6]

'''
file_output = open('saida.txt', 'w')
file_output.write(rss_content)
file_output.close()
'''

try:
    # Montando uma árvore com os elementos do XML de retorno
    root_rss = ET.fromstring(rss_content)
except ET.ParseError as e:
    print(f'Erro ao fazer o parse do XML: {e}')
except:
    print(f'Erro.....: {sys.exc_info()[0]}')
else:
    # Extrair as 10 notícias mais recentes
    noticias = root_rss.findall('.//item')[:MAX_NOTICIAS]
    # Imprimir as notícias
    for posicao, noticia in enumerate(noticias):
        titulo = noticia.find('title').text
        url    = noticia.find('link').text
        print(f'\nNOTÍCIA {posicao+1}')
        print(f'Título.: {titulo}')
        print(f'URL....: {url}\n')
