#Escreva um programa que leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

matriz = []

for lin in range(4):
    linha = []
    for col in range (4):
        linha.append(int(input("Digite um elemento da matriz: ")))
    matriz.append(linha)


cont_maior10 = 0
for lin in range(4):
    for col in range(4):
        if (matriz[lin][col] > 10):
            cont_maior10+=1

print(f"Valores maiores que 10 da matriz: {cont_maior10}")