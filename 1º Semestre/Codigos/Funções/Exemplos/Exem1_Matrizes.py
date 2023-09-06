def main():
    matriz = []
    nlinhas = int(input("Digite o numero de linhas da matriz: "))
    ncolunas = int(input("Digite o numero de colunas da matriz: "))

    carrega_matriz(matriz, nlinhas, ncolunas)
    exibe_matriz(matriz, nlinhas)
    print(f"Somatorio dos elementos da matriz: {calcula_soma_matriz(matriz, nlinhas, ncolunas)}")
    exibe_pares_matriz(matriz, nlinhas, ncolunas)


def carrega_matriz(matriz, nlin, ncol):
    for i in range(0,nlin):
        linha = []
        for i in range(0,ncol):
            linha.append(int(input("Digite um elemento da matriz: ")))
        matriz.append(linha)

def calcula_soma_matriz(matriz, nlin, ncol):
    soma = 0
    for lin in range(0, nlin):
        for col in range(0, ncol):
            soma+=matriz[lin][col]
        
    return(soma)

def exibe_pares_matriz(matriz, nlin, ncol):
    for lin in range(0, nlin):
        for col in range(0, ncol):
            if (matriz[lin][col] % 2 == 0):
                print("Os numeros pares presentes na lista são:", matriz[lin][col])

def exibe_matriz(matriz, nlin):
    for lin in range(nlin):
        print(matriz[lin])

if (__name__ == "__main__"):
    main()