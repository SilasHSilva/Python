
soma_positivos = 0
cont_positivos = 0

for i in range (8):
    num = int(input("Digite um numero: "))
    if (num >= 0):
        soma_positivos+=num
        cont_positivos+=1

media = soma_positivos / cont_positivos

print(f"Soma dos positivos: {soma_positivos}")
print(f"Media dos positivos: {media:.2f}")