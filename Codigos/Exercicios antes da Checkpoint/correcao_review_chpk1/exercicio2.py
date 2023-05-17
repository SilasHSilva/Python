qtde_porcoes_batatas = int(input("Digite a quantidade de porcoes de batatas: "))
qtde_porcoes_pasteis = int(input("Digite a quantidade de porcoes de pasteis: "))
qtde_cervejas = int(input("Digite a quantidade de cervejas: "))

qtde_amigos = int(input("Quantos amigos para rachar a conta? "))

valor_total = (qtde_porcoes_batatas * 35.00) + (qtde_porcoes_pasteis * 25.00) + (qtde_cervejas * 18.00)

valor_por_amigo = valor_total / qtde_amigos

print(f"Cada amigo deverah pagar R${valor_por_amigo:.2f}")