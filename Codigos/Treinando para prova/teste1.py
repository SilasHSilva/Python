'''
Escreva um programa em Python para ler uma lista A com 10 elementos numéricos inteiros.
Apresentar o total de elementos ímpares existentes na lista e o percentual do valor 
total de números ímpares em relação à quantidade total de elementos armazenados na lista.
'''

listaA = []
cont_impares = 0

for i in range(10):
    elemento = int(input("Digite um elemento da lista: "))
    listaA.append(elemento)
    if elemento % 2 != 0:
        cont_impares+=1

percent_impares = cont_impares / len(listaA) * 100

print("Lista completa: ", listaA)
print("Quantidade de elementos impares dessa lista: ", cont_impares)
print("Percentual de elementos impares em relação ao numero total de elementos da lista: " , percent_impares,"%")