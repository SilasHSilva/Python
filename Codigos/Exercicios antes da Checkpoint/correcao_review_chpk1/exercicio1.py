preco_caneta = float(input("Digite o preco da caneta: "))
preco_lapis = float(input("Digite o preco do lapis: "))
preco_caderno = float(input("Digite o preco do caderno: "))

qtde_caneta = int(input("Digite a quantidade de canetas: "))
qtde_lapis = int(input("Digite a quantidade de lapis: "))
qtde_caderno = int(input("Digite a quantidade de cadernos: "))

preco_caderno_desc = preco_caderno - (preco_caderno * (20/100))
preco_caneta_desc = preco_caneta - (preco_caneta * (5/100))

valor_total = (qtde_caneta * preco_caneta_desc) + (qtde_lapis * preco_lapis) + (qtde_caderno * preco_caderno_desc)

print(f"Valor total da compra: {valor_total:.2f}")