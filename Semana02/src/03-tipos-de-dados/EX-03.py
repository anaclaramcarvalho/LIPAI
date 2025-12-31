#solicite ao usuário o mês do ano no formato numérico 1, 2, 3 ..12 e apresente o nome do ano.
#Exemplo: entrada 3 saída ‘Março’.
#**Implementar com Dicionário**

meses_do_ano = {1: "Janeiro",2: "Fevereiro",3: "Março",4: "Abril",5: "Maio",6: "Junho",7: "Julho",8: "Agosto",9: "Setembro",10: "Outubro",11: "Novembro",12: "Dezembro"}

try:
    mes_numero = int(input("Digite o número do mês (1-12): "))

    nome_do_mes = meses_do_ano.get(mes_numero)

    if nome_do_mes:
        print(f"O mês número {mes_numero} é: {nome_do_mes}")
    else:
        print("Erro: Número do mês inválido. Por favor, digite um valor entre 1 e 12.")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite apenas um número.")