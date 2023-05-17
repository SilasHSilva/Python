'''
Faça um programa que leia uma matriz 3x3 de 
inteiros e retorne a linha de maior soma. 
Imprima na tela a matriz, a linha de maior soma e a soma.
'''

matriz = []

for lin in range(3):
    linha = []
    for col in range (3):
        linha.append(int(input("Digite um elemento da matriz: ")))
    matriz.append(linha)

for lin in range(3):
    soma_linha = 0
    for col in range(3):
        soma_linha+=matriz[lin][col]
    if (lin == 0):
        maior = soma_linha
        lin_maiorsoma = 0
    else:
        if(soma_linha > maior):
            maior = soma_linha
            lin_maiorsoma = lin

for lin in range(3):
    print(matriz[lin])

print(f"A maior soma eh {maior} e esta na linha {lin_maiorsoma}")

