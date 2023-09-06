#Faça um programa em Python que conte o número de 1’s que aparecem em uma string. Exemplo: “0011001” = 3.

num = input("Digite um numero: ")

tam = len(num)

cont_num = 0
for i in range(tam):
    if (num[i] == "1"):
        cont_num +=1

print(f"A quantidade de numeros '1' desse numero é {cont_num}")