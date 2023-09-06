num = int(input("Digite um numero: "))
cont = 1
while (num > 0):
    if (cont==1):
        maior = num
        menor = num
    else:
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num
    cont+=1
    num = int(input("Digite um numero: "))


print(f"Maior: {maior}")
print(f"Menor: {menor}")
