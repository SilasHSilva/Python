
soma = 0

for cont in range (0,10):
    num = int(input("Digite um numero: "))
    if (num < 40):
        soma+=num

print(f"Soma dos numeros inferiores a 40: {soma}")