def main():
    valor_n = int(input("Digite o valor de n: "))

    print(f"Tabuada do {n}: {calcula_tabuada (valor_n)}")
    print(f"Fatorial de {n} eh {calcula_fatorial (valor_n)}")


def calcula_tabuada (n):
    listaA = []
    for i in range (0,11):
        tab = n * i
        listaA.append(tab)

    return(listaA)

def calcula_fatorial (n):
    fat = 1

    for i in range (1,n+1):
        fat = fat * i

    return (fat)

if (__name__ == "__main__"):
    main()