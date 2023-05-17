'''
Escreva um programa para ler uma matriz A com 8 linhas e 6 colunas. 
Construir uma lista B que seja formado pela soma de cada linha da matriz A. 
Ao final apresentar o somatório dos elementos da lista B.
'''

matriz = []

for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(int(input("Digite um elemento da matriz: ")))
    matriz.append(linha)

for lin in range(3):
    print(matriz[lin])

listaB = []

for lin in range(3):
    lin_soma = 0
    for col in range(3):
        lin_soma += matriz[lin][col]
    listaB.append(lin_soma)

print(listaB)

