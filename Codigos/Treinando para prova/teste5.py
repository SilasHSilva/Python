'''Escreva um programa em Python para ler 12 elementos inteiros para uma lista A.
Construir uma lista B de mesmo tipo e dimensão, observando a seguinte lei de formação: 
"Todo elemento da lista A que for ímpar deve ser multiplicado por 2; 
caso contrário, o elemento da lista A deve permanecer constante". Apresentar a lista B.
'''

listaA = []
listaB = []
impares = 0

for i in range(12):
    element = int(input("Digite um elemento da lista A: "))
    listaA.append(element)
    if element % 2 != 0:
        listaB.append(element*2)
        impares+=1
    else:
        listaB.append(element)

print(listaA)
print(listaB)
print(impares)
