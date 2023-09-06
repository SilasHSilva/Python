def main():

    lista_precos = []
    lista_qtdes = []
    resp = 1

    while (resp != 0):
        preco = float(input("Digite o preco do produto comprado: "))
        qtde = int(input("Digite a quantidade desejada do produto: "))
        insere_preco_qtde (lista_precos, lista_qtdes, preco, qtde)
        resp = int(input("Deseja continuar (1 - SIM / 0 - NÃO)"))

    lista_subtotais = sum(list(map(lambda preco,qtde : preco*qtde,lista_precos,lista_qtdes)))

    print(f"O total da compra é {lista_subtotais: .2f}")



def insere_preco_qtde (lista_precos, lista_qtdes, preco, qtde):
    lista_precos.append(preco)
    lista_qtdes.append(qtde)

if(__name__ == "__main__"):
    main()