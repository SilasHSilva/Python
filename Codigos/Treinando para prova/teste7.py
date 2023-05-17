'''
Escreva um programa em Python que leia uma matriz M [5x5] e, a cada linha, multiplique 
cada elemento pelo valor do elemento inserido na diagonal principal da linha. 
Os elementos da matriz serão fornecidos pelo usuário. Escrever a matriz M lida e a matriz M modificada.
'''

'''matrizM = []

for lin in range(5):
    linha = []
    for col in range(5):
        element = int(input("Digite um elemento da matriz: "))
        linha.append(element)
    matrizM.append(linha)

for i in range(5):
    print(matrizM(linha))

for lin in range(5):
    linha = []
    for col in range(5):
        if (lin == col):
            matrizMod[lin][col] = matrizM[lin] * 
'''

# Criando a matriz M[5x5]
M = []
for i in range(3):
    linha = []
    for j in range(5):
        valor = int(input("Digite um valor para M[{}][{}]: ".format(i, j)))
        linha.append(valor)
    M.append(linha)

# Imprimindo a matriz M lida
print("Matriz M:")
for i in range(5):
    for j in range(5):
        print(M[i][j], end=" ")
    print()

# Multiplicando cada elemento pelo valor da diagonal principal
for i in range(5):
    diagonal = M[i][i]
    for j in range(5):
        M[i][j] *= diagonal

# Imprimindo a matriz M modificada
print("\nMatriz M modificada:")
for i in range(5):
    for j in range(5):
        print(M[i][j], end=" ")
    print()

