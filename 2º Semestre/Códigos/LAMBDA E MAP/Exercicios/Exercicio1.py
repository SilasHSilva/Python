'''1 - Faça uma função lambda que:
§ Retorne o oposto de um número
§ Retorne o inverso de um número
§ Calcule a metade de um número
§ Calcule a soma de quadrados de dois número
§ Imprima o nome e idade de uma pessoa
§ Retorne 0 se o valor for PAR e 1 se for ÍMPAR
§ Calcule o triplo de um número
§ Retorne se a pessoa é maior de idade'''

# Retorne o oposto de um número
converte_oposto = lambda num : -num
print(converte_oposto(-7))

# Retorne o inverso de um número
converte_inverso = lambda num: 1/num
print(converte_inverso(4))

# Calcule a metade de um número
calcula_metade = lambda num : num/2
print(calcula_metade(6))

# Calcule a soma de quadrados de dois número
calcula_soma_quadrados = lambda a,b : a**2 + b**2
print(calcula_soma_quadrados(7,5))

# Imprima o nome e idade de uma pessoa
imprime_dados = lambda nome,idade : print(f"{nome} tem {idade} anos")
imprime_dados("João" , 20)

# Retorne 0 se o valor for PAR e 1 se for ÍMPAR

verifica_parimpar = lambda x : 1 if (x % 2 == 0) else 0
print(verifica_parimpar(9))

# Calcule o triplo de um número
calcula_triplo = lambda p : 3 * p
print(calcula_triplo(8))

# Retorne se a pessoa é maior de idade
verifica_maioridade = lambda idade : print("A pessoa é maior de idade") if (idade >= 18) else print("A pessoa não é maior de idade")
verifica_maioridade(17)
