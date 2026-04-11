def carregar_dados_alunos(nome_arquivo):
    lista_alunos = []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                campos = linha_limpa.split(',')
                aluno = {
                    'prontuario': campos[0],
                    'nome': campos[1],
                    'email': campos[2]
                }
                lista_alunos.append(aluno)
                
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return ()
    except IndexError:
        print("Erro: O arquivo parece estar com o formato incorreto (faltando vírgulas).")
        return ()
    return tuple(lista_alunos)

resultado = carregar_dados_alunos("C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Exercicios/alunos.txt")

for aluno in resultado:
    print(aluno)

"""with open(...): Esta é a forma de abrir arquivos em Python. Ela garante que o arquivo seja fechado automaticamente, mesmo se ocorrer um erro durante o processamento.

strip(): Essencial para remover o caractere invisível de "quebra de linha" (\n) que fica no final de cada frase dentro do arquivo de texto.

split(','): Como o formato do arquivo é CSV (valores separados por vírgula), usamos este método para transformar a string única da linha em uma lista de strings individuais.

tuple(lista_alunos):é mais eficiente adicionar itens a uma lista (que é mutável) e, ao final, convertê-la para tupla (que é imutável), atendendo ao requisito da função."""