'''
Escreva um programa com a função “main”, o qual deverá ter uma função que receba duas listas como parâmetros
(uma lista de preços e outra de quantidades de cada produto comprado), o valor do produto e a quantidade
comprada. A função deverá inserir nas listas o valor comprado e a quantidade, respectivamente.
O programa deverá solicitar ao usuário a quantidade do produto, bem como seu preço até que seja digitada
uma opção para saída (por exemplo, 1-continuar e 0-sair). Na sequência, após a digitação dos produtos,
utilizando conceitos da função lambda e map, crie uma nova lista com o valor total de cada item
(quantidade x produto) e, por fim, calcule o valor total da compra. OBS: o programa deve ter,
obrigatoriamente, a função “main”.

'''

def main():
    lista_valor = []
    lista_qtde = []

    resp = 1

    while (resp != 0):
        valor = float(input("Digite o valor: "))
        qtde = int(input("Digite a quantidade: "))
        insere(lista_valor,lista_qtde,valor,qtde)
        resp = int(input("Deseja continuar (1-SIM / 0-NÃO)? "))

    valor_total = sum(list(map(lambda valor,qtde : valor*qtde,lista_valor,lista_qtde)))

    print(f"O valor total da compra é: {valor_total:.2f}")

def insere(lista_valor,lista_qtde,valor,qtde):
    lista_valor.append(valor)
    lista_qtde.append(qtde)

if (__name__ == "__main__"):
    main()
