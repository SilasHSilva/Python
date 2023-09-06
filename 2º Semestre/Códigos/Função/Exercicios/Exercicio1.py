'''
1) Escreva um programa em Python (estrutura “main”) que contenha as seguintes funções:
a) Uma função que faça a leitura dos dados de uma lista numérica, sendo a lista e seu tamanho como parâmetros.
b) Uma função que retorne o maior e o menor elemento da lista, sendo a lista e seu tamanho como parâmetros.
c) Uma função que faça a busca de um determinado número na lista e retorne 
o índice a posição onde ele se encontra (lista e tamanho como parâmetros). 
Caso o elemento não seja encontrado, a função deverá retornar -1.
'''

def main():
    lista = []
    tam = int(input("Digite o tamanho da Lista: "))
    carrega_lista(tam,lista)
    maior,menor = exibe_maior_menor(tam,lista)
    print(f"O maior elemento da lista eh {maior}")
    print(f"O menor elemento da lista eh {menor}")

    elem = int(input("Digite o elemento a ser procurado na lista: "))
    pos = busca_elementos_lista(lista,tam,elem)

    if (pos != -1):
        print(f"O elemento foi encontrado na posição {pos}")
    else:
        print("O elemento nao se encontra na lista")


def carrega_lista(tam,lista):
    for i in range(tam):
        num = int(input("Digite um numero da lista: "))
        lista.append(num)


def exibe_maior_menor(tam,lista):
    maior = lista[0]
    menor = lista[0]

    for i in range (1,tam):
        if (lista[i] > maior):
            maior = lista[i]
        if (lista[i] < menor):
            maior = lista[i]
    return (maior,menor)

def busca_elementos_lista(tam,lista,elem):
    pos = -1
    for i in range(tam):
        if(lista[i] == elem):
            pos = i
    return(pos)
            
    

if (__name__ == "__main__"):
    main()
