'''
Escreva um programa em Python para ler 15 elementos de uma lista A. 
Construir uma lista B, observando a seguinte lei de formação: 
“Todo elemento de B deve ser o quadrado do elemento de A correspondente". Apresentar as listas A e B.
'''

listaA = []

for i in range(5):
    element = int(input("Digite um elemento da lista: "))
    listaA.append(element)

listaB = []

for i in range(5):
    dobro = element ** 2
    listaB.append(dobro)

print(listaA)
print(listaB)