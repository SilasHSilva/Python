def main():
    matriz = []
    carrega_matriz(matriz, 3, 6)
    exibe_matriz(matriz, 3)
    print(f"Lista das somas dos elementos das colunas de índice ímpar: {cria_lista (matriz,3,6)}")



def carrega_matriz (matriz,nlin,ncol):
    for lin in range(nlin):
        linha = []
        for col in range(ncol):
            linha.append(int(input("Digite um elemento da matriz: ")))
        matriz.append(linha)

def exibe_matriz (matriz,nlin):
    for lin in range(nlin):
        print(matriz[lin])

def cria_lista (matriz,nlin,ncol):
    listaB = []
    for col in range(ncol):
        soma = 0
        for lin in range(nlin):
            if (col % 2 != 0):
                soma+=matriz[lin][col]
        if (soma!=0):
            listaB.append(soma)
    return(listaB)

if (__name__ == "__main__"):
    main()