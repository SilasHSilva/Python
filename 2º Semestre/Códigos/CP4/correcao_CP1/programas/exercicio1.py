'''
Uma empresa decidiu dar um bônus aos salários dos funcionários de acordo com o total vendido por cada um
nos últimos 3 meses. Se o total vendido pelo funcionário for até R$5000.00, então o bônus será de 10%;
caso contrário, o bônus será de 20%. Nesse sentido, escreva uma função map, com notação lambda,
em Python que retorne uma lista de salários com os devidos bônus para 10 funcionários. Os salários e
o total de vendas dos funcionários deverão ser digitados pelo usuário.
'''

lista_salarios = []
lista_vendas = []

for i in range(10):
    lista_salarios.append(float(input("Digite o salário do funcionário: ")))
    lista_vendas.append(float(input("Digite o total de vendas do funcionário: ")))

lista_novos_salarios = list(map(lambda salario,total_vendas : salario * 1.10 if (total_vendas <= 5000) else salario * 1.20,lista_salarios,lista_vendas))

print(lista_novos_salarios)
