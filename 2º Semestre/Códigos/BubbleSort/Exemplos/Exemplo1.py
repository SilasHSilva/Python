def main():

    lista = ["Silas","Luiz","Jefferson","Édipo","Eduardo"]

    bublleSort(lista)

    print(lista)


def bublleSort(lista):
    tam = len(lista)
    for i in range(tam-1,0,-1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp


if (__name__ == "__main__"):
    main()