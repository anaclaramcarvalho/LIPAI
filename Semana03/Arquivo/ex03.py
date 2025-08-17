"""om base nos códigos dos exercícios anteriores, crie a função linha_para_dict que recebe uma linha do arquivo (string), exemplo SP000001,Maria da Silva,maria@email.com , uma lista com os nomes das chaves do dicionário ['prontuario', 'nome', 'email'] e retorna o dicionário correspondente à aquele registro. Não utilizar bibliotecas ou funções prontas para leitura do arquivo. """
def linha_para_dict(linha, colunas):
    partes = [p.strip() for p in linha.split(',')]

    if len(partes) != len(chaves):
        raise ValueError("Número de partes não corresponde ao número de chaves")

    return {chave: parte for chave, parte in zip(chaves, partes)}

linha = "SP000001, Maria da Silva,maria@email.com"
chaves = ['prontuario', 'nome', 'email']
registro = linha_para_dict(linha, chaves)
print(registro)