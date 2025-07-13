''''Solicite ao usuário uma única a vez as notas no formato `n1, n2, n3, nm` e apresente o resultado da média aritmética das notas se está aprovado (maior que 6.0), recuperação (entre 4.0 e 6.0) ou reprovado (menor que 4.0).
    - Dica: utilize o método split da classe string para obter as notas como list
    - O programa deve funcionar independente do número de notas informadas pelo usuário, ex: 2 notas `10.0, 3.0` ou 5 notas `10.0, 3.0, 2.0, 5.6, 8.2`'''

notas = input('Digite as notas: ')
notas = notas.split(",")
notas = [float(nota) for nota in notas]

media = sum(notas)/len(notas)
print(f'A média resultante é: {media:.2f}')

if media >= 6.0:
    print("Aprovado")
elif 4.0 <= media < 6.0:
    print("Recuperação")
else:
    print("Reprovado")
