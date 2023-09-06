def main():
    lista_numeros = []
    tam = int(input("Digite o tamanho da lista: "))
    carrega_lista (lista_numeros,tam)
    soma,media = calcula_somamedia(lista_numeros, tam)
    print(f"Somatorio dos elementos da lista: {soma}")
    print(f"Media dos elementos da lista: {media}")

def carrega_lista (lista_numeros,tam):
    for i in range(0,tam):
        lista_numeros.append(int(input("Digite um elemento da lista: ")))

def calcula_somamedia(lista_numeros, tam):
    soma = 0
    for i in range(0,tam):
        soma+=lista_numeros[i]
    
    media = soma / tam
    return(soma,media)

if (__name__ == "__main__"):
    main()