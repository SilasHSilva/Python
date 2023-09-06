
soma_pares = 0

for i in range (1,21):
    if (i % 2== 0):
        soma_pares = soma_pares + i  # soma_pares+=i

print(f"Soma dos pares de 1 a 20: {soma_pares}")