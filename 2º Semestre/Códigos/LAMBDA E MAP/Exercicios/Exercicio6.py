'''
cl1) Utilizando os conceitos de funções lambda e Map, calcule o somatório 
dos valores pares e ímpares de uma lista. DICA: deverão ser geradas duas listas 
(uma para os pares e outra para os ímpares) para fazer as somas. Para tanto, utilize a função SUM.
'''

lista_numeros = [1,2,3,4,5,6,7,8,9]

numeros_pares = list(map(lambda x: x if x % 2 == 0 else 0, lista_numeros))
numeros_impares = list(map(lambda x: x if x % 2 != 0 else 0, lista_numeros))

numeros_pares = list(filter(lambda x: x != 0, numeros_pares))
numeros_impares = list(filter(lambda x: x != 0, numeros_impares))

soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)

print("Lista Original", lista_numeros)
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)






