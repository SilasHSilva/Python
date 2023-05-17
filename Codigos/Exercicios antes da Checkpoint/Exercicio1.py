#compra de materiais escolares

print("1 - Caneta")
print("2 - Lápis")
print("3 - Caderno")

opc_prod = int(input("Digite o que gostaria de comprar (1 - 3): "))
preco_prod = float(input("Informe o preço desse produto: "))
qtd_prod = int(input("Qual a quantidade que você gostaria de comprar: "))

if(opc_prod == 1):
    print(f"O valor total de canetas eh: {preco_prod*qtd_prod-(5/100*preco_prod*qtd_prod):.2f}")
elif(opc_prod == 2):
    print(f"O valor total de lapis eh: {preco_prod*qtd_prod:.2f}")
elif(opc_prod == 3):
    print(f"O valor total de cadernos eh: {preco_prod*qtd_prod-(20/100*preco_prod*qtd_prod):.2f}")

