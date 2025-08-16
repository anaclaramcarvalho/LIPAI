#solicite ao usuário 3 números, armazene esses elementos em uma lista e apresente no final o menor e maior elemento
numeros = []
for i in range(3):
    num = float(input(f"Digite o {i+1} numero:"))
    numeros.append(num)

menor_num = min(numeros)
maior_num = max(numeros)

print("\n--- Resultados ---")
print(f"A lista de números digitados é: {numeros}")
print(f"O menor elemento da lista é: {menor_num}")
print(f"O maior elemento da lista é: {maior_num}")