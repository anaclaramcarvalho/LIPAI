'''Implemente o `ex03.py` mas ao final do programa deve ser apresentado ao usuário todos os problemas que o identificador informado possui (implementar como list de erros):
    - Ex: identificador informado: B9999999X
        - erros
            - O identificar não inicia com a sequencias ‘BR’
            - O identificador não apresenta números inteiros entre 0001 e 9999
    - Ex: identificador informado: BR9999Y
        - erros
            - O identificar não finaliza com o caracter X'''


def validar_identificador(identificador):
    lista_de_erros = []

    if not identificador.startswith('BR'):
        lista_de_erros.append(
            'O identificador não inicia com a sequência "BR".')

    if not identificador.endswith('X'):
        lista_de_erros.append(
            'O identificador não finaliza com o caractere "X".')

    if len(identificador) != 7:
        lista_de_erros.append(
            'O identificador deve ter exatamente 7 caracteres.')
    else:
        part_numerica = identificador[2:6]
        if not part_numerica.isdigit():
            lista_de_erros.append(
                'A parte central (entre "BR" e "X") deve conter apenas 4 dígitos numéricos.')
        else:
            numero = int(part_numerica)
            if not (1 <= numero <= 9999):
                lista_de_erros.append(
                    f'O número "{part_numerica}" está fora do intervalo permitido (0001 a 9999).')

    return lista_de_erros


codigo_informado = input("Digite seu código identificador: ")

erros = validar_identificador(codigo_informado)

if not erros:
    print(f'\nO identificador "{codigo_informado}" é VÁLIDO.')
else:
    print(f'\nO identificador "{codigo_informado}" é INVÁLIDO.')
    print("Problemas encontrados:")
    for erro in erros:
        print(f'  - {erro}')
