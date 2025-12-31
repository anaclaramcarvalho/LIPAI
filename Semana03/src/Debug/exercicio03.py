"""crie uma função que recebe uma tupla de números como parâmetro (numeros) e retorna a soma dos números"""

breakpoint() 
def soma(tupla_num):
    total = sum(tupla_num)
    return total

tupla_num = (4, 12, 7)
print(f"Os números são: {tupla_num} e sua soma é: {soma(tupla_num)}")