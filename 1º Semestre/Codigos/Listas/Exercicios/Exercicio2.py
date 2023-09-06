lista_idades = []

soma_idades = 0
qtde_menores18 = 0

idade = int(input("Digite a idade o usuario: "))

while (idade > 0):
    lista_idades.append(idade)
    idade = int(input("Digite a idade do usuario: "))

for i in range(len(lista_idades)):
    soma_idades+=lista_idades[i]
    if(lista_idades[i] < 18):
        qtde_menores18+=1
    
media_idades = soma_idades / len(lista_idades) # sum(lista_idades) / len(lista_idades)

print(f"Media de idades: {media_idades:.2f}")
print(f"Quantidade de usuarios menores de 18 anos: {qtde_menores18}")
