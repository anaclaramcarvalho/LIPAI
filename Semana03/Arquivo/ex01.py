"""crie a função carregar_dados_alunos que recebe como parâmetro o nome de um arquivo que contém dados de alunos e retorna uma tupla, onde cada elemento é um dicionário"""
def carregar_dados_alunos(arq):
    with open(arq, "r") as file:
        alunos = file.readlines()
    dados_alunos = []
    for aluno in alunos:
        infos_aluno = aluno.split(",")
        dados = {
            'Prontuario': infos_aluno[0],
            'Nome': infos_aluno[1],
            'Email': infos_aluno[2]
        }
        dados_alunos.append(dados)
    return tuple(dados_alunos)

dados = carregar_dados_alunos("aluno.txt")
print(dados)