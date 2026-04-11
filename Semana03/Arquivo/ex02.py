""" crie a função carregar_dados_projetos que recebe como parâmetro o nome de um arquivo que contém dados de projetos e retorna uma tupla, onde cada elemento é um dicionário com as seguintes chaves: codigo (número inteiro que representa o código do projeto), titulo e responsável (nome do professor responsável pelo projeto)."""
def carregar_dados_projetos(arquivo):
    with open(arquivo, 'r') as arq:
        projetos = []
        for linha in arq :
            linha = linha.strip()
            if not linha : continue
            dados = linha.split(',')
            if len(dados) == 3:
                projeto = {
                    'Codigo' : int (dados[0].strip()),
                    'Titulo' : dados[1].strip(),
                    'Responsavel' : dados[2].strip()
                }
                projetos.append(projeto)
    return tuple(projetos)

tupla = carregar_dados_projetos('projeto.txt')
print(tupla)