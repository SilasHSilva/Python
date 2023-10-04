'''
Escreva funções map, com notação lambda, em Python que retorne, a partir de uma lista de 10 números inteiros,
o somatório de todos os números divisíveis por 3, além do somatório dos divisíveis por 4.
'''

lista_numeros = [3,8,6,15,11,20,30,13,27,10]

somatorio_div3 = sum(list(map(lambda num : num if (num % 3 == 0) else 0,lista_numeros)))
somatorio_div4 = sum(list(map(lambda num : num if (num % 4 == 0) else 0,lista_numeros)))

print(f"Somatório dos divisíveis por 3: {somatorio_div3}")
print(f"Somatório dos divisíveis por 4: {somatorio_div4}")
