def main():
    matriz = []
    nlin = int(input("Digite o numero de linhas da matriz: "))
    ncol = int(input("DIgite o numero de colunas da matriz: "))
    carrega_matriz(matriz, nlin, ncol)
    print(f"Soma dos impares da matriz: {calcula_somaimpares (matriz, nlin, ncol)}")
    exibe_matriz(matriz, nlin)


def carrega_matriz (matriz, nlin, ncol):
    for lin in range(0,nlin):
        linha = []
        for col in range(0,ncol):
            linha.append(int(input("Digite um elemento da lista: ")))
        matriz.append(linha)

def calcula_somaimpares (matriz, nlin, ncol):
    soma = 0
    for lin in range (0,nlin):
        for col in range (0,ncol):
            if (matriz[lin][col] % 2 != 0):
                soma+=matriz[lin][col]
    return(soma)

def exibe_matriz (matriz, nlin):
    for lin in range (0,nlin):
        print(matriz[lin])

if (__name__ == "__main__"):
    main()
