'''
Elaborar um programa em Python que efetue o cálculo de uma tabuada de um número 
qualquer e armazene os resultados em uma lista A para 11 elementos. Apresentar os valores armazenados na lista.
'''
num = int(input("Digite o numéro que quer fazer a tabuada: "))
listaA = []

print(f"A tabuada do {num} eh:")
for i in range(11):
    res = num*i
    print(num, "x", i , "=", res)
    listaA.append(res)

print(listaA)    

