#exemplo: substituir elemento igual a 0 (zero) por -1
matriz = []
nlin = 3
ncol = 4
for lin in range(0,nlin):
    linha = []
    for col in range(0,ncol):
        #inserir os elementos na linha (sublista)
        elem = int(input("Digite um elemento da linha "+str(lin+1)+" :"))
        linha.append(elem)
    #insere a linha na matriz
    matriz.append(linha)

print("\n")
#imprimir a matriz na forma tradicional (por linhas)
for lin in range(0,nlin):
    print(matriz[lin])

#percorrer a matriz para encontrar 0 e substituir por -1
for lin in range(0,nlin):
    for col in range(0,ncol):
        if (matriz[lin][col] == 0):
            matriz[lin][col] = -1

print("\n")
#imprimir a matriz na forma tradicional (por linhas)
for lin in range(0,nlin):
    print(matriz[lin])