"""crie uma função que recebe vários argumentos numéricos através do *args retorna a soma dos números"""
def soma(*args):
    s = 0
    for num in args:
        s = s + num
    return s


resultado = soma(10, 9, 8, 7, 6, 5)
print("Soma =", resultado)