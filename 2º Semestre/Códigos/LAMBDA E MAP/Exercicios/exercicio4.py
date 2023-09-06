'''
4) Uma função que calcule uma nova lista baseada em uma lista de acordo 
com a seguinte regra: quando o elemento da lista for par, adicione 5 a 
este número e, caso contrário, subtraia 2. OBS: estes elementos modificados deverão 
fazer parte da nova lista. Para tanto, utilize o conceito de MAP com função LAMBDA.
'''

lista_numeros = [4, 3, 6, 7, 5, 8, 11, 20]

nova_lista = list(map(lambda num : num + 5 if (num % 2 == 0) else num - 2,lista_numeros))

print(nova_lista)