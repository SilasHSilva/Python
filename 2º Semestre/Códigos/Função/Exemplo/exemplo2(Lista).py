def main():
    lista = []
    tam = int(input("Digite o tamanho da lista: "))
    carrega_lista(lista,tam)

    soma_pares, soma_impares = soma_pares_impares_lista(lista,tam)
    print(f"Soma dos pares: {soma_pares}")
    print(f"Soma dos impares: {soma_impares}")

    exibe_lista(lista,tam)

def carrega_lista(lista,tam):
    for i in range (tam):
        num = int(input("Digite um elemento da lista: "))
        lista.append(num)

def soma_pares_impares_lista(lista,tam):
    soma_pares = 0
    soma_impares = 0
    for i in range(tam):
        if (lista[i] % 2 == 0):
            soma_pares += lista[i]
        else:
            soma_impares += lista[i]
    return (soma_pares,soma_impares)

def exibe_lista(lista,tam):
    for i in range(tam):
        print(lista[i])

if (__name__ == "__main__"):
    main()        