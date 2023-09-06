# Lista criada a partir dos dados digitados pelo usuario

lista = []

for i in range (10):
    nome = input("Digite um nome: ")
    lista.append(nome)

for i in range (10):
    print (lista[i])

print("\n")

for nome in lista:
    print(nome)