'''
Escreva um programa em Python que dada uma string com uma frase informada
pelo usuário (incluindo espaços em branco), conte quantos espaços em branco existem na frase.
'''

frase = input("Digite uma frase: ")

tamanho_frase = len(frase)

cont_espaços = 0

for i in range(tamanho_frase):
    if (frase[i] == " "):
        cont_espaços+=1

print(frase)
print(f"A quantidade de espaços dessa frase é {cont_espaços}")