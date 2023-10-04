'''
Escreva uma função map, com notação lambda, em Python que retorne uma lista com 0 caso a palavra não seja
um palíndromo e 1 caso ela seja. Isso deve ser feito para uma lista com 5 palavras digitadas pelo usuário.
'''

lista_palavras = []

for i in range(5):
    lista_palavras.append(input("Digite uma palavra: "))

lista_palindromos = list(map(lambda palavra : 1 if (palavra == palavra[::-1]) else 0,lista_palavras))

print(lista_palindromos)
