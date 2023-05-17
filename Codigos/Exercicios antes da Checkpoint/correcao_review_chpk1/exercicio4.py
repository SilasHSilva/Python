resp = 1

total = 0

while (resp != 0):
    print("1-Porcao de fritas")
    print("2-Porção de pastéis")
    print("3-Tábua de frios")
    print("4-Porção de peixes")
    print("5-Cerveja")
    cod_produto = int(input("Digite o codigo do produto: "))
    qtde_produto = int(input("Digite a quantidade do produto: "))

    match cod_produto:
        case 1:
            subtotal = qtde_produto * 35.00
            total = total + subtotal
        case 2:
            subtotal = qtde_produto * 25.00
            total = total + subtotal
        case 3:
            subtotal = qtde_produto * 40.00
            total = total + subtotal
        case 4:
            subtotal = qtde_produto * 55.00
            total = total + subtotal
        case 5:
            subtotal = qtde_produto * 18.00
            total = total + subtotal
        case _:
            print("Codigo invalido")

    resp = int(input("Deseja continuar (1-SIM e 0-NAO)? "))

print(f"Total consumido no dia: {total:.2f}")