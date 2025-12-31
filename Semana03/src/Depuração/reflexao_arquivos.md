01 - Qual a vantagem de transformar cada linha do arquivo em dicionários em vez de trabalhar apenas com strings? 
Trabalhar com dicionários oferece três vantagens principais:
Semântica e Clareza:Em vez de acessar um dado pela posição (ex: 'aluno[1]'), acessamos por uma chave nomeada (ex: 'aluno['nome']'). Isso torna o código muito mais legível e fácil de manter.
Facilidade de Manipulação:Com dicionários, podemos facilmente passar os dados de um aluno para outras funções, converter para JSON ou salvar em bancos de dados.
Isolamento da Lógica de Parse:Uma vez que a string foi convertida em dicionário, o restante do programa não precisa saber se o separador original era uma vírgula, um ponto-e-vírgula ou um espaço.

02 - Em que situações pode ser útil retornar uma tupla de registros (como nos exercícios ex01 e ex02) em vez de apenas uma lista de linhas? 

uso de tuplas e registros processados é ideal quando:
Imutabilidade e Segurança:Uma tupla é imutável. Ao carregar dados de um arquivo, geralmente queremos garantir que essa "foto" inicial dos dados não seja alterada acidentalmente por outras partes do código durante a execução.
Prontidão para Uso:Retornar uma lista de strings puras obrigaria qualquer outra parte do sistema a "quebrar" a string (usar '.split()') toda vez que precisasse de um dado. Ao retornar registros (dicionários) já processados, o dado está pronto para ser consumido (ex: exibir em uma interface ou filtrar por ID).

03 - O que você achou mais desafiador: ler o arquivo ou transformar as linhas em estruturas de dados (dicionários)?

Geralmente, o maior desafio é a transformação e validação das linhas. Enquanto a leitura do arquivo é um processo quase sempre padrão ('open', 'read', 'close'), a transformação exige:
Lidar com caracteres invisíveis (como o '\n' no final das linhas).
Garantir que cada coluna vá para a chave correta.
Tratar exceções, como linhas em branco ou campos faltando, que podem quebrar o programa se não forem previstos. 
A função genérica 'linha_para_dict' foi um passo importante para simplificar esse desafio, centralizando a complexidade em um único lugar.