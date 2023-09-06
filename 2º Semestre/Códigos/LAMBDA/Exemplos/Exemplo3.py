# Primeira situação (LAMBDA separada do MAP)

calcula_dobro = lambda num : num * 2

lista = [3,5,4,2,8]
lista_dobro = list(map(calcula_dobro,lista))
print(lista_dobro)

# Segunda situação (LAMBDA com o MAP)

lista = [9,3,7,4,11]
lista_dobro = list(map(lambda num : num * 2,lista))
print(lista_dobro)