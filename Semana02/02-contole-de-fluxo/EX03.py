'''O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X. Exemplos válidos: BR0001X BR1236X BR9999X; Exemplos inválidos: br0001X BR126X BR99999X BR9999Y; Crie um programa em python que solicita ao usuário um identificador e apresenta se o que foi informado é um valor válido ou inválido.'''

identificador = input('Digite o código do seu identificador: ')


if len(identificador) != 7:
    print(f'O identificador "{identificador}" é INVÁLIDO.')

elif not identificador.startswith('BR'):
    print(f'O identificador "{identificador}" é INVÁLIDO.')

elif not identificador.endswith('X'):
    print(f'O identificador "{identificador}" é INVÁLIDO.')
else:
    part_numerica = identificador[2:6]

    if not part_numerica.isdigit():
        print(f'O identificador "{identificador}" é INVÁLIDO.')
    else:
        numero = int(part_numerica)
        if 1 <= numero <= 9999:
            print(f'O identificador "{identificador}" é VÁLIDO')
        else:
            print(f'O identificador "{identificador}" é INVÁLIDO.')
