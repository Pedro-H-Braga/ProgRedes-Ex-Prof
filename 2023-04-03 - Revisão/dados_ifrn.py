import requests

url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

dados = requests.get(url).json()

print(dados[0])

# Questão 01: Listar os campus e a sua quantidade de alunos


# Questão 02: Solicitar a sigla de um campus e listar os cursos do
#             campus e a quantidade de alunos de cada curso 

