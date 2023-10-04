lista_numeros = [3, 1, 5, 4, 8, 2]

nova_lista = list(map(lambda num : num+5 if (num % 2 == 0) else num-2,lista_numeros))

print(nova_lista)