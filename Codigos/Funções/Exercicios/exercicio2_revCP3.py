def main():
    lista = []
    tam = int(input("Digite o tamanho da lista: "))
    carrega_lista(lista, tam)
    cont_impares, perc_impares = conta_impares (lista)
    print(f"Quantidade de impares da lista: {cont_impares}")
    print(f"Percentual de impares da lista: {perc_impares:.2f}%")
    print(f"Lista com o triplo dos elementos: {retorna_triplolista (lista)}")



def carrega_lista (lista,tam):
    for i in range (0,tam):
        lista.append(int(input("Digite um numero da lista: ")))

def conta_impares (lista):
    tam = len(lista)
    cont_impares = 0
    for i in range(0,tam):
        if (lista[i] % 2 != 0):
            cont_impares+=1

    percent_impares = (cont_impares / tam) * 100

    return(cont_impares,percent_impares)

def retorna_triplolista (lista):
    tam = len(lista)
    lista_triplo = []
    for i in range(0, tam):
        lista_triplo.append(lista[i] * 3)

    return(lista_triplo)


if (__name__ == "__main__"):
    main()