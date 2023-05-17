# Exemplo da criação de uma lista com 10 números inteiros

lista_numeros = [2, 5, 7, 8, 11, 15, 4, 1, 8, 6]
#       indice   0  1  2  3  4   5   6  7  8  9

print(f"Lista inteira: {lista_numeros}")

# Exibir um elemento da lista

print(f"Elemento do indice 5 da lista (sexto elemento): {lista_numeros[5]}")

# Saber qual o indice que o elemento esta armazenado

print(f"Indice que o elemento 11 esta armazenado: {lista_numeros.index(11)}")

# Acessar elementos dentro de um intervalo
print(f"Exibe os elementos do indice 1 (segundo elemento) ate o quarto elemento elemento: {lista_numeros[1:4]}")

# Retornar se um elemento está na lista

num = 13

if (num in lista_numeros):
    print("O numero esta na lista")
else:
    print("O numero nao esta na lista")

# Inserção de um elemento no final da lista

lista_numeros.append(13)

print(lista_numeros)

lista_numeros.insert(4,18)
print(lista_numeros)

# Remoção de um elemento da lista

lista_numeros.pop()

print(lista_numeros)

# Tamanho da lista

print(f"Tamanho da lista: {len(lista_numeros)}")

# Lista com tipos de dados heterogeneos

lista_pessoa = ["Maria", 20, 1.56]

print(lista_pessoa)





