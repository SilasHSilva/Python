qtde_dentro_interv = 0
qtde_fora_interv = 0

for cont in range (10):
    num = int(input("Digite um numero: "))
    if (num >= 10 and num <=20):
        qtde_dentro_interv+=1
    else:
        qtde_fora_interv+=1

print(f"Quantidade de numeros no intervalo [10,20]: {qtde_dentro_interv}")
print(f"Quantidade de numeros fora do intervalo [10,20]: {qtde_fora_interv}")