# Diretório é igual pasta
# Repositorio está relacionado a git e não tem nada com linha de comando, ele é uma aplicação que controla versão
# Bash é o terminal de comando mais famoso
# Git não é o shell é um comando do shell
# CTR+C -> terminar o comando anterior
# SETA CIMA BAIXO -> ver comandos que você digitou anteriormente
# TAB -> completa o comando ou pasta que vcoê esta tentando digitar
# CTRL + R -> busca no historico de comandos ou use historyi grep "comando"
# CTRL + L OU CLEAR-> limpa a tela
# CTRL + A / CTRL + E -> vai para o inicio da linha ou fim da linha
# CTRL + K -> apaga do ponto que está até o final
# CAT -> lista o arquivo inteiro do inicio ao fim no terminal pode ser usado também para escrever no arquivo
# MORE -> para arquivos maiores você pode usá-los para navegar para frente com enter ou espaços para sair 'q'
# LESS -> parecido com o 'more' mas permite navegar para frente ou para tras .Você pode usar enter , espaço para ir para frente ou ainda setas para cima e para baixo além das teclas j e k para sair esc e depois q ou :q
# LEITURA DO LIVRO
# -CAP 01-
# date - mostra a data e hora atuais do sistema.
# uptime - mostra há quanto tempo o sistema está ligado, número de usuários logados e carga média.
# df - mostra o uso de espaço em disco de todas as partições montadas.
# free - exibe o uso de memória RAM e swap.
# exit - encerra a sessão do terminal ou fecha um script.
# reset- restaura o terminal caso ele “bugue” ao exibir arquivos binários.

# -CAP 02-
# pwd - mostra o diretório atual onde você está.
# cd - muda o diretório atual.
# cd - vai para o diretório pessoal (home)
# cd .. - volta um diretório
# cd - - volta ao diretório anterior
# cd /caminho/inteiro - caminho absoluto
# cd pasta - caminho relativo
# ls - lista arquivos e diretórios.
# ls -l - formato longo, mostra permissões, dono, tamanho, datas
# ls -a - mostra arquivos ocultos (nomes que começam com .)
# ls /caminho - lista outro diretório
# ls -t - ordena por data
# ls -r - ordem reversa
# ls -h - exibe tamanhos em formato “humano” (KB, MB...)
# ls -F - adiciona indicadores aos arquivos (ex: / para diretórios)

# -CAP 03-
# file -mostra qual é o tipo de um arquivo (texto, imagem, binário, script etc.).
# less - abre arquivos texto para leitura com rolagem.
# q - sair
# /texto - busca
# n - próximo resultado
# G - final
# g - início

# -CAP 04-
# Wildcards
#  operadores usados com comandos como ls, rm, cp:
# * - qualquer sequência
# ? - um único caractere
# [abc] - conjunto específico
# [a-z] - intervalo
# {a,b,c} - expansão de lista
# mkdir - cria diretórios.
# cp - copia arquivos ou diretórios.
# cp -r pasta destino → copiar diretórios recursivamente
# mv -move ou renomeia arquivos e diretórios.
# rm -remove (apaga) arquivos.
# ln- cria links (atalhos) entre arquivos.

# -CAP 05-
# type -mostra o tipo de um comando (alias, função, bui ltin, executável etc.).
# which - mostra o caminho completo de um comando executável no sistema.
# help - mostra ajuda de comandos internos do shell (builtins) como cd, echo, pwd.
# help -mostra a ajuda rápida de um programa externo.
# man - abre a página de manual do comando.
# apropos -busca comandos relacionados a uma palavra-chave.
# whatis - mostra uma descrição curta de um comando.
# info - outro sistema de documentação (mais detalhado que o man para algumas ferramentas GNU).
# alias - cria atalhos personalizados para comandos.
