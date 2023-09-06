def main():
    matriz = []
    nlin = int(input("Digite o numero de linhas: "))
    ncol = int(input("Digite o numero de colunas: "))

    carrega_matriz(matriz, nlin,ncol)
    
    print(f"A média dos elementos da matriz é {calcula_media_matriz(matriz,nlin,ncol):.2f}")


def carrega_matriz(matriz,nlin,ncol):
    for lin in range (nlin):
        linha = []
        for col in range(ncol):
            linha.append(int(input("Digite um elemento da matriz: ")))
        matriz.append(linha)

def calcula_media_matriz(matriz,nlin,ncol):
    soma = 0
    for lin in range(nlin):
        for col in range(ncol):
            soma+=matriz[lin][col]
    
    media = soma / (nlin*ncol)
    return (media)

def exibe_impares(matriz, nlin,ncol):
    for lin in range (nlin):
        for col in range(ncol):
            if (matriz[lin][col] % 2 != 0):
                print(matriz[lin][col])


if (__name__ == "__main__"):
    main()