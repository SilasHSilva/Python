palavra = input("Digite uma palavra: ")

tam = len(palavra)
qtde_vogais = 0

for i in range (tam):
    if (palavra[i]=="a" or palavra[i]=="e" or palavra[i]=="i" or palavra[i]=="o" or palavra[i]=="u"):
        qtde_vogais+=1

print(f"Quantidade de vogais: {qtde_vogais}")
