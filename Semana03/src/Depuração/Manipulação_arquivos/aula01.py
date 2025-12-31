arquivo = open("C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Manipulação_arquivos/teste.txt", "r")
#print(arquivo.readable())
#print(arquivo.read())
#print(arquivo.readline())
#lista = arquivo.readlines()
#print(lista)
#print(lista[3])

# arquivo = open("C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Manipulação_arquivos/teste.txt", "a")
# arquivo.write("C\n")
# arquivo.write("Terraform\n")

#arquivo = open(""C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Manipulação_arquivos/teste2.txt", "w")

# arquivo = open("C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Manipulação_arquivos/teste3.txt", "x")
# arquivo.write("python\n")
# arquivo.write("Terraform\n")

#arquivo.close()

import os
# if os.path.exists("C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Manipulação_arquivos/teste3.txt"):
#     "se existir ele remove"
#     os.remove("C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Manipulação_arquivos/teste3.txt")
# else:
#     print("Arquivo não existe")

os.rmdir("C:/Users/anacl/OneDrive/Documents/UFU/LIPAI/Semana03/src/Depuração/Manipulação_arquivos/novo_arquivo")