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
sigla_campus = input('Informe a Sigla do Campus: ').upper()

if sigla_campus in campi:
    filtro = lambda c: c['campus'] == sigla_campus
    alunos = list(filter(filtro, dados))
    cursos = set(map(lambda c: c['curso'], alunos))
    for curso in cursos:
        filtro = lambda c: c['curso'] == curso
        alunos_curso = list(filter(filtro, alunos))
        qt_alunos = len(alunos_curso)
        print(f'Curso {curso}: {qt_alunos} Alunos')
else:
    print('Não existe esse campus...')

# Exercício: Gerar arquivo com os dados da questão 02, 
# cada curso em uma linha, separando o nome do curso da
# quantidade de alunos por ; 