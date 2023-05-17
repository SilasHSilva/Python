'''
Escreva um programa em Python para ler duas listas A e B com 10 elementos cada. 
Construir uma lista C, sendo esta a junção das 2 outras listas. Desta forma C deve ter o dobro de 
elementos em relação às listas A e B, ou seja, a lista C deverá possuir 20 elementos. Apresentar a lista C.
'''

listaA = []
listaC = []

for a in range(10):
    element_A = int(input("Digite um elemento da lista A: "))
    listaA.append(element_A)
    listaC.append(element_A)

listaB = []

for b in range(10):
    element_B = int(input("Digite um elemento da lista B: "))
    listaB.append(element_B)
    listaC.append(element_B)



'''for c in range(6):
    element_C = element_A and element_B
    listaC.append(element_C)
'''
print(listaA)
print(listaB)
print(listaC)