"""Aula 05 - Tipos de dados"""

# Númericos
# int , float
idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# String
nome = 'Pedro'
sobrenome = 'dos Santos'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Coca -cola'
print(f'O cliente {nome} {sobrenome} comprou o produto { produto}')

print(nome[0], nome[-1])
print(nome.lower())
print(nome.upper())
