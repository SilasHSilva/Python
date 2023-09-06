
cont = 0

for i in range (0,6):
    num = int(input("Digite um numero: "))
    if (num >= 0):
        if (cont == 0): #primeiro nro positivo digitado
            maior = num
        else:
            if (num > maior): #achou um nro maior do que o que estava armazenado em "maior"
                maior = num
        cont+=1

print(f"Maior dos positivos: {maior}")
