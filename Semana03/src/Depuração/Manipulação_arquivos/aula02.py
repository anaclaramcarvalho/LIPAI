arq = open("teste.txt","w")
print(arq)

string = "ola Ana!"
x = ["ola", "Ana","!"]
#arq.write(x)#uma string
arq.writelines(x)#interavel de string

for nome in x:
    arq.write(nome + '\n')

arq.close()

with open('arquivo.txt', 'w') as arq:
    arq.write('teste')
    print('fim')

with open('arquivo.txt', 'a') as arq:
    arq.write('\nCaio')

with open('arquivo.txt', 'r') as arq:
    x = arq.read()#let tudo e trazer em uma string
    arq.readline()

with open('arquivo.txt', 'rB') as arq:
    x = arq.read()
    print(x)