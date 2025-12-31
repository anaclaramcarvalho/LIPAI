def linha_para_dict(linha, chaves):
    valores = linha.strip().split(',')
    dicionario = {}
    for i in range(len(chaves)):
        chave = chaves[i]
        valor = valores[i]
        dicionario[chave] = valor
        
    return dicionario

"""EXEMPLOS"""
linha1 = "SP000001,Maria da Silva,maria@email.com"
chaves1 = ['prontuario', 'nome', 'email']
print("Saída Exemplo 1:", linha_para_dict(linha1, chaves1))

linha2 = "banana,3"
chaves2 = ['item', 'quantidade']
print("Saída Exemplo 2:", linha_para_dict(linha2, chaves2))