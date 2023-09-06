# Criar uma nova lista baseado no dobro dos elementos de uma lista numérica com 5 valores

lista_A = []
lista_B = [] #lista nova

# Criação da lista A pelos dados digitados pelo usuario
for i in range (5):
    num = int(input("Digite um numero: "))
    lista_A.append(num)

# Criação da lista B pelo dobro dos elementos correspondentes da lista A
for i in range (5):
    dobro = lista_A[i] * 2
    lista_B.append(dobro)

print(lista_A)
print(lista_B)