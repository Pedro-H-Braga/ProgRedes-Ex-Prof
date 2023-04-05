import requests

url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

dados = requests.get(url).json()


# Questão 01: Listar os campi e a sua 
# quantidade de alunos
campi = set(map(lambda c: c['campus'], dados))
for campus in campi:
    filtro = lambda c: c['campus'] == campus
    alunos = list(filter(filtro, dados))
    qt_alunos = len(alunos)
    print(f'Campus {campus}: {qt_alunos} Alunos')


# Questão 02: Solicitar a sigla de um campus e listar os cursos do
#             campus e a quantidade de alunos de cada curso 

