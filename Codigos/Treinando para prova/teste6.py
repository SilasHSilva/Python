'''
Escreva um programa em Python para ler uma matriz 3X6 de números reais. 
Em seguida, quando houver números negativos, troque-os pelo número 1. Por fim, mostre a matriz atualizada.
'''

matriz = []


for lin in range(2):
    linha = []
    for col in range(2):
        element = (float(input("Digite um elemento da matriz: ")))
        if element < 0:
            linha.append(1)
        else:
            linha.append(element)
    matriz.append(linha)

for lin in range(0,2):
    print(matriz[lin])
