#exemplo: somatorio dos elementos matriz
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

soma = 0
#percorrer a matriz para fazer o somatorio
for lin in range(0,nlin):
    for col in range(0,ncol):
        soma = soma + matriz[lin][col]

print(f"Somatorio dos elementos da matriz: {soma}")