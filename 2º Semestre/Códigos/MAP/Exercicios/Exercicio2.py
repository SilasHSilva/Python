'''
Dada as listas abaixo, faça uma função que calcule o preço final de cada item dado 
os descontos para cada um deles. OBS: o programa deve ter, obrigatoriamente, a função “main”.
# listaOriginal = [234, 64, 13467, 45.89, 23]
# listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]
'''

def main():
    lista_original = [234, 64, 13467, 45.89, 23]
    lista_descontos = [0.3, 0.004, 0.5, 0.03, 0.8]

    lista_preco_desc = list(map(calcula_desconto,lista_original,lista_descontos))

    print(lista_preco_desc)


def calcula_desconto(preco,desc):
    preco_desc = preco - (preco * desc)
    return (preco_desc)

if (__name__ == "__main__"):
    main()