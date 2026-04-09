import numpy as np

#O que é um array?
#É um conjunto de dados que pode estar disposto em dimensões diferentes
#Tipos de arrays: ndarrays -> significam arrays com N dimensões
#   1-D array -> Possui apenas uma dimensão. Será comumente chamado de vetor ou vector
#   2-D array -> Possui 2 dimensões. Será comumente chamado de matriz oou matrix
#   3-D ou Mais array -> Possui 3 ou mais dimensões. Será comumente chamado de tensor#

#Criando um Array -> np.array()
a = np.array([1,2,3,4,5,6])
print(a)
#print(type(a))
b = np.array([[1,2,3,4,5,6],[6,5,4,3,2,1]])
print(b)

#   Criar matriz com diagonal  0 -> np.zeros()
zero_arrays = np.zeros(shape = (5,3,6))
print(zero_arrays)

#   Criar matriz com diagonal 1 -> no.ones()
um_array = np.ones(2)
print(um_array)
um_array2 = np.ones((2,3))
print(um_array2)

#   Criar porém nenhum valor vai ser vazio então ele coloca numeros aleatorios-> np.empty()
vazio = np.empty(3)
print(vazio)

#   Criar  com um pouco mais de informação-> np.arange()
arr = np.arange(10)
print(arr)
arr2 = np.arange(50,200,30)
print(arr2)

#   Criar valores baseado em sequencias 
#       A np.linspace() cria em sequencia linear
array_linear = np.linspace(0, 100 , num = 20, endpoint = False, retstep = True)
print(array_linear)

#Descobrindo o tamanho do array
# Números de dimensões e número de itens
zero_array = np.zeros(shape = (5,3,6))
print(zero_array)
print(zero_array.shape) #Formato
print(zero_array.size) #Tamanho
print(zero_array.ndim) #Número de dimenções

#   Mudando o tamanho de um array

#Rankeando um array

#Transformando um vetor (1D) em uma matriz(2D)
#   .newaxis
#   .expand_dims
a = np.array( [ 1, 2, 3])
print(a.shape)
print(a.ndim)

a2 = a[np.newaxis,:] #Criar uma nova dimenção dentro de a no primeiro item da lista
print(a2.shape)
print(a2.ndim)
print(a2)

a22 = a[:,np.newaxis]
print(a22.shape)
print(a22)

a22[2][0] = 2
print(a22)

#Concatenando Arrays
a = np.array( [1, 2, 3])
b = np.array( [4, 5, 6])

c=np.concatenate((a,b))
d=np.concatenate((b,a))

print(c)
print(d)

#Consultando itens de um array -> logica e pode fazer consulta caso tenha muitos dados
a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print('------------')
maior_8 = a[a<8]
print(maior_8)

#Operações com array
a = np.array( [1, 2, 3])

print(a.max()) #Valor máximo
print(a.min()) #Valor mínimo
print(a.mean()) #Média
print(a.sum()) #Soma

#Gerando amostras aleatórias
from numpy.random import default_rng
rng= default_rng()
aleatorio = rng.integers(10, size=(2,4))
print(aleatorio)

#Diferença entre array e lista
e = np.array([1,3,4,5,6,5,7,8])
print("Essa é o array 'e':",e)
print("Esse é tipo de 'e':",type(e))
print('-------------------------------------')
lista_e=[1,3,4,5,6,5,7,8]
print("Essa é a 'lista_a':", lista_e)
print("Esse é tipo de 'lista_a':",type(lista_e))

#   arrays não permitem tipos de dados distintos:
f = np.array([1,'Daniel',2,3,4,5,6,7,8])
print(f)
print(type(f[0]))

#   já as listas sim:
lista_g = [1,'Daniel',2,3,4,5,6,7,8]
print(lista_g)
print(type(lista_g[0]))

#Comparando o processamento
from time import process_time
lista_a = list(rng.integers(10, 100, 10000000))
print(type(lista_a))
lista_b = list(rng.integers(10, 100, 10000000))
#ab= []
#ab = lista_a*lista_b

print(type(lista_a))
print(len(lista_a))

h=[]
t1 = process_time()
for i in range(len(lista_a)):
    h.append(lista_a[i] * lista_b[i])
t2 = process_time()
print(t2-t1)

i = rng.integers(10, 100, 10000000)
j = rng.integers(10, 100, 10000000)
print(type(i))
print(i)
t1i=process_time()
c=i*j
t2i=process_time()
print(t2i-t1i)

import matplotlib.pyplot as plt
dados_x = rng.integers(20, size = 30)
dados_y = rng.integers(12, size = 30)
plt.scatter(x = dados_x, y = dados_y)
plt.show()