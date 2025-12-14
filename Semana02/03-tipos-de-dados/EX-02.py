#solicite ao usuário o mês do ano no formato numérico 1, 2, 3 ..12 e apresente o nome do ano.
#Exemplo: entrada 3 saída ‘Março’.
#**Implementar com Tupla**

meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

mes_numero = int(input("Digite o número do mês (1-12): "))
indice = mes_numero - 1
print(f"O mês correspondente é: {meses_do_ano[indice]}")