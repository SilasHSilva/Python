'''
Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos 
da diagonal principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação 
'''
matriz = []

for lin in range(3):
    linha = []
    for col in range (3):
        linha.append(int(input("Digite um elemento da matriz: ")))
    matriz.append(linha)

for lin in range(3):
    print(matriz[lin])

k = int(input("Digite o valor da k: "))

for lin in range(3):
    linha = []
    for col in range (3):
        if(lin == col): #condição para o elemento da matriz estar na diagonal principal 
            matriz[lin][col] = matriz[lin][col] * k

for lin in range(3):
    print(matriz[lin])