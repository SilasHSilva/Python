nome = input("Digite seu nome e sobrenome: ")

nome_minusc = nome.lower()
print(nome_minusc)

tam = len(nome)

for i in range(tam):
    print(nome[i])

