#for encadeado

for i in range (0,3):
    print("-----------------")
    for j in range (0,4):
        print(i, " ", j)

#leitura dos elementos da matriz
matriz = []
nlin = 3
ncol = 3
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
