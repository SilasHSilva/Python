inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))

cont = inicio
cont_pares = 0
cont_impares = 0

while (cont <= fim):
    if (cont % 2 == 0):
        cont_pares+=1
    else:
        cont_impares+=1
    cont+=1

print(f"Quantidade de pares de {inicio} a {fim}: {cont_pares}")
print(f"Quantidade de impares de {inicio} a {fim}: {cont_impares}")