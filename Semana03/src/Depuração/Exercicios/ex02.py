def carregar_dados_projetos(nome_arquivo):
    lista_projetos = []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                campos = linha_limpa.split(',')
                projeto = {
                    'codigo': int(campos[0]), 
                    'titulo': campos[1],
                    'responsavel': campos[2]
                }
                
                lista_projetos.append(projeto)
                
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return ()
    except (ValueError, IndexError):
        print("Erro: Falha ao processar os dados. Verifique o formato do arquivo.")
        return ()

    return tuple(lista_projetos)

caminho = "C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Exercicios/projetos.txt"
resultado = carregar_dados_projetos(caminho)

for projeto in resultado:
    print(projeto)